# _*_coding: utf-8_*_

from time import sleep

from page import Login
from page.page_base import PageBase
import logging


class PageLogin(PageBase):
    logger = logging.getLogger(__name__)

    def page_get_showname(self):
        return self.element_get_text(Login.usershow_ID).strip()

    def page_get_hello(self):
        return self.element_get_text(Login.hello_ID).strip()

    def page_get_login_title(self):
        return self.element_get_text(Login.login_pagetitle).strip()

    def page_get_invalid_loginInfo(self):
        return self.element_get_text(Login.invalid_userpwd).strip()

    # about Login business to integration
    def page_login(self, username, password):
        self.logger.info("登录vStudio，账号'用户名为：{}、密码为：{}'".format(username, password))
        self.element_input(Login.username_ID, username)
        self.element_input(Login.password_ID, password)
        self.element_click(Login.login_btn)

    def page_logout(self):
        self.logger.info("退出登录")
        self.element_click(Login.usershow_ID)
        sleep(3)
        self.element_click(Login.logout_ID)
        # checking login button
    def page_admin_logout(self):
        self.logger.info("admin退出登录")
        self.element_click(Login.adminshow_ID)
        sleep(3)
        self.element_click(Login.admin_logout_ID)

    def page_get_recent_task(self, update_text, exec_text, deploy_text):
        update_bool = self.element_get_text(Login.recent_update_text).strip() == update_text
        exec_bool = self.element_get_text(Login.recent_exec_text).strip() == exec_text
        deploy_bool = self.element_get_text(Login.recent_deploy_text).strip() == deploy_text
        return deploy_bool and update_bool and exec_bool
