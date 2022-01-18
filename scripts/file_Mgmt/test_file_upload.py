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


class FileUploadTest:
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

    @pytest.mark.parametrize("path,filename", [GetYaml("file_Mgmt.yaml").getUploadInfo()])
    def test_file_upload(self, path, filename):
        self.logger.info("回到文件管理主页")
        self.pageMgmt.page_moveto_fileMgmt()
        self.logger.info("进行文件上传")
        self.pageMgmt.page_file_upload_click()
        path = BASE_PATH + os.sep + path
        try:
            self.logger.info('验证文件名格式提示')
            assert(self.pageMgmt.page_file_upload_prompt() == '包含中文或中文符号的信号名，数据预览的显示将存在乱码，这不会影响数据使用。使用数据时，请在输入“数据读入连接器”按照信号命名规则重新定义！')
            self.pageMgmt.page_file_upload_choose(path, filename)
            self.logger.info("新上传的文件名称为:{}".format(filename))
            self.logger.info("取第一条的文件名")
            first_fileName = self.pageMgmt.page_get_filename()
            self.logger.info("第一条的文件名为:{}".format(first_fileName))
            assert first_fileName == filename
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pageMgmt.insert_image()
            """
             self.logger.info("判断窗口是否还在，如果存在，click 取消，避免影响其他的测试用例")
            if self.pageMgmt.is_element_present(page.file_Mgmt.fileMgmt_upload_cancel):
                self.logger.info("窗口还在,click 取消")
                self.pageMgmt.element_click(page.file_Mgmt.fileMgmt_upload_cancel)
            """
            raise
