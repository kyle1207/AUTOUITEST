# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: base
# @author: kyle
# @date: 2021/10/9 13:30
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import page
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from config import BASE_PATH
from time import sleep

from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchWindowException,
    TimeoutException, ElementClickInterceptedException,
)




class PageBase:
    logger = logging.getLogger(__name__)

    # initialize driver

    def __init__(self, driver):
        self.logger.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # Encapsulated find function
    def element_find(self, loc, timeout=30, poll=0.3):
        """
        :param loc: 元素（数据结构为列表或者元组）
        :param timeout: 超时时间，默认30
        :param poll: 步频，默认0.5
        :return: 元素
        """
        self.logger.info("正在查找元素：{}".format(loc))
        try:
            '''
            return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))
            '''
            WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except (NoSuchElementException, TimeoutException):
            self.logger.error(
                "{0} can't be found in the page {1} element".format(self, loc)
            )
            # save the screenshot
            self.insert_image()
            raise

    def is_element_present(self, loc):
        """check it the locate single element exist
        param loc: element properties
        return: True if it present; otherwise false
        """
        self.logger.info("正在查找元素：{}".format(loc))
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
        except (NoSuchElementException, TimeoutException):
            self.logger.info(
                "{0} was not found in the page {1} element".format(self, loc)
            )
            return False
        else:
            return True

    # Encapsulated input function
    def element_input(self, loc, value):
        """
        :param loc: 元素（数据结构为列表或者元组）
        :param value: 输入值
        """
        ele = self.element_find(loc)
        self.logger.info("正在清空：{}元素内容".format(loc))
        ele.clear()
        ele.send_keys(Keys.CONTROL + "a")
        self.logger.info("正在对：{}元素执行输入：{}操作".format(loc, value))
        ele.send_keys(value)
        sleep(2)

    # Encapsulated click function
    def element_click(self, loc):
        """
        :param loc: 元素（数据结构为列表或者元组）
        """
        self.logger.info("正在对: {} 元素进行点击操作".format(loc))
        self.element_find(loc).click()
        sleep(2)

    # Encapsulated get text function
    def element_get_text(self, loc):
        """
        :param loc: 元素（数据结构为列表或者元组）
        :return:
        """
        p_text = self.element_find(loc).text
        self.logger.info("正在获取: {} 元素的文本值！获取的文本值为：{}".format(loc, p_text))
        return p_text

    # Encapsulated screenshot function
    def insert_image(self):
        self.logger.error("断言错误，正在进行截图操作...")
        filename = (
                time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + ".png"
        )
        image = BASE_PATH + os.sep + 'image' + os.sep + filename
        self.driver.get_screenshot_as_file(image)
        """
        self.logger.error("断言出错，正在将截取的错误图片写入Allure报告中")
        self.img2allure(image)
        """

    # The function will write image to report
    """
     def img2allure(self, image):
        with open(image, "rb") as f:
            allure.attach(f.read(), "Error cause", allure.attachment_type.PNG)
    """

    def get_current_driver(self):
        return self.driver


    def switch_frame(self, loc):
        """
        switch multiple frame
        :param loc: element properties
        :return: the located elements
        """
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            self.logger.error("search iframe exception-> {0}".format(msg))

    def switch_window(self, index):
        """
        switch multiple window
        param window handle index
        return:
        """
        try:
            windowstab = self.driver.window_handles
            self.driver.switch_to.window(windowstab[index])
        except NoSuchWindowException as msg:
            self.logger.error("switch window exception-> {0}".format(msg))

    def switch_alert(self):
        """
        handle alert
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            self.logger.error("search alert window exception-> {0}".format(msg))

    # redefine send_keys function
    def send_key(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr same as self.loc
            if click_first:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(value)
        except AttributeError:
            self.logger.error("%s can't be found in page %s element" % (self, loc))

    def open(self, url):
        """
        invoke _open private function
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def moveto_main_page(self):
        self.element_click(page.mainPage)

    """是否能点击"""

    def is_enable(self, loc):
        try:
            self.element_click(loc)
            return True
        except ElementClickInterceptedException as e:
            self.logger.info(e)
            return False
        except:
            self.logger.error("Unexpected error: %s", sys.exc_info()[0])
            raise

    """鼠标挪到页面某个元素上"""
    def mouse_move_to_element(self,loc):
        element = self.pagewsp.element_find(loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def elements_find(self, loc, timeout=30, poll=0.3):
        """
        :param loc: 元素（数据结构为列表或者元组）
        :param timeout: 超时时间，默认30
        :param poll: 步频，默认0.5
        :return: 元素
        """
        self.logger.info("正在查找元素：{}".format(loc))
        try:
            return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        except (NoSuchElementException, TimeoutException):
            self.logger.error(
                "{0} can't be found in the page {1} element".format(self, loc)
            )
            # save the screenshot
            self.insert_image()
            raise


    def elements_get_text(self, loc):
        """
        :param loc: 元素（数据结构为列表或者元组）
        :return:
        """
        info = self.elements_find(loc)
        list = []
        for i in info:
            list.append(i.text)
        self.logger.info("正在获取: {} 元素的文本值！获取的文本值为：{}".format(loc, list))
        return list