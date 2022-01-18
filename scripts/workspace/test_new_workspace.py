# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_new_workspace
# @author: kyle
# @date: 2021/12/27 16:20
import logging
import re
from time import sleep
import page.Login

from page import workspace
from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestNewWorkSpace:
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
        self.logger.info("关闭浏览器")
        GetDriver.quit_web_driver()

    def test_new_workspace(self):
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.element_click(workspace.new_workspace_btn)
        ale = self.pagewsp.element_find(workspace.new_workspace_search).text
        try:
            # 校验新建workspace弹框
            notable = self.pagewsp.is_enable(workspace.new_workspace_sure)
            self.pagewsp.element_input(workspace.new_workspace_name, "Test")
            isable = self.pagewsp.is_enable(workspace.new_workspace_sure)
            assert ale == "新建"
            assert notable is False
            self.logger.info("确认按钮为不可点击状态")
            assert isable is True
            self.logger.info("输入空间名称后确认按钮为可点击状态")
        except Exception as e:
            self.logger.error("断言出错，错误信息为：{}".format(e))
            raise

        # 校验新建
        # self.pagewsp.element_click(workspace.workspace_btn)
        # self.pagewsp.page_workspace_mk("Test")
        # self.pagewsp.element_input(workspace.new_workspace_name, "Test")
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        F = self.pagewsp.page_workspace_count()
        self.pagewsp.page_workspace_mk(self.spacename)
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        E = self.pagewsp.page_workspace_count()
        try:
            reg = r"共(\d+)条"
            assert int(re.search(reg, F).group(1)) + 1 == int(re.search(reg, E).group(1))
            self.logger.info("工作空间新建成功")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间未创建成功")
            raise

    def test_new_workspace_chinese(self):
        # 中文
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        F_china = self.pagewsp.page_workspace_count()
        self.pagewsp.page_workspace_mk(self.spacename_chinese)
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        E_china = self.pagewsp.page_workspace_count()
        try:
            reg = r"共(\d+)条"
            assert int(re.search(reg, F_china).group(1)) + 1 == int(re.search(reg, E_china).group(1))
            self.logger.info("工作空间新建成功")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间未创建成功")
            raise

    def test_new_workspace_special(self):
        # 特殊字符
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        fir = self.pagewsp.page_workspace_count()
        self.pagewsp.page_workspace_mk(self.spacenamefir)
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        end = self.pagewsp.page_workspace_count()
        try:
            reg = r"共(\d+)条"
            assert int(re.search(reg, fir).group(1)) + 1 == int(re.search(reg, end).group(1))
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间未创建成功")
            raise

    def test_new_workspace_exceed_30(self):
        # 长度超过30字符
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        self.pagewsp.page_workspace_mk(self.spacenamesen)
        sleep(3)
        keep = self.pagewsp.element_find(workspace.new_workspace_search).text
        try:
            assert keep == "新建"
            self.logger.info("新建不成功，长度超出字符")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间名称超过30字符，创建不成功")
            raise

    def test_del_workspace(self):
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        sleep(2)
        del_F = self.pagewsp.page_workspace_count()
        filename = "Test"
        self.pagewsp.page_workspace_del(filename)
        self.pagewsp.element_click(workspace.index_btn)
        self.pagewsp.element_click(workspace.workspace_btn)
        del_E = self.pagewsp.page_workspace_count()
        self.pagewsp.element_input(workspace.search_box, "Test")
        del_search = self.pagewsp.element_get_text(workspace.del_workspace_search)
        try:
            reg = r"共(\d+)条"
            assert int(re.search(reg, del_F).group(1)) - 1 == int(re.search(reg, del_E).group(1))
            self.logger.info("空间列表数据变化，删除成功")
            assert del_search == "暂无数据"
            self.logger.info("删除的空间名称未找到，删除成功")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间未删除成功")

            raise

