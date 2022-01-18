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

    def test_devoper_role(self):
        self.pageroleMgmt.page_devOper_list()
        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_devOper_list)[0] == '资源监控'
        except Exception as e:
            self.logger.error("未找到资源监控菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_devOper_list)[1] == '版本查询'
        except Exception as e:
            self.logger.error("未找到版本查询菜单")
            self.pageroleMgmt.insert_image()
            raise

        try:
            assert self.pageroleMgmt.elements_get_text(role_Mgmt.roleMgmt_devOper_list)[2] == '部署审批'
        except Exception as e:
            self.logger.error("未找到部署审批菜单")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_devOper_main_1()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
        except Exception as e:
            self.logger.error("打开的资源监控页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_devOper_main_2()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
        except Exception as e:
            self.logger.error("打开的版本查询页面不正确")
            self.pageroleMgmt.insert_image()
            raise

        self.pageroleMgmt.page_devOper_main_3()
        try:
            assert self.pageroleMgmt.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)
        except Exception as e:
            self.logger.error("打开的部署审批页面不正确")
            self.pageroleMgmt.insert_image()
            raise










