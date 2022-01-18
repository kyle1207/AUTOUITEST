# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: test_vs_file_make
# @author: kyle
# @date: 2021/12/3 12:40

import logging
import pytest
import page.Login
import page.file_Mgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml
from page.file_Mgmt.page_file_Mgmt import PageFileMgmt
from page.Login.page_login import PageLogin
from time import sleep
import re
from config import BASE_PATH
import os


class FilemkdirTest:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageMgmt = PageFileMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        sleep(2)
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("filename", [(GetYaml("file_Mgmt.yaml").get_fileMgmt_DirSelect())])
    def test_createdir(self, filename):
        self.logger.info("回到文件管理主页")
        self.pageMgmt.page_moveto_fileMgmt()
        self.logger.info("取文件的数量")
        fcFirst = self.pageMgmt.page_get_count()
        self.logger.info("创建前:{}".format(fcFirst))
        reg = r"(\d+)"
        pre = re.search(reg, fcFirst).group(1)
        self.logger.info("新建文件夹")
        self.pageMgmt.page_createdir(filename)
        sleep(3)
        fcEnd = self.pageMgmt.page_get_count()
        self.logger.info("创建后:{}".format(fcEnd))
        post = re.search(reg, fcEnd).group(1)
        try:
            assert int(pre) + 1 == int(post)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pageMgmt.insert_image()
            raise
