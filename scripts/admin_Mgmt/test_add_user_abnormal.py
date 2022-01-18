import logging
from time import sleep

import pytest
from selenium.webdriver import ActionChains, Keys

import page.Login
from page import admin_Mgmt
from page.Login.page_login import PageLogin
from page.admin_Mgmt.page_admin_Mgmt import PageAdminMgmt
from utils.driver_utils import GetDriver
from utils.yaml_utils import GetYaml


class TestAddUserAbnormalMgmt:
    logger = logging.getLogger(__name__)

    @pytest.fixture()
    def admin_login(self):
        self.driver = GetDriver.get_web_driver(page.Login.url_vstudio)
        self.user, self.pwd = GetYaml(self.driver).get_admin_LoginInfo()
        self.pagelogin = PageLogin(self.driver)
        self.pageadminMgmt = PageAdminMgmt(self.driver)
        self.pagelogin.page_login(self.user, self.pwd)
        self.pageadminMgmt.page_moveto_background()
        yield
        self.admin_logout()
        GetDriver.quit_web_driver()

    def admin_logout(self):
        self.logger.info("退出admin")
        sleep(2)
        self.pagelogin.page_admin_logout()
        GetDriver.quit_web_driver()


    @pytest.mark.parametrize("username,email,password,surname,name", [(GetYaml("user_Mgmt.yaml").get_normaluserMgmt())])
    @pytest.mark.usefixtures("admin_login")
    def test_add_user_abnormal(self, username, email, password, surname, name):
        self.logger.info("回到用户管理主页面")
        self.pageadminMgmt.page_moveto_userMgmt()
        self.pageadminMgmt.page_create_user_before()
        try:
            self.logger.info("是否显示新建用户标题")
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_adduserpage_open) == "新建用户"
        except Exception as e:
            self.logger.error("未显示新建用户标题")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否显示用户名标签")
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_username) == "用户名"
        except Exception as e:
            self.logger.error("未显示用户名标签")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否已标识用户名不为空")
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_username_notempty)
        except Exception as e:
            self.logger.error("未标识用户名不为空")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否显示预设密码标签")
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_password) == "预设密码"
        except Exception as e:
            self.logger.error("未显示预设密码标签")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否已标识预设密码不为空")
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_password_noteempty)
        except Exception as e:
            self.logger.error("未标识预设密码不为空")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否显示姓标签")
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_surname) == "姓"
        except Exception as e:
            self.logger.error("未显示姓标签")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否已标识姓不为空")
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_surname_notempty)
        except Exception as e:
            self.logger.error("未标识姓不为空")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否显示名标签")
            assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_name) == "名"
        except Exception as e:
            self.logger.error("未显示名标签")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("是否已标识名不为空")
            assert self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_name_notempty)
        except Exception as e:
            self.logger.error("未标识名不为空")
            self.pageadminMgmt.insert_image()
            raise
        try:
            self.logger.info("未输入用户信息前确定按钮不可点击")
            assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
        except Exception as e:
            self.logger.error("未输入用户信息时，确定按钮应该不可点击")
            self.pageadminMgmt.insert_image()
            raise
        # 异常输入
        self.logger.info("获取异常用户信息")
        for i in range(30):
            userinfo = GetYaml("user_Mgmt.yaml").get_abuserinfo_Mgmt()
            username = userinfo[i]['username']
            self.logger.info("输入用户名")
            self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_username_input,username)
            email = userinfo[i]['email']
            self.logger.info("输入电子邮件")
            self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_email_input,email)
            password = userinfo[i]['password']
            self.logger.info("输入预设密码")
            self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_password_input,password)
            surname = userinfo[i]['surname']
            self.logger.info("输入姓")
            self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_surname_input,surname)
            name = userinfo[i]['name']
            self.logger.info("输入名")
            self.pageadminMgmt.element_input(admin_Mgmt.adminMgmt_name_input,name)
            try:
                self.logger.info("输入用户信息后，确定按钮可点击")
                assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
            except Exception as e:
                self.logger.error("输入用户信息后，确定按钮应该可点击")
                self.pageadminMgmt.insert_image()
                raise
            self.logger.info("输入用户信息后点击确定按钮")
            self.pageadminMgmt.page_create_user_confirm()
            try:
                self.logger.info("判断是否会提示用户名异常")
                assert "只允许输入中文、数字、字母及中、下划线" in self.pageadminMgmt.element_get_text(
                    admin_Mgmt.adminMgmt_adduser_abnormal)
            except Exception as e:
                self.logger.error("用户名异常未给出提示")
                self.pageadminMgmt.insert_image()
                raise

            sleep(1)
            self.logger.info("清空用户名文本输入框信息")
            ele = self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_username_input)
            action = ActionChains(self.driver)
            action.click(ele).perform()
            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(username)):
                action.send_keys(Keys.BACKSPACE).perform()
            try:
                self.logger.info("用户名输入框信息被清除")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_username_input) == ""
            except Exception as e:
                self.logger.error("用户名信息未成功清除")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("是否提示必填项")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_username_mandatory) == "必填项"
            except Exception as e:
                self.logger.error("不填写用户名未提示必填项")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("用户名被清空后，确定按钮是否可点击")
                assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
            except Exception as e:
                self.logger.error("清空用户名，确定按钮不可点击")
                self.pageadminMgmt.insert_image()

            sleep(1)
            self.logger.info("清空电子邮件文本输入框信息")
            ele = self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_email_input)
            action = ActionChains(self.driver)
            action.click(ele).perform()

            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(email)):
                action.send_keys(Keys.BACKSPACE).perform()

            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(email)):
                action.send_keys(Keys.BACKSPACE).perform()

            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(email)):
                action.send_keys(Keys.BACKSPACE).perform()

            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(email)):
                action.send_keys(Keys.BACKSPACE).perform()
            try:
                self.logger.info("电子邮件输入框信息被清除")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_email_input) == ""
            except Exception as e:
                self.logger.error("电子邮件信息未成功清除")
                self.pageadminMgmt.insert_image()

            sleep(1)
            self.logger.info("清空预设密码文本输入框信息")
            ele = self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_password_input)
            action = ActionChains(self.driver)
            action.click(ele).perform()
            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(password)):
                action.send_keys(Keys.BACKSPACE).perform()
            try:
                self.logger.info("预设密码输入框信息被清除")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_password_input) == ""
            except Exception as e:
                self.logger.error("预设密码信息未成功清除")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("是否提示必填项")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_password_mandatory) == "必填项"
            except Exception as e:
                self.logger.error("不填写预设密码未提示必填项")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("预设密码被清空后，确定按钮是否可点击")
                assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
            except Exception as e:
                self.logger.error("清空预设密码，确定按钮不可点击")
                self.pageadminMgmt.insert_image()

            sleep(1)
            self.logger.info("清空姓文本输入框信息")
            ele = self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_surname_input)
            action = ActionChains(self.driver)
            action.click(ele).perform()
            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(surname)):
                action.send_keys(Keys.BACKSPACE).perform()
            try:
                self.logger.info("姓输入框信息被清除")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_surname_input) == ""
            except Exception as e:
                self.logger.error("姓信息未成功清除")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("是否提示必填项")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_surname_mandatory) == "必填项"
            except Exception as e:
                self.logger.error("不填写姓未提示必填项")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("姓被清空后，确定按钮是否可点击")
                assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
            except Exception as e:
                self.logger.error("清空姓，确定按钮不可点击")
                self.pageadminMgmt.insert_image()

            sleep(1)
            self.logger.info("清空名文本输入框信息")
            ele = self.pageadminMgmt.element_find(admin_Mgmt.adminMgmt_name_input)
            action = ActionChains(self.driver)
            action.click(ele).perform()
            action.send_keys(Keys.RIGHT).perform()
            for i in range(len(name)):
                action.send_keys(Keys.BACKSPACE).perform()
            try:
                self.logger.info("名输入框信息被清除")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_name_input) == ""
            except Exception as e:
                self.logger.error("名信息未成功清除")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("是否提示必填项")
                assert self.pageadminMgmt.element_get_text(admin_Mgmt.adminMgmt_name_mandatory) == "必填项"
            except Exception as e:
                self.logger.error("不填写名未提示必填项")
                self.pageadminMgmt.insert_image()
            try:
                self.logger.info("名被清空后，确定按钮是否可点击")
                assert self.pageadminMgmt.is_enable(admin_Mgmt.adminMgmt_adduser_confirm) == True
            except Exception as e:
                self.logger.error("清空名，确定按钮不可点击")
                self.pageadminMgmt.insert_image()


