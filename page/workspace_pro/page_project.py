# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: page_project
# @author: kyle
# @date: 2022/1/6 12:28
import logging

from pywinauto.keyboard import send_keys

from page import workspace, workspace_pro
from page.page_base import PageBase


class PageProject(PageBase):
    logger = logging.getLogger(__name__)

    def page_workspace_base(self, spaceName, check_existed=True):
        """
        创建基础工作空间
        :return: 
        """
        self.element_click(workspace.workspace_btn)
        self.logger.info("点击功能栏工作空间按钮")
        # if check_existed and self.page_workspace_search(spaceName, True):
        #     self.page_workspace_del(spaceName)
        self.element_click(workspace.index_btn)
        self.element_click(workspace.workspace_btn)
        self.logger.info("点击新建")
        self.element_click(workspace.new_workspace_btn)
        self.logger.info("输入新建工作空间名称")
        self.element_input(workspace.new_workspace_name, spaceName)
        self.logger.info("点击确认按钮，完成新建操作")
        self.element_click(workspace.new_workspace_sure)
        self.element_click(workspace.workspace_btn)
    
    def page_workspace_search(self, spaceName, full_match=False):
        """
        查是否有，查出来的第一条是否包换spaceName，有返回 True,没有返回False
        """
        self.element_input(workspace.search_box, spaceName)
        send_keys("{VK_RETURN}")
        if self.is_element_present(workspace.search_res):
            if full_match:
                return spaceName == self.element_get_text(workspace.search_res).strip()
            else:
                return spaceName in self.element_get_text(workspace.search_res).strip()
        else:
            return False
        
    def page_workspace_del(self, spaceName):
        self.logger.info("点击功能栏工作空间按钮")
        self.element_click(workspace.workspace_btn)
        if self.page_workspace_search(spaceName, True):
            self.element_click(workspace.del_workspace_btn)
            self.element_click(workspace.del_workspace_sure)
        else:
            self.logger.info("没找到工作空间 {}".format(spaceName))

    def page_project_index(self, spaceName):
        """
        页面置于baseSpace基础工作空间工程页面
        :return:
        """
        self.element_input(workspace_pro.space_search, spaceName)
        self.element_click(workspace_pro.space_base)
        self.driver.refresh()
        return self.element_get_text(workspace_pro.project_list)

    def page_project_refresh(self):
        self.driver.refresh()

    def page_project_new(self, projectName):
        """
        新建工程
        :return:
        """
        self.element_click(workspace_pro.new_project_btn)
        self.element_click(workspace_pro.new_project_pro)
        self.element_input(workspace_pro.input_project, projectName)
        self.element_click(workspace_pro.new_project_sure)
        self.driver.back()



    def page_project_search(self):
        '''
        检索工程
        :return:
        '''
        pass
