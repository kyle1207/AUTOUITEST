# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: page_workspace
# @author: kyle
# @date: 2021/12/27 14:08
import logging

from pywinauto import Desktop
from pywinauto.keyboard import send_keys

from page.page_base import PageBase
from page import workspace


class PageWorkSpace(PageBase):
    logger = logging.getLogger(__name__)

    def __init__(self, driver):
        super().__init__(driver)
        self.PageFileMgmt = None

    def page_workspace_mk(self, spacename, check_existed=True):
        self.logger.info("点击功能栏工作空间按钮")
        self.element_click(workspace.workspace_btn)
        # if check_existed and self.page_workspace_search(spacename, True):
        #     self.page_workspace_del(spacename)
        # self.element_click(workspace.index_btn)
        # self.element_click(workspace.workspace_btn)
        self.logger.info("点击新建")
        self.element_click(workspace.new_workspace_btn)
        self.logger.info("输入新建工作空间名称")
        self.element_input(workspace.new_workspace_name, spacename)
        self.logger.info("点击确认按钮，完成新建操作")
        self.element_click(workspace.new_workspace_sure)
        self.logger.info("判断创建窗口是否还在，如果存在就是错误")
        # if check_existed:
        #     assert not self.is_element_present(workspace.new_workspace_sure)

    """这么做不对，需要传入工作空间名，search 工作空间，然后点击第一行的删除button"""

    def page_workspace_del(self, spacename):
        self.logger.info("点击功能栏工作空间按钮")
        """需要加search,定位到第一行"""
        self.element_click(workspace.workspace_btn)
        if self.page_workspace_search(spacename, True):
            self.element_click(workspace.del_workspace_btn)
            self.element_click(workspace.del_workspace_sure)
        else:
            self.logger.info("没找到工作空间 {}".format(spacename))

    def page_workspace_search(self, spacename, fullmatch=False):
        """查是否有，查出来的第一条是否包换spacename，有返回 True,没有返回False"""
        # self.element_click(workspace.search_box)
        self.element_input(workspace.search_box, spacename)
        send_keys("{VK_RETURN}")
        if (self.is_element_present(workspace.search_res)):
            if fullmatch:
                return spacename == self.element_get_text(workspace.search_res).strip()
            else:
                return spacename in self.element_get_text(workspace.search_res).strip()
        else:
            return False

    def page_workspace_im(self, path, filename):
        self.element_click(workspace.workspace_btn)
        self.element_click(workspace.im_workspace)
        app = Desktop()
        win = app["打开"]
        win["Toolbar3"].click()
        send_keys(path)
        send_keys("{VK_RETURN}")
        win["文件名(&N):Edit"].type_keys(filename)
        send_keys("{VK_RETURN}")

    def page_workspace_ex(self):
        self.element_click(workspace.workspace_btn)
        self.element_click(workspace.ex_workspace)

    def page_workspace_count(self):
        return self.element_get_text(workspace.space_count)

    def page_workspace_list(self):
        self.element_click(workspace.workspace_btn)

    def page_file_upload_prompt(self):
        return self.element_get_text(workspace.fileMgmt_upload_prompt).strip()

    def page_file_upload_choose(self, path, filename):
        self.element_click(workspace.file_upload_choose_btn)
        self.page_workspace_im(path, filename)
        self.element_click(workspace.file_upload_confirm)

    def page_get_filename(self):
        return self.element_get_text(workspace.file_firstline_ID).strip()
