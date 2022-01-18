# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_workspace_enshrine
# @author: kyle
# @date: 2021/12/30 16:15
import logging
import re

import page.Login
from page import workspace

from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestWorkSpaceEnshrine:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        # self.pagewsp = PageWorkSpace(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin = PageLogin(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.spacename, self.spacenamefir, self.spacenamesen, self.pacename_chinese = GetYaml("new_workspace.yaml").get_wkspace_Info()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_workspace_enshrine(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.page_workspace_mk("Base")
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.page_workspace_search("Base")
        self.pagewsp.element_click(workspace.enshrine_space)
        self.pagewsp.element_click(workspace.enshrine_btn)
        self.pagewsp.element_input(workspace.enshring_search, "Base")
        try:
            assert self.pagewsp.element_get_text(workspace.enshrine_list) == "Base"
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("收藏夹未找到收藏的内容")
            raise
        self.pagewsp.element_click(workspace.enshrine_btn)
        self.pagewsp.element_input(workspace.enshring_search, "Base")
        self.pagewsp.element_click(workspace.enshrine_not)
        self.pagewsp.element_click(workspace.enshrine_btn)
        self.pagewsp.element_input(workspace.enshring_search, "Base")
        try:
            assert self.pagewsp.element_get_text(workspace.enshrine_list) == "暂无数据"
            self.logger.info("取消收藏")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("收藏夹未找到收藏的内容,已取消收藏")
            raise

    def test_del_all(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        reg = r"共(\d+)条"
        count = int(re.search(reg, self.pagewsp.page_workspace_count()).group(1))
        while count >= 1:
            self.pagewsp.element_click(workspace.workspace_btn)
            self.pagewsp.element_click(workspace.del_all)
            self.pagewsp.element_click(workspace.del_workspace_sure)
            self.pagewsp.element_click(workspace.workspace_btn)
            count -= 1

