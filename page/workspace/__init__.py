# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: __init__.py
# @author: kyle
# @date: 2021/12/27 14:07
from selenium.webdriver.common.by import By

# new work space
workspace_btn = (By.XPATH, "//*[@id='sidebar']/div/a[2]/div/span")
new_workspace_btn = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div/div[1]/div/div[1]/div/button/span[1]")
new_workspace_name = (By.XPATH, "//*[@id='mainContent']/section/div/div[3]/div/div/div/div[2]/div/div[2]/input")
new_workspace_sure = (By.XPATH, "//*[@id='mainContent']/section/div/div[3]/div/div/div/div[3]/div/div[1]/button")
new_workspace_search = (By.XPATH, "//*[@id='mainContent']/section/div/div[3]/div/div/div/div[1]/div/span")

# del work space
# del_workspace_btn = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[6]/div/div/button[1]/span[1]/div/div/span")
"""第一行的删除按钮"""
del_workspace_btn = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[6]/div/div/button[1]/span[1]/div/div/span")
# del_workspace_sure = (By.XPATH, "/html/body/div[@id='app']/div[@class='jss1']/div[@class='jss195 jss200']/main[@id='mainContent']/section[@class='jss215 jss213']/div[@class='MuiGrid-root jss682 MuiGrid-container MuiGrid-direction-xs-column MuiGrid-wrap-xs-nowrap']/div[@class='MuiGrid-root']/div/div[@class='MuiDrawer-root MuiDrawer-docked']/div[@class='MuiPaper-root MuiDrawer-paper jss1456 jss1457 MuiDrawer-paperAnchorRight MuiDrawer-paperAnchorDockedRight MuiPaper-elevation0']/div[@class='MuiGrid-root jss1455 MuiGrid-container MuiGrid-direction-xs-column']/div[@class='MuiGrid-root jss1466 MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-xs-flex-end']/div[@class='MuiGrid-root MuiGrid-container MuiGrid-wrap-xs-nowrap MuiGrid-justify-xs-flex-end']/div[@class='MuiGrid-root jss1470 jss1471 jss1474']/button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']/span[@class='MuiButton-label']")
del_workspace_sure = (By.XPATH, "//*[@id='mainContent']/section/div/div[3]/div/div/div/div/div[3]/div/div[1]/button/span[1]")
del_workspace_search = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/tbody/tr/td")
del_all = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/div/div/button[1]/span[1]/div/div/span')


# import or export work space
im_workspace = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/button/span[1]/span[2]")
ex_workspace = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[6]/div/div/button[3]/span[1]/div/div/span')
space_toast_format = (By.XPATH, '')
space_upload_choose = (By.XPATH, '')
fileMgmt_upload_prompt = (By.XPATH, '')
spage_file_upload_prompt = (By.XPATH, '')
fileMgmt_upload_cancel = (By.XPATH, '')
file_upload_choose_btn = (By.XPATH, '')
file_upload_confirm = (By.XPATH, '')
file_firstline_ID = (By.XPATH, '')
im_space = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/div/div[3]/div/span')
imsencond = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/tbody/tr/td')

# 获取页面的工程数量
space_count = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span")

# search_box
search_box = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/input")
search_res = (By.XPATH,"//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div[3]/div/span")

# index_btn
index_btn = (By.XPATH, "//*[@id='sidebar']/div/a[1]/div/span")
toastinfo = (By.XPATH, "//*[@id='3famvuaw71']/div[1]/div/div[2]")

# workspace_list
workspace_list = (
By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody")
spacename = (
By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[1]/span")
spacedes = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[2]')
spaceauth = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[3]/span')
spaceacreat = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[4]/span')
spaceend = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/thead/tr/th[5]/span')
workspace_ele_click = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/div/div[3]/div/span'
)
pro_ele = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div[3]/div/span'
)
workspace_fuzzy = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table'
)

# enshrine workspace
enshrine_space = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[6]/div/div/button[2]/span[1]/div/div/span')
enshrine_btn = (By.XPATH, '//*[@id="sidebar"]/div/a[5]/div/span')
enshring_search = (By.XPATH, '//*[@id="mainContent"]/section/div/div/div[1]/div[2]/div/div/div/input')
enshrine_list = (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div/div/div/div/div/div[1]/table/tbody/tr/td')
enshrine_not = (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr/td[4]/div/div/button/span[1]/div/div/span')

# workspace update
#spaceupdate = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div[3]/div/span')
update_icon = (By.CSS_SELECTOR, '.icon-edit5')
sucess_icon = (By.CSS_SELECTOR, '.icon-success')
spaceupdate = (By.CSS_SELECTOR, '.MuiInput-input')
#spaceupdate = (By.XPATH, "//main[@id='mainContent']/section/div/div[2]/div/div/div[2]/div/div/div/div/table/tbody/tr/td/div/div[3]/div/div/div/div/input")