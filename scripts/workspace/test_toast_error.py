# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_toast_error
# @author: kyle
# @date: 2021/12/30 13:52
import logging
import re

import page.Login
from page import workspace

from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestToastError:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        # self.pagewsp = PageWorkSpace(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin = PageLogin(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.spacename, self.spacenamefir, self.spacenamesen, self.spacename_chinese = GetYaml("new_workspace.yaml").get_wkspace_Info()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_toast_name_repeat_error(self):
        '''
        校验total.error
        '''
        self.pagewsp.element_click(workspace.workspace_btn)
        fir = self.pagewsp.page_workspace_count()

        self.pagewsp.page_workspace_mk(self.spacename, False)

        keep = self.pagewsp.element_find(workspace.new_workspace_search).text
        self.pagewsp.element_click(workspace.workspace_btn)
        end = self.pagewsp.page_workspace_count()
        try:
            """名称重复错误提示框没法catch，所以判断新建窗口还在"""
            assert keep == "新建"
            self.logger.info("新建不成功，名称重复")
            reg = r"共(\d+)条"
            assert int(re.search(reg, fir).group(1))  == int(re.search(reg, end).group(1))
        except Exception as e:
            self.logger.error("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            raise
        GetDriver.quit_web_driver()
