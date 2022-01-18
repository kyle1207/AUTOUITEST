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

    def test_download_role(self):
        self.pageroleMgmt.page_download_list()
        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_list)[0] == '全量下载'
        except Exception as e:
            self.logger.error("未找到全量下载菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_list)[1] == '数采下载'
        except Exception as e:
            self.logger.error("未找到数采下载菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_list)[2] == '事件下载'
        except Exception as e:
            self.logger.error("未找到事件下载菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_list)[3] == '信号查询'
        except Exception as e:
            self.logger.error("未找到信号查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_download_list)[4] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_download_main_1()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Full_download_main)
        except Exception as e:
            self.logger.error("打开的全量下载页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_download_main_2()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Data_download_main)
        except Exception as e:
            self.logger.error("打开的数采下载页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_download_main_3()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Event_download_main)
        except Exception as e:
            self.logger.error("打开的事件下载页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_download_main_4()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
        except Exception as e:
            self.logger.error("打开的信号查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_download_main_5()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise









