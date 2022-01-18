from selenium.webdriver.common.by import By
from utils.yaml_utils import GetYaml

""" vs_login_config """

username_ID = (By.CSS_SELECTOR, "[id='username']")
password_ID = (By.CSS_SELECTOR, "[id='password']")
login_btn = (By.CSS_SELECTOR, ".btn-primary")

"""invalid user pwd"""
invalid_userpwd= (By.XPATH, "//*[@id='kc-content-wrapper']/div[1]/span[2]")

""""login界面的 "Log In"""
login_pagetitle = (By.XPATH, "//*[@id='kc-page-title']")

"""" 页面右上部显示的用户名"""
#usershow_ID = (By.XPATH, "//*[@id='app']/div[1]/div[2]/header/div/div[2]/div/div[2]/button/span[1]/span")
usershow_ID = (By.CSS_SELECTOR, '.MuiButton-label > span')

# usershow_ID = (By.XPATH, "//*[@id='app']/div[1]/div[2]/header/div/div[2]/div/div/button")
adminshow_ID = (By.XPATH, "//*[@id='app']/div[1]/div[2]/header/div/div[2]/div/div[2]/button")


"""" 登录页面显示的Hello {username} """
hello_ID = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[1]/div/div/div/div/p")

"""""logout"""
logout_ID = (By.XPATH, "//*[@id='customized-menu']/div[3]/ul/li[2]/div[2]/span")
admin_logout_ID =  (By.XPATH, "//*[@id='customized-menu']/div[3]/ul/li[4]/div[2]/span")

""" url """
url_vstudio = GetYaml('config.yaml').get_vstudio_URL()
url_datacollector = GetYaml('config.yaml').get_DC_URL()
url_index = GetYaml('config.yaml').get_vstudio_URL()

"""主页的最近改动"""
recent_update_text = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[2]/div[1]/span")
recent_update_check_all = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[2]/div[1]/a")


"""最近执行"""
recent_exec_text = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[3]/div[1]/span")
recent_exec_check_all = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[3]/div[1]/a")

"""最近部署"""
recent_deploy_text = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[4]/div[1]/span")
recent_deploy_check_all =(By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div[4]/div[1]/a")

"""最近改动页面"""
recent_update_page_title = (By.XPATH, "//*[@id='mainContent']/section/div/div/div/div/div[1]/div[1]/p")
"""最近执行页面"""
recent_exec_page_title = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/div/div/div[1]/div[1]/p")
"""最近部署页面"""
recent_deploy_page_title = (By.XPATH, "//*[@id='mainContent']/section/div/div[1]/nav/ol/li/div/div/span")