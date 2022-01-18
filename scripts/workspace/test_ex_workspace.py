# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_ex_workspace
# @author: kyle
# @date: 2021/12/30 13:47
import logging
import page.Login
from page import workspace

from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestExWorkSpace:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))

    def teardown_class(self):
        GetDriver.quit_web_driver()


    def test_ex_workspace(self):
        self.logger.info("点击工作空间主页")
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.page_workspace_mk("testExport")
        self.pagewsp.page_workspace_search("testExport")
        self.pagewsp.element_click(workspace.ex_workspace)
