import logging
import re
from time import sleep

import pytest

import page.Login
from page import role_Mgmt, admin_Mgmt
from page.Login.page_login import PageLogin
from page.admin_Mgmt.page_admin_Mgmt import PageAdminMgmt
from page.role_Mgmt.page_role_Mgmt import PageRoleMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestRoleAdminMgmt:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.logger.info("admin登录地址")
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.logger.info("admin用户信息")
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.logger.info("admin用户登录")
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    def test_admin_backgroud_role(self):
        self.pageadminMgmt.page_admin_backgroud_list()
        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[0] == '主页'
        except Exception as e:
            self.logger.error("未找到主页菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[1] == '用户管理'
        except Exception as e:
            self.logger.error("未找到用户管理菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[2] == '用户组'
        except Exception as e:
            self.logger.error("未找到用户组菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[3] == '车辆分组'
        except Exception as e:
            self.logger.error("未找到车辆分组菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[4] == '车辆查询'
        except Exception as e:
            self.logger.error("未找到车辆查询菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[5] == '信号矩阵管理'
        except Exception as e:
            self.logger.error("未找到信号矩阵管理菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[6] == '用户参数配置'
        except Exception as e:
            self.logger.error("未找到用户参数配置菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_backgroup_list)[7] == '授权书管理'
        except Exception as e:
            self.logger.error("未找到授权书管理菜单")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_1()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_user_number)
        except Exception as e:
            self.logger.error("打开的主页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_2()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_user_manage)
        except Exception as e:
            self.logger.error("打开的用户管理页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_3()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_group_manage)
        except Exception as e:
            self.logger.error("打开的用户组页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_4()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_vehicle_manage)
        except Exception as e:
            self.logger.error("打开的车辆分组页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_5()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_vehicle_search)
        except Exception as e:
            self.logger.error("打开的车辆查询页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_6()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_signal_search)
        except Exception as e:
            self.logger.error("打开的信号矩阵页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_7()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_parameter_config)
        except Exception as e:
            self.logger.error("打开的用户参数配置页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_backgroup_main_8()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_authorization)
        except Exception as e:
            self.logger.error("打开的授权数管理页面不正确")
            self.pageadminMgmt.insert_image()
            raise

    def test_admin_application_role(self):
        self.pageadminMgmt.page_admin_application_list()
        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[0] == '主页'
        except Exception as e:
            self.logger.error("未找到主页菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[1] == '工作空间'
        except Exception as e:
            self.logger.error("未找到工作空间菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[2] == '最近改动'
        except Exception as e:
            self.logger.error("未找到最近改动菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[3] == '最近执行'
        except Exception as e:
            self.logger.error("未找到最近执行菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[4] == '收藏夹'
        except Exception as e:
            self.logger.error("未找到收藏夹菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[5] == '文件管理'
        except Exception as e:
            self.logger.error("未找到文件管理菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[6] == '部署历史'
        except Exception as e:
            self.logger.error("未找到部署历史菜单")
            self.pageadminMgmt.insert_image()
            raise

        try:
            assert self.pageadminMgmt.elements_get_text(admin_Mgmt.adminshow_application_list)[7] == '参数配置'
        except Exception as e:
            self.logger.error("未找到参数配置菜单")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_1()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_hello)
        except Exception as e:
            self.logger.error("打开的主页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_2()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_workspace)
        except Exception as e:
            self.logger.error("打开的工作空间页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_3()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_Recent_changes)
        except Exception as e:
            self.logger.error("打开的最近改动页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_4()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_Recent_perform)
        except Exception as e:
            self.logger.error("打开的最近执行页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_5()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_favorites)
        except Exception as e:
            self.logger.error("打开的收藏夹页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_6()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_File_management)
        except Exception as e:
            self.logger.error("打开的文件管理页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_7()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_deployment_history)
        except Exception as e:
            self.logger.error("打开的部署历史页面不正确")
            self.pageadminMgmt.insert_image()
            raise

        self.pageadminMgmt.page_adminshow_application_main_8()
        try:
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminshow_Parameter_configuration)
        except Exception as e:
            self.logger.error("打开的参数配置页面不正确")
            self.pageadminMgmt.insert_image()
            raise
