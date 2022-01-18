from selenium.webdriver.common.by import By

""""右上角的用户信息"""
roleMgmt_userinfo_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/header/div/div[2]/div/div[2]/button')

""" 各菜单主页面 """
""" 主页 """
roleMgmt_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[1]/div/div[1]/div/div/div/span')
""" 工作空间 """
roleMgmt_workspace_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/thead/tr')
""" 最近改动 """
roleMgmt_Recent_changes_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div/div/div/div[1]/div[1]')
""" 最近执行 """
roleMgmt_Recent_perform_main =(By.XPATH,'//*[@id="mainContent"]/section/div/div[1]/div/div/div[1]/div[1]')
""" 收藏夹 """
roleMgmt_favorites_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div/div[1]/div[1]')
""" 文件管理 """
roleMgmt_File_management_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[1]/div/span')
""" 部署历史 """
roleMgmt_Deployment_history_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div/div/div/div/div[1]/table/thead')
""" 信号查询 """
roleMgmt_Signal_matrix_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/thead/tr')
""" 版本查询 """
roleMgmt_Signal_correlation_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
""" 部署审批 """
roleMgmt_Deployment_approval_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table')
""" 参数配置 """
roleMgmt_Parameter_configuration_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div/div/div/div[2]/div')
""" 事件历史 """
roleMgmt_Events_history_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[1]')
""" 资源监控 """
roleMgmt_Resource_monitoring_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[1]/nav/ol')
""" 灵活采集 """
roleMgmt_Flexible_acquisition_main =(By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/table/thead')
""" 事件采集 """
roleMgmt_Event_collection_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/table/thead/tr')
""" 全量下载"""
roleMgmt_Full_download_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[1]/nav/ol')
""" 数采下载"""
roleMgmt_Data_download_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/table')
""" 事件下载 """
roleMgmt_Event_download_main = (By.XPATH,'//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/thead')

""" 开发运营：资源监控、信号关联、部署审批"""
roleMgmt_devOper_list = (By.XPATH, '//*[@id="sidebar"]/div/a/div')
""" 资源监控 """
roleMgmt_devOper_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 版本查询 """
roleMgmt_devOper_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 部署审批 """
roleMgmt_devOper_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')

""" 普通用户：主页、工作空间、最近改动、最近执行、收藏夹、文件管理、部署历史、信号查询、版本查询、参数配置、事件历史"""
roleMgmt_dev_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 主页 """
roleMgmt_dev_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 工作空间 """
roleMgmt_dev_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
"""最近改动"""
roleMgmt_dev_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
"""最近执行"""
roleMgmt_dev_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
"""收藏夹"""
roleMgmt_dev_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')
"""文件管理"""
roleMgmt_dev_6 = (By.XPATH,'//*[@id="sidebar"]/div/a[6]/div')
"""部署历史"""
roleMgmt_dev_7 = (By.XPATH,'//*[@id="sidebar"]/div/a[7]/div')
"""信号查询"""
roleMgmt_dev_8 = (By.XPATH,'//*[@id="sidebar"]/div/a[8]/div')
"""版本查询"""
roleMgmt_dev_9 = (By.XPATH,'//*[@id="sidebar"]/div/a[9]/div')
"""参数配置"""
roleMgmt_dev_10 = (By.XPATH,'//*[@id="sidebar"]/div/a[10]/div')
"""事件历史"""
roleMgmt_dev_11 = (By.XPATH,'//*[@id="sidebar"]/div/a[11]/div')


""" 数采运营人员：数据采集、事件采集、资源监控、信号查询、版本查询"""
roleMgmt_ac_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 灵活采集 """
roleMgmt_ac_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 事件采集 """
roleMgmt_ac_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 资源监控 """
roleMgmt_ac_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 信号查询 """
roleMgmt_ac_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 版本查询 """
roleMgmt_ac_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')

""" 数据下载人员：全量下载、数采下载、事件下载、信号查询、版本查询"""
roleMgmt_download_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 全量下载 """
roleMgmt_download_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 数采下载 """
roleMgmt_download_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 事件下载 """
roleMgmt_download_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 信号查询 """
roleMgmt_download_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 版本查询 """
roleMgmt_download_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')


""" 数据下载+数采运营人员：数据采集、事件采集、全量下载、数采下载、事件下载、资源监控、信号查询、版本查询"""
roleMgmt_ac_download_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 灵活采集 """
roleMgmt_ac_download_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 事件采集 """
roleMgmt_ac_download_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 全量下载 """
roleMgmt_ac_download_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 数采下载 """
roleMgmt_ac_download_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 事件下载 """
roleMgmt_ac_download_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')
""" 资源监控 """
roleMgmt_ac_download_6 = (By.XPATH,'//*[@id="sidebar"]/div/a[6]/div')
""" 信号查询"""
roleMgmt_ac_download_7 = (By.XPATH,'//*[@id="sidebar"]/div/a[7]/div')
""" 版本查询 """
roleMgmt_ac_download_8 = (By.XPATH,'//*[@id="sidebar"]/div/a[8]/div')


""" 普通用户+开发运营人员：主页、工作空间、最近改动、最近执行、收藏夹、文件管理、部署历史、资源监控、信号查询、版本查询、部署审批、参数配置、事件历史"""
roleMgmt_dev_devOper_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 主页 """
roleMgmt_dev_devOper_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 工作空间 """
roleMgmt_dev_devOper_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 最近改动 """
roleMgmt_dev_devOper_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 最近执行 """
roleMgmt_dev_devOper_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 收藏夹 """
roleMgmt_dev_devOper_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')
""" 文件管理 """
roleMgmt_dev_devOper_6 = (By.XPATH,'//*[@id="sidebar"]/div/a[6]/div')
""" 部署历史 """
roleMgmt_dev_devOper_7 = (By.XPATH,'//*[@id="sidebar"]/div/a[7]/div')
""" 资源监控 """
roleMgmt_dev_devOper_8 = (By.XPATH,'//*[@id="sidebar"]/div/a[8]/div')
""" 信号查询 """
roleMgmt_dev_devOper_9 = (By.XPATH,'//*[@id="sidebar"]/div/a[9]/div')
""" 版本查询 """
roleMgmt_dev_devOper_10 = (By.XPATH,'//*[@id="sidebar"]/div/a[10]/div')
""" 部署审批 """
roleMgmt_dev_devOper_11 = (By.XPATH,'//*[@id="sidebar"]/div/a[11]/div')
""" 参数配置 """
roleMgmt_dev_devOper_12 = (By.XPATH,'//*[@id="sidebar"]/div/a[12]/div')
""" 事件历史 """
roleMgmt_dev_devOper_13 = (By.XPATH,'//*[@id="sidebar"]/div/a[13]/div')


""" 数采运营+开发运营人员(vstudio)：数据采集、事件采集、资源监控、信号查询、版本查询"""
roleMgmt_ac_devOper_vstudio_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 资源监控 """
roleMgmt_ac_devOper_vstudio_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 信号查询 """
roleMgmt_ac_devOper_vstudio_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 版本查询 """
roleMgmt_ac_devOper_vstudio_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 部署审批 """
roleMgmt_ac_devOper_vstudio_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')


""" 数采运营+开发运营人员(datacollector)：灵活采集、事件采集、资源监控、信号查询、版本查询"""
roleMgmt_ac_devOper_datacollector_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 灵活采集 """
roleMgmt_ac_devOper_datacollector_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 事件采集 """
roleMgmt_ac_devOper_datacollector_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 资源监控 """
roleMgmt_ac_devOper_datacollector_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 信号查询 """
roleMgmt_ac_devOper_datacollector_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 版本查询 """
roleMgmt_ac_devOper_datacollector_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')


""" 数据下载+开发运营人员(vstudio)：资源监控、信号查询、版本查询、部署审批"""
roleMgmt_download_devOper_vstudio_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 资源监控 """
roleMgmt_download_devOper_vstudio_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 信号查询 """
roleMgmt_download_devOper_vstudio_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 版本查询 """
roleMgmt_download_devOper_vstudio_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 部署审批 """
roleMgmt_download_devOper_vstudio_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')


""" 数据下载+开发运营人员(datacollector)：全量下载、数采下载、事件下载、资源监控、信号查询、版本查询"""
roleMgmt_download_devOper_datacollector_list =  (By.XPATH,'//*[@id="sidebar"]/div/a/div')
""" 全量下载 """
roleMgmt_download_devOper_datacollector_1 = (By.XPATH,'//*[@id="sidebar"]/div/a[1]/div')
""" 数采下载 """
roleMgmt_download_devOper_datacollector_2 = (By.XPATH,'//*[@id="sidebar"]/div/a[2]/div')
""" 事件下载 """
roleMgmt_download_devOper_datacollector_3 = (By.XPATH,'//*[@id="sidebar"]/div/a[3]/div')
""" 资源监控 """
roleMgmt_download_devOper_datacollector_4 = (By.XPATH,'//*[@id="sidebar"]/div/a[4]/div')
""" 信号查询 """
roleMgmt_download_devOper_datacollector_5 = (By.XPATH,'//*[@id="sidebar"]/div/a[5]/div')
""" 版本查询 """
roleMgmt_download_devOper_datacollector_6 = (By.XPATH,'//*[@id="sidebar"]/div/a[6]/div')

roleMgmt_stop_login_text = (By.XPATH, '//*[@id="kc-content-wrapper"]/div[1]/span[2]')













