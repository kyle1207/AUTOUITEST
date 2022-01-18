# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_im_workspace
# @author: kyle
# @date: 2021/12/30 13:48
import logging
import os
from time import sleep

import pytest

import page.Login
from config import BASE_PATH
from page import workspace

from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestImWorkSpace:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        # self.pagewsp = PageWorkSpace(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("path,filename", [GetYaml("new_workspace.yaml").get_im_space()])
    def test_im_workspace(self, path, filename):
        staticdir = "testdata"
        self.logger.info("回到工作空间主页")
        self.pagewsp.element_click(workspace.workspace_btn)
        self.logger.info("进行文件上传")
        path = os.path.join(BASE_PATH, staticdir)
        self.pagewsp.page_workspace_im(path, filename)
        try:
            self.pagewsp.element_click(workspace.workspace_btn)
            self.pagewsp.element_input(workspace.search_box, filename.split(".json")[0])
            assert self.pagewsp.element_get_text(workspace.im_space) == filename.split(".json")[0]
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pagewsp.insert_image()
            raise



    @pytest.mark.parametrize("path,filename", [GetYaml("new_workspace.yaml").get_im_upname()])
    def test_im_repeat(self, path, filename):
        staticdir = "testdata"
        self.logger.info("回到工作空间主页")
        self.pagewsp.element_click(workspace.workspace_btn)
        self.logger.info("进行修改文件名称后的上传")
        path = os.path.join(BASE_PATH, staticdir)
        self.pagewsp.page_workspace_im(path, filename)
        try:
            self.pagewsp.element_click(workspace.workspace_btn)
            self.pagewsp.element_input(workspace.search_box, filename.split(".json")[0])
            assert self.pagewsp.element_get_text(workspace.imsencond) == "暂无数据"
            self.pagewsp.element_click(workspace.workspace_btn)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pagewsp.insert_image()
            raise

    @pytest.mark.parametrize("path,filename", [GetYaml("new_workspace.yaml").get_im_updes()])
    def test_im_upname(self, path, filename):
        staticdir = "testdata"
        self.logger.info("回到工作空间主页")
        self.pagewsp.element_click(workspace.workspace_btn)
        self.logger.info("上传修改文件名称后的文件")
        path = os.path.join(BASE_PATH, staticdir)
        self.pagewsp.page_workspace_im(path, filename)
        try:
            self.pagewsp.element_click(workspace.workspace_btn)
            self.pagewsp.element_input(workspace.search_box, filename.split(".json")[0])
            assert self.pagewsp.element_get_text(workspace.im_space) == filename.split(".json")[0]
            self.pagewsp.element_click(workspace.workspace_btn)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pagewsp.insert_image()
            raise
