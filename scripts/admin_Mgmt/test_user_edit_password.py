import logging
import re
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import page.Login
from page import admin_Mgmt
from page.Login.page_login import PageLogin
from page.admin_Mgmt.page_admin_Mgmt import PageAdminMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestUserEditPassMgmt:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)

    def teardown_class(self):
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,email,password,surname,name", [(GetYaml("user_Mgmt.yaml").get_normaluserMgmt())])
    def test_user_edit_password(self,username,email,password,surname,name):
        self.logger.info("进入后台管理页面")
        self.pageadminMgmt.page_moveto_background()
        self.logger.info("返回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("搜索用户")
        adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
        self.pageadminMgmt.search_user(adduser)
        self.logger.info("返回第一行用户信息")
        self.pageadminMgmt.page_get_username()
        if self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_firstuser_ID).strip() == "暂无数据":
            self.add_user(username, email, password, surname, name)
        else:
            self.logger.info("用户已存在")
        self.user_edit_password()

    def add_user(self, username, email, password, surname, name):
        self.logger.info("回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.logger.info("清空搜索")
        self.pageadminMgmt.empty_search_user()
        self.logger.info("取用户的数量")
        fFirst = self.pageadminMgmt.page_get_user_count()
        fcFirst = fFirst.split(sep=' ')[2]
        self.logger.info("创建前:{}".format(fcFirst))
        reg = r"(\d+)"
        pre = re.search(reg, fcFirst).group(1)
        self.logger.info("新建用户")
        self.pageadminMgmt.page_create_user_before()
        self.pageadminMgmt.page_create_user_input(username, email, password, surname, name)
        self.pageadminMgmt.page_create_user_confirm()
        sleep(3)
        fEnd = self.pageadminMgmt.page_get_user_count()
        fcEnd = fEnd.split(sep=' ')[2]
        self.logger.info("创建后:{}".format(fcEnd))
        post = re.search(reg, fcEnd).group(1)
        try:
            assert int(pre) + 1 == int(post)
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.pageadminMgmt.insert_image()
            self.logger.info("判断窗口是否还在，如果存在，click 取消，避免影响其他的测试用例")
            if self.pageadminMgmt.is_element_present(page.admin_Mgmt.adminMgmt_adduser_cancel):
                self.logger.info("窗口还在,click 取消")
                self.pageadminMgmt.element_click(page.admin_Mgmt.adminMgmt_adduser_cancel)
            raise

    def user_edit_password(self):
        self.logger.info("点击更多按钮")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_more_btn)
        self.logger.info("点击重置密码")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_password_btn)
        try:
            adduser = GetYaml("user_Mgmt.yaml").find_userMgmt()
            assert adduser in self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_userinfo_confirm)
        except Exception as e:
            self.logger.error("用户信息不存在")
        self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_newpass_input,"test456")
        self.pageadminMgmt.element_click(admin_Mgmt.adminMgmt_confirm_btn)
