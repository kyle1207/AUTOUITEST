
from selenium.webdriver.common.by import By
""""导航菜单里的文件管理"""
fileMgmt_management_btn = (By.XPATH, "//*[@id='sidebar']/div/a[6]/div/span")

""" file upload """

fileMgmt_upload_btn = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[1]/div[1]/button/span[1]")
fileMgmt_upload_choose_btn = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[2]")
fileMgmt_upload_confirm = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[3]/div/button[1]/span[1]")
fileMgmt_upload_cancel = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[3]/div/button[2]/span[1]")
fileMgmt_upload_prompt = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div")

""" create dir"""
fileMgmt_makedir = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div[1]/button/span[1]")
fileMgmt_dirname = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/input")
fileMgmt_mkdir_confirm = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div[3]/div/div/div/div[3]/div/button[1]/span[1]")
fileMgmt_mkdir_cancel = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div[3]/div/button[2]/span[1]")

""""页面底部的 共几个"""
fileMgmt_file_count = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[2]/div/div/div/div/div[2]")

""""第一行的数据"""
fileMgmt_firstline_ID = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td[2]/div/span")