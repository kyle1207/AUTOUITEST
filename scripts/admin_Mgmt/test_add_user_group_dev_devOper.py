import logging
import re
from time import sleep

import pytest
from selenium.webdriver import ActionChains

import page.Login
from page import admin_Mgmt, role_Mgmt
from page.Login.page_login import PageLogin
from page.admin_Mgmt.page_admin_Mgmt import PageAdminMgmt
from page.role_Mgmt.page_role_Mgmt import PageRoleMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestAddUserDevOpGroupMgmt:
    logger = logging.getLogger(__name__)

    @pytest.fixture()
    def admin_login(self):
        self.logger.info("admin登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("admin用户信息")
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.logger.info("admin用户登录")
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        yield
        self.admin_logout()

    def admin_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.fixture()
    def user_dev_devOper_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("开发运营+普通用户用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("开发运营+普通用户用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        self.user_dev_devOper_logout()

    def user_dev_devOper_logout(self):
        element = self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_dev_devOper_1)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        self.role_pagelogin.page_logout()
        GetDriver.quit_web_driver()

    @pytest.fixture()
    def admin_delete_login(self):
        self.logger.info("admin登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("admin用户信息")
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.logger.info("admin用户登录")
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        yield
        self.admin_delete_logout()

    def admin_delete_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.mark.run(order=0)
    @pytest.mark.parametrize("username,email,password,surname,name", [(GetYaml("user_Mgmt.yaml").get_normaluserMgmt())])
    @pytest.mark.usefixtures("admin_login")
    def test_add_user_group_ac_download(self, username, email, password, surname, name):
        self.add_user(username, email, password, surname, name)
        self.add_operator_Usergroup()
        self.add_normalUser_Usergroup()
        self.user_group_assign()

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("user_dev_devOper_login")
    def test_user_role_judge_dev_devOper(self):
        self.user_dev_devOper_judge_vstudio()

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("admin_delete_login")
    def test_delete_user_group_dev_devOper(self):
        self.delete_user_group_dev_devOper()

    def delete_user_group_dev_devOper(self):
        username = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.page_moveto_userMgmt()
        self.pageadminMgmt.delete_user(username)
        self.pageadminMgmt.page_moveto_groupMgmt()
        groupNameList = GetYaml("user_Mgmt.yaml").get_groupNames_Mgmt()
        self.pageadminMgmt.delete_group(groupNameList[8][0])
        self.pageadminMgmt.delete_group(groupNameList[8][1])

    def add_user(self, username, email, password, surname, name):
        self.logger.info("回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
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

    def add_operator_Usergroup(self):
        self.logger.info("创建开发运营用户组")
        groupname, rolename = GetYaml("user_Mgmt.yaml").get_operator_groupMgmt()
        self._add_User_group(groupname, rolename)

    def add_normalUser_Usergroup(self):
        self.logger.info("创建普通用户组")
        groupname, rolename = GetYaml("user_Mgmt.yaml").get_normalUser_groupMgmt()
        self._add_User_group(groupname, rolename)

    def _add_User_group(self, groupname, rolename):
        self.logger.info("回到用户组主页面")
        self.pageadminMgmt.page_moveto_groupMgmt()
        self.logger.info("取用户组的数量")
        fFirst = self.pageadminMgmt.page_get_group_count()
        fcFirst = fFirst.split(sep=' ')[2]
        self.logger.info("创建前:{}".format(fcFirst))
        reg = r"(\d+)"
        pre = re.search(reg, fcFirst).group(1)
        self.logger.info("新建用户组")
        self.pageadminMgmt.page_create_User_group(groupname, rolename)
        sleep(3)
        fEnd = self.pageadminMgmt.page_get_group_count()
        fcEnd = fEnd.split(sep=' ')[2]
        self.logger.info("创建后:{}".format(fcEnd))
        post = re.search(reg, fcEnd).group(1)
        try:
            assert int(pre) + 1 == int(post)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pageadminMgmt.insert_image()
            self.logger.info("判断窗口是否还在，如果存在，click 取消，避免影响其他的测试用例")
            if self.pageadminMgmt.is_element_present(page.admin_Mgmt.adminMgmt_addgroup_cancel):
                self.logger.info("窗口还在,click 取消")
                self.pageadminMgmt.element_click(page.admin_Mgmt.adminMgmt_addgroup_cancel)
            raise

    def user_group_assign(self):
        self.logger.info("开发运营+普通用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        groupNameList = GetYaml("user_Mgmt.yaml").get_groupNames_Mgmt()
        self.assign_usergroup(adduser, groupNameList[8])

    def assign_usergroup(self, adduser, usergroups):
        self.logger.info("对用户进行分组")
        self.logger.info("回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        self.pageadminMgmt.search_user(adduser)
        self.logger.info("对用户进行分组")
        self.pageadminMgmt.user_role(adduser, usergroups)

    def user_dev_devOper_judge_vstudio(self):
        self.role_pageroleMgmt.page_dev_devOper_list()
        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[0] == '主页'
        except Exception as e:
            self.logger.error("未找到主页菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[1] == '工作空间'
        except Exception as e:
            self.logger.error("未找到工作空间菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[2] == '最近改动'
        except Exception as e:
            self.logger.error("未找到最近改动菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[3] == '最近执行'
        except Exception as e:
            self.logger.error("未找到最近执行菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[4] == '收藏夹'
        except Exception as e:
            self.logger.error("未找到收藏夹菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[5] == '文件管理'
        except Exception as e:
            self.logger.error("未找到文件管理菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[6] == '部署历史'
        except Exception as e:
            self.logger.error("未找到部署历史菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[7] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[8] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[9] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[10] == '部署审批'
        except Exception as e:
            self.logger.error("未找到部署审批菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[11] == '参数配置'
        except Exception as e:
            self.logger.error("未找到参数配置菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)[12] == '事件历史'
        except Exception as e:
            self.logger.error("未找到事件历史菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_1()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_main)
        except Exception as e:
            self.logger.error("打开的主页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_2()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_workspace_main)
        except Exception as e:
            self.logger.error("打开的工作空间页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_3()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_changes_main)
        except Exception as e:
            self.logger.error("打开的最近改动页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_4()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_perform_main)
        except Exception as e:
            self.logger.error("打开的最近执行页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_5()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_favorites_main)
        except Exception as e:
            self.logger.error("打开的收藏夹页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_6()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_File_management_main)
        except Exception as e:
            self.logger.error("打开的文件管理页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_7()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_history_main)
        except Exception as e:
            self.logger.error("打开的部署历史页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_8()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_9()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_10()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_11()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)
        except Exception as e:
            self.logger.error("打开的部署审批页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_12()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Parameter_configuration_main)
        except Exception as e:
            self.logger.error("打开的参数配置页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_dev_devOper_main_13()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Events_history_main)
        except Exception as e:
            self.logger.error("打开的事件历史页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise
