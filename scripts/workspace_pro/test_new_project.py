# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: new_project
# @author: kyle
# @date: 2022/1/6 12:27
import logging

import page
from page import workspace_pro, workspace
from page.Login.page_login import PageLogin
from page.workspace_pro import pro_yaml
from page.workspace_pro.page_project import PageProject
from page.workspace_pro.pro_yaml import ProYaml
from utils.driver_utils import GetDriver


class TestNewProject:
    logger = logging.getLogger()

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.workspace_pro.url_index)
        self.user, self.pwd = pro_yaml.ProYaml("workspace_pro.yaml").get_LoginInfo()
        PageLogin(GetDriver.get_web_driver(page.Login.url_vstudio)).page_login(self.user, self.pwd)
        self.pagePro = PageProject(self.driver)
        self.spaceName = pro_yaml.ProYaml("workspace_pro.yaml").get_space_name()
        self.projectName = pro_yaml.ProYaml("workspace_pro.yaml").get_new_project()
        self.projectSpaceName = pro_yaml.ProYaml("workspace_pro.yaml").get_new_project()
        self.projectSpecialName = pro_yaml.ProYaml("workspace_pro.yaml").get_new_project()

    def teardown_class(self):
        self.logger.info("关闭浏览器")
        GetDriver.quit_web_driver()

    def test_check_new_project(self):
        # Check the list
        self.driver.refresh()
        self.pagePro.page_workspace_base(self.spaceName)
        self.driver.refresh()
        try:
            assert self.pagePro.page_project_index(self.spaceName) == "工程名称"
        except Exception as e:
            self.logger.error("断言出错，错误信息为：{}".format(e))
            raise

        # check the alert
        self.driver.refresh()
        self.pagePro.element_click(workspace_pro.new_project_btn)
        self.pagePro.element_click(workspace_pro.new_project_pro)
        ale = self.driver.element_find(workspace_pro.new_project_search).text
        try:
            notable = self.pagePro.is_enable(workspace_pro.new_project_sure)
            self.driver.element_input(workspace_pro.new_project_name, "Test")
            isable = self.pagePro.is_enable(workspace_pro.new_project_sure)
            assert ale == "新建"
            assert notable is False
            self.logger.info("确认按钮为不可点击状态")
            assert isable is True
            self.logger.info("输入空间名称后确认按钮为可点击状态")
        except Exception as e:
            self.logger.error("断言出错，错误信息为：{}".format(e))
            raise

    def test_new_project(self):
        self.pagePro.element_click(workspace.workspace_btn)
        self.pagePro.page_project_index(self.spaceName)
        self.driver.refresh()
        self.pagePro.page_project_new(self.projectName)
        try:
            self.pagePro.element_input(workspace_pro.project_search, self.projectName)
            assert self.pagePro.element_get_text(workspace_pro.project_search_name) == self.projectName
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagePro.insert_image()
            self.logger.info("工程创建未成功")
            raise

    def test_new_project_space(self):
        self.pagePro.element_click(workspace.workspace_btn)
        self.pagePro.page_project_index(self.spaceName)
        self.driver.refresh()
        self.pagePro.page_project_new(self.projectSpaceName)
        try:
            self.pagePro.element_input(workspace_pro.project_search, self.projectSpaceName)
            assert self.pagePro.element_get_text(workspace_pro.project_search_space) == "暂无数据"
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagePro.insert_image()
            self.logger.info("工程创建未成功, 输入字符不合法")
            raise

    def test_new_project_special(self):
        self.pagePro.element_click(workspace.workspace_btn)
        self.pagePro.page_project_index(self.spaceName)
        self.driver.refresh()
        self.pagePro.page_project_new(self.projectSpecialName)
        try:
            self.pagePro.element_input(workspace_pro.project_search, self.projectSpecialName)
            assert self.pagePro.element_get_text(workspace_pro.project_search_space) == "暂无数据"
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagePro.insert_image()
            self.logger.info("工作空间创建未成功, 输入字符不合法")
            raise
