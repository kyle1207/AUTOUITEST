import logging
import re
from time import sleep

import pytest

import page.Login
from page import role_Mgmt
from page.Login.page_login import PageLogin
from page.role_Mgmt.page_role_Mgmt import PageRoleMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestRoleDevMgmt:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageroleMgmt = PageRoleMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        sleep(2)
        GetDriver.quit_web_driver()

    def test_dev_devOper_role(self):
        self.pageroleMgmt.page_dev_devOper_list()
        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[0] == '主页'
        except Exception as e:
            self.logger.error("未找到主页菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[1] == '工作空间'
        except Exception as e:
            self.logger.error("未找到工作空间菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[2] == '最近改动'
        except Exception as e:
            self.logger.error("未找到最近改动菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[3] == '最近执行'
        except Exception as e:
            self.logger.error("未找到最近执行菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[4] == '收藏夹'
        except Exception as e:
            self.logger.error("未找到收藏夹菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[5] == '文件管理'
        except Exception as e:
            self.logger.error("未找到文件管理菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[6] == '部署历史'
        except Exception as e:
            self.logger.error("未找到部署历史菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[7] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[8] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[9] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[10] == '部署审批'
        except Exception as e:
            self.logger.error("未找到部署审批菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[11] == '参数配置'
        except Exception as e:
            self.logger.error("未找到参数配置菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_dev_list)[12] == '事件历史'
        except Exception as e:
            self.logger.error("未找到事件历史菜单")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_1()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_main)
        except Exception as e:
            self.logger.error("打开的主页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_2()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_workspace_main)
        except Exception as e:
            self.logger.error("打开的工作空间页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_3()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_changes_main)
        except Exception as e:
            self.logger.error("打开的最近改动页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_4()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Recent_perform_main)
        except Exception as e:
            self.logger.error("打开的最近执行页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_5()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_favorites_main)
        except Exception as e:
            self.logger.error("打开的收藏夹页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_6()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_File_management_main)
        except Exception as e:
            self.logger.error("打开的文件管理页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_7()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_history_main)
        except Exception as e:
            self.logger.error("打开的部署历史页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_8()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_9()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_10()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_11()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)
        except Exception as e:
            self.logger.error("打开的部署审批页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_12()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Parameter_configuration_main)
        except Exception as e:
            self.logger.error("打开的参数配置页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_dev_devOper_main_13()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Events_history_main)
        except Exception as e:
            self.logger.error("打开的事件历史页面不正确")
            self.pageroleMgmt.insert_image()
            raise

