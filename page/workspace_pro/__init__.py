# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: __init__.py
# @author: kyle
# @date: 2022/1/6 12:26
from selenium.webdriver.common.by import By

from utils.yaml_utils import GetYaml

url_index = GetYaml('config.yaml').get_vstudio_URL()

space_search = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/input')
space_base = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div[3]/div/span')
project_list = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/table/thead/tr/th[1]/span')

# input_project = (By.XPATH, '')

# new_project_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[1]/div/div[1]/div/button/span[1]')
new_project_btn = (By.CSS_SELECTOR, '#mainContent > section > div > div.MuiGrid-root.jss2360.MuiGrid-container.MuiGrid-item.MuiGrid-grid-xs-true > div.MuiGrid-root.jss2361.MuiGrid-container > div > div.MuiGrid-root.MuiGrid-container > div > div:nth-child(1) > div > div.MuiGrid-root.jss2385.MuiGrid-item > button')
new_project_pro = (By.XPATH, '//*[@id="menu"]/div[3]/ul/li/div/div/div[1]')

new_project_search = (By.XPATH, '')
new_project_name = (By.XPATH, '')
new_project_sure = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[1]')

project_search = (By.XPATH, '')
project_search_name = (By.XPATH, '')
project_search_space = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/table/tbody/tr/td')
