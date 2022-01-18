# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_list_workspace
# @author: kyle
# @date: 2021/12/30 13:40
import logging

import page
from page import workspace
from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestListWorkspace:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        # self.pagewsp = PageWorkSpace(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin = PageLogin(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        # self.spacename, self.spacenamefir, self.spacenamesen = GetYaml("new_workspace.yaml").get_wkspace_Info()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_list_workspace(self):
        self.pagewsp.page_workspace_list()
        tables = self.pagewsp.element_find(workspace.workspace_list)
        rows = tables.find_elements_by_tag_name("tr")
        res = self.pagewsp.page_workspace_count()
        if int(res[7]) == 1:
            assert len(rows) == int(res[-2])
        else:
            assert (int(res[7]) - 1) * 10 + int(res[-2]) == len(rows)
