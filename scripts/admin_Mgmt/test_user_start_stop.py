import logging
import re
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import page.Login
from page import admin_Mgmt, role_Mgmt
from page.Login.page_login import PageLogin
from page.admin_Mgmt.page_admin_Mgmt import PageAdminMgmt
from page.role_Mgmt.page_role_Mgmt import PageRoleMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


# 测试用户启用、暂停
class TestUserStartStopMgmt:
    logger = logging.getLogger(__name__)

    @pytest.fixture()
    def admin_stop_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        yield
        self.admin_stop_logout()

    def admin_stop_logout(self):
        sleep(3)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.fixture()
    def admin_quit_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        yield
        self.admin_quit_logout()

    def admin_quit_logout(self):
        sleep(3)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.fixture()
    def admin_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        yield
        self.admin_logout()

    def admin_logout(self):
        sleep(3)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.mark.run('first')
    @pytest.mark.usefixtures("admin_login")
    @pytest.mark.parametrize("username,email,password,surname,name", [(GetYaml("user_Mgmt.yaml").get_normaluserMgmt())])
    def test_a_user_add(self, username, email, password, surname, name):
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        self.logger.info("返回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.search_user(adduser)
        self.logger.info("返回第一行用户信息")
        self.pageadminMgmt.page_get_username()
        if self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_firstuser_ID).strip() != "暂无数据":
            self.logger.info("用户已存在，先删除，后创建")
            self.pageadminMgmt.delete_user(adduser)
        elif self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_firstuser_ID).strip() == "暂无数据":
            self.logger.info("用户不存在，直接创建用户")
        else:
            self.logger.error("出错了")
        self.logger.info("开始创建用户")
        self.add_user(username, email, password, surname, name)


    @pytest.fixture()
    def user_start_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("普通用户用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("普通用户用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        self.user_start_logout()

    def user_start_logout(self):
        element = self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_dev_list)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        self.role_pagelogin.page_logout()
        GetDriver.quit_web_driver()

    def add_user(self, username, email, password, surname, name):
        self.logger.info("清空搜索")
        self.pageadminMgmt.empty_search_user()
        self.logger.info("取用户的数量")
        fFirst = self.pageadminMgmt.page_get_user_count()
        fcFirst = fFirst.split(sep=' ')[2]
        self.logger.info("创建前:{}".format(fcFirst))
        reg = r"(\d+)"
        pre = re.search(reg, fcFirst).group(1)
        self.logger.info("新建用户")
        self.pageadminMgmt.page_create_user_before()
        self.pageadminMgmt.page_create_user_input(username, email, password, surname, name)
        self.pageadminMgmt.page_create_user_confirm()
        sleep(3)
        fEnd = self.pageadminMgmt.page_get_user_count()
        fcEnd = fEnd.split(sep=' ')[2]
        self.logger.info("创建后:{}".format(fcEnd))
        post = re.search(reg, fcEnd).group(1)
        try:
            assert int(pre) + 1 == int(post)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pageadminMgmt.insert_image()
            self.logger.info("判断窗口是否还在，如果存在，click 取消，避免影响其他的测试用例")
            if self.pageadminMgmt.is_element_present(page.admin_Mgmt.adminMgmt_adduser_cancel):
                self.logger.info("窗口还在,click 取消")
                self.pageadminMgmt.element_click(page.admin_Mgmt.adminMgmt_adduser_cancel)
            raise
        try:
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_state) == '启用'
        except Exception as e:
            self.logger.error("新创建的用户状态应该为启用")
            self.pageadminMgmt.insert_image()
            raise

    @pytest.mark.run('second')
    @pytest.mark.usefixtures("user_start_login")
    def test_b_user_role_judge_dev(self):
        self.user_dev_judge_vstudio()

    def user_dev_judge_vstudio(self):
        self.role_pageroleMgmt.page_dev_list()
        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[0] == '主页'
        except Exception as e:
            self.logger.error("未找到主页菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[1] == '工作空间'
        except Exception as e:
            self.logger.error("未找到工作空间菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[2] == '最近改动'
        except Exception as e:
            self.logger.error("未找到最近改动菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[3] == '最近执行'
        except Exception as e:
            self.logger.error("未找到最近执行菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[4] == '收藏夹'
        except Exception as e:
            self.logger.error("未找到收藏夹菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[5] == '文件管理'
        except Exception as e:
            self.logger.error("未找到文件管理菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[6] == '部署历史'
        except Exception as e:
            self.logger.error("未找到部署历史菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[7] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[8] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[9] == '参数配置'
        except Exception as e:
            self.logger.error("未找到参数配置菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[10] == '事件历史'
        except Exception as e:
            self.logger.error("未找到事件历史菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_1()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_main)
        except Exception as e:
            self.logger.error("打开的主页页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_2()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_workspace_main)
        except Exception as e:
            self.logger.error("打开的工作空间页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_3()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_changes_main)
        except Exception as e:
            self.logger.error("打开的最近改动页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_4()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_perform_main)
        except Exception as e:
            self.logger.error("打开的最近执行页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_5()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_favorites_main)
        except Exception as e:
            self.logger.error("打开的收藏夹页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_6()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_File_management_main)
        except Exception as e:
            self.logger.error("打开的文件管理页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_7()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_history_main)
        except Exception as e:
            self.logger.error("打开的部署历史页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_8()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_9()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_10()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Parameter_configuration_main)
        except Exception as e:
            self.logger.error("打开的参数配置页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_main_11()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Events_history_main)
        except Exception as e:
            self.logger.error("打开的事件历史页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

    @pytest.mark.run('third')
    @pytest.mark.usefixtures("admin_stop_login")
    def test_c_user_stop(self):
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        self.logger.info("返回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.search_user(adduser)
        self.logger.info("返回第一行用户信息")
        self.pageadminMgmt.page_get_username()
        self.logger.info("点击暂停按钮")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_stop_start_btn)
        try:
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_stop_confirm) == "停用用户"
        except Exception as e:
            self.logger.error("未显示确认停用用户")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_stop_warning)
        except Exception as e:
            self.logger.error("未显示警告")
            self.pageadminMgmt.insert_image()
            raise

        self.logger.info("点击确定按钮")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_stop_confirm_btn)

        # self.driver.switch_to.alert()
        # try:
        #     assert "停用用户 lhx1227 成功" in self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_stop_success)
        # except Exception as e:
        #     self.logger.error("没有停用成功的弹框提示")
        #     self.pageadminMgmt.insert_image()
        #     raise

        try:
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_state) == '暂停'
        except Exception as e:
            self.logger.error("点击后用户状态应该暂停")
            self.pageadminMgmt.insert_image()
            raise

    @pytest.fixture()
    def user_stop_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("普通用户用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("普通用户用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        self.user_stop_logout()

    def user_stop_logout(self):
        sleep(3)
        GetDriver.quit_web_driver()

    @pytest.mark.run('fourth')
    @pytest.mark.usefixtures("user_stop_login")
    def test_d_user_role_judge_dev(self):
        sleep(3)
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_stop_login_text)
        except Exception as e:
            self.logger.error("没有获取到用户停用信息")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert "Account is disabled, contact your administrator." in self.role_pageroleMgmt.element_get_text(role_Mgmt.roleMgmt_stop_login_text)
        except Exception as e:
            self.logger.error("未提示用户已停用")
            self.role_pageroleMgmt.insert_image()
            raise

    @pytest.mark.run('fifth')
    @pytest.mark.usefixtures("admin_quit_login")
    def test_f_admin_delete_user(self):
        self.delete_user()

    def delete_user(self):
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        self.logger.info("返回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.search_user(adduser)
        self.logger.info("返回第一行用户信息")
        self.pageadminMgmt.page_get_username()
        self.logger.info("删除用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.delete_user(adduser)
        self.logger.info("清空搜索")
        self.pageadminMgmt.empty_search_user()





