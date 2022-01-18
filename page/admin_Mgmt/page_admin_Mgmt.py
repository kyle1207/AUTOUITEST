import logging
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page import admin_Mgmt
from page.page_base import PageBase


class PageAdminMgmt(PageBase):
    logger = logging.getLogger(__name__)

    def page_logout(self):
        self.logger.info("退出登录")
        self.element_click(admin_Mgmt.usershow_btn)
        sleep(3)
        self.element_click(admin_Mgmt.logout_ID)
        # checking login button
    def page_admin_logout(self):
        self.logger.info("admin退出登录")
        self.element_click(admin_Mgmt.adminshow_btn)
        sleep(3)
        self.element_click(admin_Mgmt.admin_logout_ID)

    def page_moveto_background(self):
        self.logger.info("点击右上角的用户信息")
        self.element_click(admin_Mgmt.adminMgmt_userinfo_btn)
        self.logger.info("点击右上角的后台管理")
        self.element_click(admin_Mgmt.adminMgmt_background_btn)

    def page_moveto_groupMgmt(self):
        self.logger.info("点击导航菜单用户组")
        sleep(3)
        self.element_click(admin_Mgmt.adminMgmt_groupmanagement_btn)

    def page_get_group_count(self):
        self.logger.info("页面底部的共几个用户组")
        return self.element_get_text(admin_Mgmt.adminMgmt_group_count)

    def page_get_groupname(self):
        self.logger.info("返回第一行用户组信息")
        return self.element_get_text(admin_Mgmt.adminMgmt_firstgroup_ID)

    def page_get_group_userlist(self):
        self.logger.info("点击向下箭头")
        self.element_click(admin_Mgmt.adminMgmt_userlist_btn)
        self.logger.info("返回包含的用户列表")
        info = self.elements_find(admin_Mgmt.adminMgmt_userlist)
        num = []
        for i in info:
            info = print(i.text)
            print("---------")
            num.append(i)
        return num

    def page_edit_group_role(self, rolename):
        self.logger.info("编辑用户组的角色")
        self.logger.info("点击导航菜单用户组")
        sleep(3)
        self.element_click(admin_Mgmt.adminMgmt_groupmanagement_btn)
        if len(self.elements_find(admin_Mgmt.adminMgmt_group_list)) > 0:
            self.logger.info("找到首行用户组")
            self.element_find(admin_Mgmt.adminMgmt_firstgroup_ID)
            self.logger.info("点击编辑用户组")
            self.element_click(admin_Mgmt.adminMgmt_group_edit_btn)
            self.logger.info("用户组编辑前所选的角色")
            brole = self.element_get_text(admin_Mgmt.adminMgmt_role_edited)
            self.logger.info("编辑前的用户组")
            bgroup = self.element_get_text(admin_Mgmt.adminMgmt_groupname_edited)
            self.logger.info("确认编辑前的角色")
            confirmrole = self.element_get_text(admin_Mgmt.adminMgmt_edit_role_confirm)
            self.logger.info("选择角色'角色为：{}'".format(rolename))
            self.page_select_rolename(rolename)
            self.logger.info("点击确定按钮")
            self.element_click(admin_Mgmt.adminMgmt_addgroup_confirm)

    def page_create_User_group(self, groupname, rolename):
        self.logger.info("创建用户组'用户组名为：{},角色：{}'".format(groupname, rolename))
        self.logger.info("点击新建用户组")
        self.element_click(admin_Mgmt.adminMgmt_addgroup)
        self.logger.info("输入用户组名")
        self.element_input(admin_Mgmt.adminMgmt_groupname, groupname)
        if (rolename != 'default'):
            self.page_select_rolename(rolename)
        self.logger.info("点击确定按钮")
        self.element_click(admin_Mgmt.adminMgmt_addgroup_confirm)

    def search_group(self, groupname):
        self.logger.info("查找用户组'用户组名为：{}'".format(groupname))
        self.element_input(admin_Mgmt.adminMgmt_searchgroup, groupname)
        return self.element_get_text(admin_Mgmt.adminMgmt_findgroupname)

    def delete_group(self,groupname):
        self.logger.info("搜索用户")
        self.search_group(groupname)
        self.logger.info("点击删除按钮")
        self.element_click(admin_Mgmt.adminMgmt_deletegroup_btn)
        self.logger.info("点击确定按钮")
        self.element_click(admin_Mgmt.adminMgmt_deletegroup_confirm_btn)

    def empty_search_group(self):
        self.logger.info("清空搜索'")
        self.element_click(admin_Mgmt.adminMgmt_cleargroup)

    def page_moveto_userMgmt(self):
        self.logger.info("点击导航菜单用户管理")
        sleep(3)
        self.element_click(admin_Mgmt.adminMgmt_usermanagement_btn)

    def page_get_user_count(self):
        self.logger.info("页面底部共几个用户")
        return self.element_get_text(admin_Mgmt.adminMgmt_user_count)

    def page_get_username(self):
        self.logger.info("返回第一行用户信息")
        return self.element_get_text(admin_Mgmt.adminMgmt_firstuser_ID).strip()

    def page_get_first_username(self):
        self.logger.info("返回第一行用户信息-用户名")
        return self.element_get_text(admin_Mgmt.adminMgmt_firstuser_name).strip()

    def page_create_user_before(self):
        self.logger.info("点击新建用户")
        self.element_click(admin_Mgmt.adminMgmt_adduser_btn)
        self.logger.info("显示新建用户标题")
        self.element_get_text(admin_Mgmt.adminMgmt_adduserpage_open)
        self.logger.info("显示用户名标签")
        self.element_get_text(admin_Mgmt.adminMgmt_username)
        self.logger.info("显示用户名不为空")
        self.element_get_text(admin_Mgmt.adminMgmt_username_notempty)
        self.logger.info("显示预设密码标签")
        self.element_get_text(admin_Mgmt.adminMgmt_password)
        self.logger.info("显示预设密码不为空")
        self.element_get_text(admin_Mgmt.adminMgmt_password_noteempty)
        self.logger.info("显示姓标签")
        self.element_get_text(admin_Mgmt.adminMgmt_surname)
        self.logger.info("显示姓不为空")
        self.element_get_text(admin_Mgmt.adminMgmt_surname_notempty)
        self.logger.info("显示名标签")
        self.element_get_text(admin_Mgmt.adminMgmt_name)
        self.logger.info("显示名不为空")
        self.element_get_text(admin_Mgmt.adminMgmt_name_notempty)

    def page_create_user_input(self, username, email, password, surname, name):
        self.logger.info(
            "输入用户信息'用户名为：{}、电子邮件为：{}、预设密码为：{}、姓为：{}、名为：{}'".format(username, email, password, surname, name))
        self.logger.info("输入用户名")
        self.element_input(admin_Mgmt.adminMgmt_username_input, username)
        self.logger.info("输入电子邮件")
        self.element_input(admin_Mgmt.adminMgmt_email_input, email)
        self.logger.info("输入预设密码")
        self.element_input(admin_Mgmt.adminMgmt_password_input, password)
        self.logger.info("输入姓")
        self.element_input(admin_Mgmt.adminMgmt_surname_input, surname)
        self.logger.info("输入名")
        self.element_input(admin_Mgmt.adminMgmt_name_input, name)


    def page_create_user_confirm(self):
        self.logger.info("显示确定按钮")
        self.element_find(admin_Mgmt.adminMgmt_adduser_confirm)
        self.logger.info("点击确定按钮")
        self.element_click(admin_Mgmt.adminMgmt_adduser_confirm)

    def page_create_user_cancel(self):
        self.logger.info("点击取消按钮")
        self.send_key(admin_Mgmt.adminMgmt_adduser_cancel)

    def search_user(self, username):
        self.logger.info("查找用户'用户名为：{}'".format(username))
        self.element_input(admin_Mgmt.adminMgmt_searchuser, username)

    def delete_user(self,username):
        self.search_user(username)
        self.logger.info("点击删除按钮")
        self.element_click(admin_Mgmt.adminMgmt_deleteuser_btn)
        self.logger.info("点击确定按钮")
        self.element_click(admin_Mgmt.adminMgmt_deleteuser_confirm)

    def empty_search_user(self):
        self.logger.info("清空搜索")
        self.element_click(admin_Mgmt.adminMgmt_clearuser)

    def page_list_username(self):
        pass

    def page_list_group(self):
        self.element_click(admin_Mgmt.adminMgmt_group_contains_user_btn)


    def edit_user_group(self, username):
        pass

    def search_userrole(self, groupname):
        self.logger.info("输入搜素的用户角色'角色名为：{}'".format(groupname))

    def page_get_user_grouplist(self):
        self.logger.info("找到已选择的用户组")
        info = self.elements_find(admin_Mgmt.adminMgmt_usergroup_list)
        num = []
        for i in info:
            print("-----------------------")
            print(i.text)
            print("***********************")
            num.append(i.text)
        print("+++++++++++++++++++++++++++")
        print(num)
        print(len(num))
        print("+++++++++++++++++++++++++++")

    def user_role(self, adduser, groupNames):
        self.logger.info("选择用户分组'用户名为：{},用户组名:{}'".format(adduser, groupNames))
        self.element_click(admin_Mgmt.adminMgmt_selectuser)
        self.logger.info("点击更多按钮")
        self.element_click(admin_Mgmt.adminMgmt_more_btn)
        self.logger.info("点击用户分组按钮")
        self.element_click(admin_Mgmt.adminMgmt_usergroup_btn)
        self.logger.info("对用户进行分组")
        self.page_select_usergroups(groupNames)
        self.logger.info("点击确定按钮")
        self.element_click(admin_Mgmt.adminMgmt_group_select_confirm)

    def page_select_usergroups(self, usergroups):
        """
        usergroup: group list ["a","b","c"]
        """
        self.logger.info("选择用户组名：{}".format(usergroups))
        number = 2
        while True:
            usergroup_checkbox_xpath = (By.XPATH, admin_Mgmt.usergroup_select_basepath
                                        + str(number) + admin_Mgmt.usergroup_checkbox_left)
            usergroup_text_xpath = (By.XPATH, admin_Mgmt.usergroup_select_basepath
                                    + str(number) + admin_Mgmt.usergroup_text_left)
            if not self.is_element_present(usergroup_text_xpath):
                break

            group_text = self.element_get_text(usergroup_text_xpath)
            for usergroup in usergroups:
                usergroup_full = usergroup
                if len(group_text) > 6:
                    group_text = group_text[0:6]
                if len(usergroup) > 6:
                    usergroup = usergroup[0:6]
                if group_text == usergroup:
                    element = self.element_find(usergroup_text_xpath)
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).perform()
                    sleep(2)
                    self.logger.info("勾选 " + usergroup_full)
                    self.element_click(usergroup_checkbox_xpath)
            number = number + 1

    def page_select_rolename(self, rolename):
        self.logger.info("找到选项选择的dropdown list")
        self.element_click(admin_Mgmt.adminMgmt_selectrole_dropdown)
        if rolename == '普通用户':
            self.element_click(admin_Mgmt.adminMgmt_selectrole_normal)
        elif rolename == '开发运营人员':
            self.element_click(admin_Mgmt.adminMgmt_selectrole_dev_operator)
        elif rolename == '数采运营人员':
            self.element_click(admin_Mgmt.adminMgmt_selectrole_acquisition_operator)
        elif rolename == '数据下载人员':
            self.element_click(admin_Mgmt.adminMgmt_selectrole_download)
        sleep(2)

    # admin后台管理菜单
    def page_admin_backgroud_list(self):
        self.logger.info("点击右上角的用户信息")
        self.element_click(admin_Mgmt.adminMgmt_userinfo_btn)
        self.logger.info("点击右上角后台管理")
        self.element_click(admin_Mgmt.adminMgmt_background_btn)
        self.logger.info("查找admin后台管理菜单组")
        self.elements_find(admin_Mgmt.adminshow_backgroup_list)
        return self.elements_get_text(admin_Mgmt.adminshow_backgroup_list)

    # admin后台管理菜单点击
    def page_adminshow_backgroup_main_1(self):
        self.logger.info("点击主页管理")
        self.element_click(admin_Mgmt.adminshow_backgroup_1)
        self.logger.info("返回主页")
        self.element_find(admin_Mgmt.adminshow_user_number)

    def page_adminshow_backgroup_main_2(self):
        self.logger.info("点击用户管理菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_2)
        self.logger.info("返回用户管理页面")
        self.element_find(admin_Mgmt.adminshow_user_manage)

    def page_adminshow_backgroup_main_3(self):
        self.logger.info("点击用户组菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_3)
        self.logger.info("返回用户组页面")
        self.element_find(admin_Mgmt.adminshow_group_manage)

    def page_adminshow_backgroup_main_4(self):
        self.logger.info("点击车辆分组菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_4)
        self.logger.info("返回车辆分组页面")
        self.element_find(admin_Mgmt.adminshow_vehicle_manage)

    def page_adminshow_backgroup_main_5(self):
        self.logger.info("点击车辆查询菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_5)
        self.logger.info("返回车辆查询页面")
        self.element_find(admin_Mgmt.adminshow_vehicle_search)

    def page_adminshow_backgroup_main_6(self):
        self.logger.info("点击信号矩阵管理菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_6)
        self.logger.info("返回信号矩阵管理页面")
        self.element_find(admin_Mgmt.adminshow_signal_search)

    def page_adminshow_backgroup_main_7(self):
        self.logger.info("点击用户参数配置菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_7)
        self.logger.info("返回用户参数配置页面")
        self.element_find(admin_Mgmt.adminshow_parameter_config)

    def page_adminshow_backgroup_main_8(self):
        self.logger.info("点击授权书管理菜单")
        self.element_click(admin_Mgmt.adminshow_backgroup_8)
        self.logger.info("返回授权书管理页面")
        self.element_find(admin_Mgmt.adminshow_authorization)

    # admin前台应用菜单
    def page_admin_application_list(self):
        self.logger.info("点击右上角的用户信息")
        self.element_click(admin_Mgmt.adminMgmt_userinfo_btn)
        self.logger.info("点击右上角前台应用")
        self.element_click(admin_Mgmt.adminMgmt_application_btn)
        self.logger.info("查找admin前台应用菜单组")
        self.elements_find(admin_Mgmt.adminshow_application_list)
        return self.elements_get_text(admin_Mgmt.adminshow_application_list)

    # admin前台应用菜单点击
    def page_adminshow_application_main_1(self):
        self.logger.info("点击主页")
        self.element_click(admin_Mgmt.adminshow_application_1)
        self.logger.info("返回主页")
        self.element_find(admin_Mgmt.adminshow_hello)

    def page_adminshow_application_main_2(self):
        self.logger.info("点击工作空间菜单")
        self.element_click(admin_Mgmt.adminshow_application_2)
        self.logger.info("返回工作空间页面")
        self.element_find(admin_Mgmt.adminshow_workspace)

    def page_adminshow_application_main_3(self):
        self.logger.info("点击最近改动菜单")
        self.element_click(admin_Mgmt.adminshow_application_3)
        self.logger.info("返回最近改动页面")
        self.element_find(admin_Mgmt.adminshow_Recent_changes)

    def page_adminshow_application_main_4(self):
        self.logger.info("点击最近执行菜单")
        self.element_click(admin_Mgmt.adminshow_application_4)
        self.logger.info("返回最近执行页面")
        self.element_find(admin_Mgmt.adminshow_Recent_perform)

    def page_adminshow_application_main_5(self):
        self.logger.info("点击收藏夹菜单")
        self.element_click(admin_Mgmt.adminshow_application_5)
        self.logger.info("返回收藏夹页面")
        self.element_find(admin_Mgmt.adminshow_favorites)

    def page_adminshow_application_main_6(self):
        self.logger.info("点击文件管理菜单")
        self.element_click(admin_Mgmt.adminshow_application_6)
        self.logger.info("返回文件管理页面")
        self.element_find(admin_Mgmt.adminshow_File_management)

    def page_adminshow_application_main_7(self):
        self.logger.info("点击部署历史菜单")
        self.element_click(admin_Mgmt.adminshow_application_7)
        self.logger.info("返回部署历史页面")
        self.element_find(admin_Mgmt.adminshow_deployment_history)

    def page_adminshow_application_main_8(self):
        self.logger.info("点击参数配置菜单")
        self.element_click(admin_Mgmt.adminshow_application_8)
        self.logger.info("返回参数配置页面")
        self.element_find(admin_Mgmt.adminshow_Parameter_configuration)