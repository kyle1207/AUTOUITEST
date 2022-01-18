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


class TestGroupDeleteMgmt:
    logger = logging.getLogger(__name__)

    # admin选择分组
    @pytest.fixture()
    def admin_assign_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.username, self.email, self.password, self.surname, self.name = GetYaml(
            "user_Mgmt.yaml").get_normaluserMgmt()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.pageadminMgmt.page_moveto_background()
        yield
        self.admin_assign_logout()
        GetDriver.quit_web_driver()

    def admin_assign_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    # 步骤一：创建用户，创建并选择开发运营、数据下载测试组
    @pytest.mark.run('first')
    @pytest.mark.usefixtures("admin_assign_login")
    @pytest.mark.parametrize("username,email,password,surname,name", [(GetYaml("user_Mgmt.yaml").get_normaluserMgmt())])
    def test_add_user_group(self, username, email, password, surname, name):
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
        self.logger.info("创建用户")
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
        self.add_download_Usergroup()
        self.add_operator_Usergroup()
        self.user_group_assign_8()

    def add_download_Usergroup(self):
        self.logger.info("创建下载用户组")
        groupname, rolename = GetYaml("user_Mgmt.yaml").get_downloader_groupMgmt()
        self._add_User_group(groupname, rolename)

    def add_operator_Usergroup(self):
        self.logger.info("创建开发运营用户组")
        groupname, rolename = GetYaml("user_Mgmt.yaml").get_operator_groupMgmt()
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

    def user_group_assign_8(self):
        self.logger.info("数据下载+开发运营")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        groupNameList = GetYaml("user_Mgmt.yaml").get_groupNames_Mgmt()
        self.assign_usergroup(adduser, groupNameList[1])

    def assign_usergroup(self, adduser, usergroups):
        self.logger.info("对用户进行分组")
        self.logger.info("回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        self.pageadminMgmt.search_user(username=GetYaml("user_Mgmt.yaml").find_userMgmt())
        self.logger.info("对用户进行分组")
        self.pageadminMgmt.user_role(adduser, usergroups)

    @pytest.fixture()
    def user_devOper_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("开发运营用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("开发运营用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        self.user_devOper_logout()

    def user_devOper_logout(self):
        element = self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_devOper_1)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        self.role_pagelogin.page_logout()
        GetDriver.quit_web_driver()

    # 步骤三：登录开发运营平台：验证开发运营测试组菜单权限是否正常
    @pytest.mark.run('third')
    @pytest.mark.usefixtures("user_devOper_login")
    def test_user_role_judge_devOper(self):
        self.logger.info("创建的用户登录开发运营平台：开发运营测试组菜单权限是否正常")
        self.user_devOper_judge_vstudio()

    def user_devOper_judge_vstudio(self):
        self.role_pageroleMgmt.page_download_devOper_vstudio_list()
        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_vstudio_list)[0] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_vstudio_list)[1] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_vstudio_list)[2] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_vstudio_list)[3] == '部署审批'
        except Exception as e:
            self.logger.error("未找到部署审批菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_vstudio_main_1()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_vstudio_main_2()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_vstudio_main_3()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_vstudio_main_4()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)
        except Exception as e:
            self.logger.error("打开的部署审批页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

    @pytest.fixture()
    def user_download_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_datacollector)
        self.logger.info("数据下载用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("数据下载用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        self.user_download_logout()

    def user_download_logout(self):
        element = self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_download_1)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        self.role_pagelogin.page_logout()
        GetDriver.quit_web_driver()

    # 步骤二：登录数采应用平台：验证数据下载测试组菜单权限是否正常
    @pytest.mark.run('second')
    @pytest.mark.usefixtures("user_download_login")
    def test_user_role_judge_datacollector(self):
        self.logger.info("创建的用户登录数采应用平台：数据下载测试组菜单权限是否正常")
        self.user_download_judge_datacollector()

    def user_download_judge_datacollector(self):
        self.role_pageroleMgmt.page_download_devOper_datacollector_list()
        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[0] == '全量下载'
        except Exception as e:
            self.logger.error("未找到全量下载菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[1] == '数采下载'
        except Exception as e:
            self.logger.error("未找到数采下载菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[2] == '事件下载'
        except Exception as e:
            self.logger.error("未找到事件下载菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[3] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[4] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        try:
            assert self.role_pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)[5] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_1()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Full_download_main)
        except Exception as e:
            self.logger.error("打开的全量下载页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_2()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Data_download_main)
        except Exception as e:
            self.logger.error("打开的数采下载页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_3()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Event_download_main)
        except Exception as e:
            self.logger.error("打开的事件下载页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_4()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_5()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

        self.role_pageroleMgmt.page_download_devOper_datacollector_main_6()
        try:
            assert self.role_pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.role_pageroleMgmt.insert_image()
            raise

    # 删除分组download
    @pytest.fixture()
    def deleted_download_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.username, self.email, self.password, self.surname, self.name = GetYaml(
            "user_Mgmt.yaml").get_normaluserMgmt()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.pageadminMgmt.page_moveto_background()
        yield
        self.deleted_download_logout()
        GetDriver.quit_web_driver()

    def deleted_download_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    # 步骤四：删除数据下载测试组
    @pytest.mark.run('fourth')
    @pytest.mark.usefixtures("deleted_download_login")
    def test_delete_group_download(self):
        self.pageadminMgmt.page_moveto_groupMgmt()
        self.logger.info("搜索用户")
        groupname = GetYaml("user_Mgmt.yaml").find_downloader_groupMgmt()
        self.pageadminMgmt.search_group(groupname)
        self.logger.info("点击删除按钮")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_deletegroup_btn)
        self.logger.info("删除用户组是否给出警告")
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_deletegroup_warning)
        except Exception as e:
            self.logger.error("删除用户组未给出警告")
            self.pageadminMgmt.insert_image()

        self.logger.info("删除用户组是否显示影响元素")
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_deletegroup_impact)
        except Exception as e:
            self.logger.error("删除用户组未显示影响元素")
            self.pageadminMgmt.insert_image()
        self.logger.info("点击确定按钮")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_deletegroup_confirm_btn)

    # 获取被删除用户组的用户信息
    @pytest.fixture()
    def download_deleted_role_login(self):
        self.logger.info("role登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_datacollector)
        self.logger.info("被删除的数据下载用户信息")
        self.role_user, self.role_pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.logger.info("被删除的数据下载用户登录")
        self.role_pagelogin = PageLogin(self.driver)
        self.role_pageroleMgmt = PageRoleMgmt(self.driver)
        self.role_pagelogin.page_login(self.role_user, self.role_pwd)
        yield
        GetDriver.quit_web_driver()

    # 步骤五：用户登录数采应用平台：验证是否提示无权限
    @pytest.mark.run('fifth')
    @pytest.mark.usefixtures("download_deleted_role_login")
    def test_user_role_judge_datacollector_second(self):
        self.logger.info("创建的用户登录数采应用平台：验证是否提示无权限")
        sleep(5)
        element1 = self.driver.execute_script("return document.getElementsByClassName('Toastify__toast-body toast-error-body').length")
        print(element1)
        element2 = self.driver.execute_script("return document.getElementsByClassName('Toastify__close-button')")
        print(element2)

    # admin删除用户、删除devOper
    @pytest.fixture()
    def admin_delete_devOper(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.username, self.email, self.password, self.surname, self.name = GetYaml(
            "user_Mgmt.yaml").get_normaluserMgmt()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.pageadminMgmt.page_moveto_background()
        yield
        self.admin_delete_devOper_logout()
        GetDriver.quit_web_driver()

    def admin_delete_devOper_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    # 步骤六：删除用户、删除devOper分组后退出
    @pytest.mark.run('last')
    @pytest.mark.usefixtures("admin_delete_devOper")
    def test_delete_user_group_devOper(self):
        self.delete_user_group_devOper()

    def delete_user_group_devOper(self):
        username = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.page_moveto_userMgmt()
        self.pageadminMgmt.delete_user(username)
        self.pageadminMgmt.page_moveto_groupMgmt()
        groupname = GetYaml("user_Mgmt.yaml").find_operator_groupMgmt()
        self.pageadminMgmt.delete_group(groupname)
