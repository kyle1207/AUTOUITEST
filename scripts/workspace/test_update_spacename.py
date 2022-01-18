# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_update_spacename
# @author: kyle
# @date: 2021/12/30 18:00
import logging
from time import sleep

from selenium.webdriver import ActionChains

import page
from page import workspace
from page.Login.page_login import PageLogin
from page.workspace.page_workspace import PageWorkSpace
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestUpdateSpaceName:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pagewsp = PageWorkSpace(GetDriver.get_web_driver(page.Login.url_index))
        self.pagelogin.page_login(self.user, self.pwd)
        self.spacename = GetYaml("new_workspace.yaml").get_workspace_list()['spacename']
        self.up_name = 'testupdatename'

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_update_spacename(self):
        self.logger.info("修改工作空间名字")
        self.update_spacename(self.spacename, self.up_name)

    def test_restore_spacename(self):
        self.logger.info("恢复修改工作空间名字")
        self.update_spacename(self.up_name, self.spacename)
        GetDriver.quit_web_driver()

    def update_spacename(self, pre_name, udpate_name):
        self.pagewsp.element_click(workspace.workspace_btn)
        assert self.pagewsp.page_workspace_search(pre_name, True)
        self.logger.info("鼠标挪到第一行")
        element = self.pagewsp.element_find(workspace.search_res)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        self.logger.info("修改工作空间名")
        self.pagewsp.element_click(workspace.update_icon)
        self.pagewsp.element_input(workspace.spaceupdate, udpate_name)
        self.pagewsp.element_click(workspace.sucess_icon)
        self.pagewsp.element_click(workspace.workspace_btn)
        assert self.pagewsp.page_workspace_search(udpate_name, True)
        self.logger.info("查找工作空间：{}".format(pre_name))
        self.pagewsp.element_input(workspace.search_box, pre_name)
        del_search = self.pagewsp.element_get_text(workspace.del_workspace_search)
        try:
            assert del_search == "暂无数据"
            self.logger.info("更改空间名称后列表中未找到，更改成功")
        except Exception as e:
            self.logger.info("断言出错，错误信息为：{}".format(e))
            self.pagewsp.insert_image()
            self.logger.info("工作空间未改名成功")
            raise


