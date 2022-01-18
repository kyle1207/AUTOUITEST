# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_workspace_ele
# @author: kyle
# @date: 2021/12/30 13:43
import logging
import re

import page.Login

from page import workspace
from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestWorkSpaceEle:
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

    def test_workspace_ele(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        assert self.pagewsp.element_find(workspace.spacename).text == "空间名称"
        self.logger.info("空间名称-元素校验完成")
        assert self.pagewsp.element_find(workspace.spacedes).text == "描述"
        self.logger.info("描述-元素校验完成")
        assert self.pagewsp.element_find(workspace.spaceauth).text == "所有者"
        self.logger.info("所有者-元素校验完成")
        assert self.pagewsp.element_find(workspace.spaceacreat).text == "创建时间"
        self.logger.info("创建时间-元素校验完成")
        assert self.pagewsp.element_find(workspace.spaceend).text == "更新时间"
        self.logger.info("更新时间-元素校验完成")
        self.pagewsp.element_click(workspace.workspace_btn)
        ele_E = self.pagewsp.page_workspace_count()
        try:
            reg = r"共(\d+)条"
            assert int(re.search(reg, ele_E).group(1)) != 0
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            raise