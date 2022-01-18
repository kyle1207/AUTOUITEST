# _*_coding: utf-8_*_

import logging
from time import sleep

import page.Login
from page.Login.page_login import PageLogin
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class LoginTest:
    logger = logging.getLogger(__name__)

    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.login_page = PageLogin(self.driver)
        self.user, self.pwd = GetYaml(self.driver).get_dev_LoginInfo()
        self.invalid_user, self.invalid_pwd = GetYaml(self.driver).get_invalid_userInfo()

    def test_login_invalid_pwd(self):
        self.logger.info("验证错误密码登录")
        self.login_page.page_login(self.user, self.pwd + '$$')
        try:
            assert self.login_page.page_get_invalid_loginInfo() == 'Invalid username or password.'
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.login_page.insert_image()
            raise
        sleep(3)

    def test_login_invalid_user(self):
        self.logger.info("验证错误用户名登录")
        self.login_page.page_login(self.invalid_user, self.invalid_pwd)
        try:
            assert self.login_page.page_get_invalid_loginInfo() == 'Invalid username or password.'
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.login_page.insert_image()
            raise
        sleep(3)

    def test_dev_login(self):
        self.logger.info("有效用户名密码的开发用户登录")
        self.login_page.page_login(self.user, self.pwd)
        try:
            self.logger.info("验证显示在页面右上角的用户名")
            assert self.login_page.page_get_showname() == self.user
            assert self.login_page.page_get_hello() == 'Hello ' + self.user
            self.logger.info("验证主页显示")
            self.dev_mainPage_checking()
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.login_page.insert_image()
            raise

    def test_admin_login(self):
        self.logger.info("admin用户登录")
        self.login_page.page_login(self.user, self.pwd)
        try:
            self.logger.info("验证显示在页面右上角的用户名")
            assert self.login_page.page_get_showname() == self.user
            assert self.login_page.page_get_hello() == 'Hello ' + self.user
            self.logger.info("验证主页显示")
            self.dev_mainPage_checking()
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.login_page.insert_image()
            raise

    def dev_mainPage_checking(self):
        self.login_page.moveto_main_page()
        self.logger.info("验证主页显示 最近改动，最近执行，部署历史")
        assert self.login_page.page_get_recent_task('最近改动', '最近执行', '部署历史')
        self.logger.info("验证最近改动link")
        self.login_page.element_click(page.Login.recent_update_check_all)
        assert self.login_page.element_get_text(page.Login.recent_update_page_title).strip() == '最近改动'
        self.logger.info("验证最近经执行link")
        self.login_page.moveto_main_page()
        self.login_page.element_click(page.Login.recent_exec_check_all)
        assert self.login_page.element_get_text(page.Login.recent_exec_page_title).strip() == '最近执行'
        self.logger.info("验证部署历史link")
        self.login_page.moveto_main_page()
        self.login_page.element_click(page.Login.recent_deploy_check_all)
        assert self.login_page.element_get_text(page.Login.recent_deploy_page_title).strip() == '部署历史'

    def test_logout(self):
        self.logger.info("退出登录")
        self.login_page.page_logout()
        self.logger.info("验证退出后的页面,title 应该是 'Log in' ")
        try:
            assert self.login_page.page_get_login_title() == 'Log In'
        except Exception as e:
            self.logger.error("断言出错，错误信息：{}".format(e))
            self.login_page.insert_image()
            raise
        sleep(3)

    def teardown_class(self):
        self.logger.info("关闭浏览器")
        GetDriver.quit_web_driver()

