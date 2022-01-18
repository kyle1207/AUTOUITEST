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
        self.driver = GetDriver.get_web_driver(page.Login.url_datacollector)
        self.user, self.pwd = GetYaml(self.driver).get_role_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageroleMgmt = PageRoleMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        sleep(2)
        GetDriver.quit_web_driver()

    def test_ac_role(self):
        self.pageroleMgmt.page_ac_list()
        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_ac_list)[0] == '灵活采集'
        except Exception as e:
            self.logger.error("未找到灵活采集菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_ac_list)[1] == '事件采集'
        except Exception as e:
            self.logger.error("未找到事件采集菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_ac_list)[2] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_ac_list)[3] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_ac_list)[4] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_ac_main_1()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Flexible_acquisition_main)
        except Exception as e:
            self.logger.error("打开的灵活采集页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_ac_main_2()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Event_collection_main)
        except Exception as e:
            self.logger.error("打开的事件采集页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_ac_main_3()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_ac_main_4()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_ac_main_5()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise








