# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_fuzzy_workspace
# @author: kyle
# @date: 2021/12/30 15:16
import logging
from time import sleep

import page.Login
from page import workspace

from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestFuzzyWorkSpace:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        # self.pagewsp = PageWorkSpace(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin = PageLogin(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_create_workspace(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        self.logger.info("创建验证查询需要的工作空间，包括名字包含中文")
        self.pagewsp.page_workspace_mk(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename1"])
        self.pagewsp.page_workspace_mk(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename2"])
        self.pagewsp.page_workspace_mk(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename3"])

    def test_fuzzy_workspace(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        fuzzy_one = GetYaml("new_workspace.yaml").get_fuzzy_list()["fuzzy_one"]
        self.logger.info("查找普通模糊匹配: {}".format(fuzzy_one))
        assert self.pagewsp.page_workspace_search(fuzzy_one)
        self.logger.info("查看table")
        tables = self.pagewsp.element_find(workspace.workspace_fuzzy)
        """减去表头"""
        rows = len(tables.find_elements_by_tag_name("tr")) - 1
        assert rows == 1

    def test_fuzzy_special_workspace(self):
        fuzzy_special = GetYaml("new_workspace.yaml").get_fuzzy_list()["fuzzy_special"]
        self.logger.info("查找特殊字符匹配：{},查询暂无数据".format(fuzzy_special))
        assert not self.pagewsp.page_workspace_search(fuzzy_special)
        del_search = self.pagewsp.element_get_text(workspace.del_workspace_search)
        assert del_search == "暂无数据"

    def test_fuzzy_chinese_workspace(self):
        fuzzy_chinese = GetYaml("new_workspace.yaml").get_fuzzy_list()["fuzzy_chinese"]
        self.logger.info("查找中文字符匹配：{}".format(fuzzy_chinese))
        assert self.pagewsp.page_workspace_search(fuzzy_chinese)
        tables = self.pagewsp.element_find(workspace.workspace_fuzzy)
        rows = len(tables.find_elements_by_tag_name("tr")) - 1
        assert rows == 1

    def test_fuzzy_notfound_workspace(self):
        fuzzy_no = GetYaml("new_workspace.yaml").get_fuzzy_list()["fuzzy_no"]
        self.logger.info("查找字符匹配：{},查询暂无数据".format(fuzzy_no))
        assert not self.pagewsp.page_workspace_search(fuzzy_no)
        del_search = self.pagewsp.element_get_text(workspace.del_workspace_search)
        assert del_search == "暂无数据"

    def test_del_workspace(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.page_workspace_del(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename1"])
        self.pagewsp.page_workspace_del(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename2"])
        self.pagewsp.page_workspace_del(GetYaml("new_workspace.yaml").get_fuzzy_list()["spacename3"])