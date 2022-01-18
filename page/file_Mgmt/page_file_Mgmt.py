import logging
from page.page_base import PageBase
from pywinauto.keyboard import send_keys
from pywinauto import Desktop
from time import sleep

from page import file_Mgmt


class PageFileMgmt(PageBase):
    logger = logging.getLogger(__name__)

    def page_get_count(self):
        return self.element_get_text(file_Mgmt.fileMgmt_file_count)

    def page_moveto_fileMgmt(self):
        self.element_click(file_Mgmt.fileMgmt_management_btn)

    def page_createdir(self, filename):
        self.element_click(file_Mgmt.fileMgmt_makedir)
        self.logger.info("在输入文件目录名前检查确定按钮是否可点击")
        assert not self.is_enable(file_Mgmt.fileMgmt_mkdir_confirm)
        self.logger.info("输入文件目录名")
        self.element_input(file_Mgmt.fileMgmt_dirname, filename)
        sleep(2)
        self.element_click(file_Mgmt.fileMgmt_mkdir_confirm)

    # des: Used as a selection function for uploading files
    def page_file_choose(self, path, filename):
        self.logger.info("选择文件")
        app = Desktop()
        win = app["打开"]
        # win.print_ctrl_ids()
        win["Toolbar3"].click()
        # send_keys(filenamePat)
        send_keys(path)
        send_keys("{VK_RETURN}")
        win["文件名(&N):Edit"].type_keys(filename)
        # win["打开(&O)"].click()
        send_keys("{VK_RETURN}")
        sleep(2)

    def page_file_upload_click(self):
        self.element_click(file_Mgmt.fileMgmt_upload_btn)

    def page_file_upload_prompt(self):
        return self.element_get_text(file_Mgmt.fileMgmt_upload_prompt).strip()

    def page_file_upload_choose(self, path, filename):
        self.element_click(file_Mgmt.fileMgmt_upload_choose_btn)
        self.page_file_choose(path, filename)
        self.element_click(file_Mgmt.fileMgmt_upload_confirm)

    def page_get_filename(self):
        return self.element_get_text(file_Mgmt.fileMgmt_firstline_ID).strip()
