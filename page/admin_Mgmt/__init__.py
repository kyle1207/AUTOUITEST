from selenium.webdriver.common.by import By

"""login"""
usershow_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/header/div/div[2]/div/div/button/span[1]')
adminshow_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/header/div/div[2]/div/div[2]/button/span[1]')

"""logout"""
logout_ID = (By.XPATH, "//*[@id='customized-menu']/div[3]/ul/li[2]/div[2]/span")
admin_logout_ID = (By.XPATH, "//*[@id='customized-menu']/div[3]/ul/li[4]/div[2]/span")

""""右上角的用户信息"""
# adminMgmt_userinfo_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/header/div/div[2]/div/div[2]/button')

adminMgmt_userinfo_btn = (By.CSS_SELECTOR, '.MuiButton-label > span')

"""admin后台菜单list"""
""""右上角的后台管理"""
adminMgmt_background_btn = (By.XPATH, '//*[@id="customized-menu"]/div[3]/ul/li[1]/div[2]')
"""主页"""
adminshow_user_number = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div[2]/div[1]')
"""用户管理"""
adminshow_user_manage = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""用户组"""
adminshow_group_manage = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table')
"""车辆分组"""
adminshow_vehicle_manage = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""车辆查询"""
adminshow_vehicle_search = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""信号矩阵管理"""
adminshow_signal_search = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""用户参数配置"""
adminshow_parameter_config = (By.XPATH, '//*[@id="mainContent"]/section/div/div[1]')
"""授权书管理"""
adminshow_authorization = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[1]')

""" admin后台管理：主页、用户管理、用户组、车辆分组、车辆查询、信号矩阵管理、用户参数配置、授权书管理"""
adminshow_backgroup_list = (By.XPATH, '//*[@id="sidebar"]/div/a/div')
""" 主页 """
adminshow_backgroup_1 = (By.XPATH, '//*[@id="sidebar"]/div/a[1]/div')
""" 用户管理 """
adminshow_backgroup_2 = (By.XPATH, '//*[@id="sidebar"]/div/a[2]/div')
""""用户组"""
adminshow_backgroup_3 = (By.XPATH, '//*[@id="sidebar"]/div/a[3]')
""""车辆分组"""
adminshow_backgroup_4 = (By.XPATH, '//*[@id="sidebar"]/div/a[4]')
""""车辆查询"""
adminshow_backgroup_5 = (By.XPATH, '//*[@id="sidebar"]/div/a[5]')
""""信号矩阵管理"""
adminshow_backgroup_6 = (By.XPATH, '//*[@id="sidebar"]/div/a[6]')
""""用户参数配置"""
adminshow_backgroup_7 = (By.XPATH, '//*[@id="sidebar"]/div/a[7]')
""""授权书管理"""
adminshow_backgroup_8 = (By.XPATH, '//*[@id="sidebar"]/div/a[8]')

"""admin前台菜单list"""
""""右上角的前台应用"""
adminMgmt_application_btn = (By.XPATH, '//*[@id="customized-menu"]/div[3]/ul/li[2]/div[2]')
"""主页"""
adminshow_hello = (By.XPATH, '//*[@id="mainContent"]/section/div/div[1]/div/div[1]/div/div/div/div/p')
"""工作空间"""
adminshow_workspace = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""最近改动"""
adminshow_Recent_changes = (
By.XPATH, '//*[@id="mainContent"]/section/div/div/div/div/div[2]/div/div[1]/div/div[1]/table')
"""最近执行"""
adminshow_Recent_perform = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/table')
"""收藏夹"""
adminshow_favorites = (By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div/div/div/div[1]/div/div[1]/table')
"""文件管理"""
adminshow_File_management = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/table')
"""部署历史"""
adminshow_deployment_history = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div/div/div[1]/div/div[1]/table')
"""参数配置"""
adminshow_Parameter_configuration = (By.XPATH, '//*[@id="mainContent"]/section/div/div/div/div/p')

""" admin后台管理：主页、工作空间、最近改动、最近执行、收藏夹、文件管理、部署历史、参数配置"""
adminshow_application_list = (By.XPATH, '//*[@id="sidebar"]/div/a/div')
""" 主页 """
adminshow_application_1 = (By.XPATH, '//*[@id="sidebar"]/div/a[1]/div')
""" 工作空间 """
adminshow_application_2 = (By.XPATH, '//*[@id="sidebar"]/div/a[2]/div')
""""最近改动"""
adminshow_application_3 = (By.XPATH, '//*[@id="sidebar"]/div/a[3]')
""""最近执行"""
adminshow_application_4 = (By.XPATH, '//*[@id="sidebar"]/div/a[4]')
""""收藏夹"""
adminshow_application_5 = (By.XPATH, '//*[@id="sidebar"]/div/a[5]')
""""文件管理"""
adminshow_application_6 = (By.XPATH, '//*[@id="sidebar"]/div/a[6]')
""""部署历史"""
adminshow_application_7 = (By.XPATH, '//*[@id="sidebar"]/div/a[7]')
""""参数配置"""
adminshow_application_8 = (By.XPATH, '//*[@id="sidebar"]/div/a[8]')

""" create group"""
adminMgmt_groupmanagement_btn = (By.XPATH, '//*[@id="sidebar"]/div/a[3]/div')
adminMgmt_addgroup = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[1]/button')
adminMgmt_groupname = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/input')
adminMgmt_selectrole_dropdown = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]/div')
adminMgmt_selectrole_normal = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
adminMgmt_selectrole_dev_operator = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')
adminMgmt_selectrole_acquisition_operator = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')
adminMgmt_selectrole_download = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]')

adminMgmt_addgroup_confirm = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[1]/button')
adminMgmt_addgroup_cancel = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[3]/div/div/div/div[3]/div/button[2]/span[1]')

""""页面底部的共几个用户组"""
adminMgmt_group_count = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/span/span')

""""第一行用户组的数据"""
adminMgmt_firstgroup_role = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]')
adminMgmt_firstgroup_ID = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]')
""" search group"""
adminMgmt_group_list = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr')
adminMgmt_searchgroup = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[1]/div/div/div/div/input')
adminMgmt_nofindgroupname = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div/div/div[1]/table/tbody/tr')
adminMgmt_findgroupname = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody')
adminMgmt_cleargroup = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[1]/div/div/div/div/button')

""" edit group """
adminMgmt_group_edit_btn = (By.XPATH,
                            '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/div/div/button[1]/span[1]')
adminMgmt_groupname_edited = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]')
adminMgmt_role_edited = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[5]')
adminMgmt_edit_role_confirm = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]')
"""delete group"""
adminMgmt_deletegroup_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div['
                                       '1]/table/tbody/tr/td[6]/div/div/button[2]')
adminMgmt_deletegroup_confirm_btn = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div/div[3]/div/div[1]/button')
adminMgmt_deletegroup_confirm = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div/div[3]/div/div[1]')
adminMgmt_deletegroup_warning = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div')
adminMgmt_deletegroup_impact = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div/div[2]/div/div[2]/div/div[2]/p[2]')
""" group list """
adminMgmt_group_contains_user_btn = (
    By.XPATH,
    '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[1]/button')
adminMgmt_userlist_btn = (
    By.XPATH,
    '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/button')
adminMgmt_userlist = (By.XPATH,
                      '//*[@id="mainContent"]/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/table/tbody/td/div/div/div/table/tbody/tr')

""""导航菜单里的用户管理"""
adminMgmt_usermanagement_btn = (By.XPATH, '//*[@id="sidebar"]/div/a[2]/div/span')

""" create user"""
adminMgmt_adduser_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[1]/div/div[1]/div/button')
adminMgmt_adduserpage_open = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[1]/div/span')
adminMgmt_adduserpage_shut = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[1]/button')
adminMgmt_username = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[1]')
adminMgmt_username_notempty = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[1]/span/div/div/span')
adminMgmt_password = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[4]/div[1]')
adminMgmt_password_noteempty = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[4]/div[1]/span/div/div/span')
adminMgmt_surname = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[5]/div[1]')
adminMgmt_surname_notempty = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[5]/div[1]/span/div/div/span')
adminMgmt_name = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]/div[1]')
adminMgmt_name_notempty = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]/div[1]/span/div/div/span')
adminMgmt_username_input = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div['
                                      '2]/div/input')
adminMgmt_username_prompt = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]')
adminMgmt_email_input = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[3]/div[2]/div/input')

adminMgmt_password_input = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[4]/div['
                                      '2]/div/input')
adminMgmt_surname_input = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[5]/div['
                                     '2]/div/input')
adminMgmt_name_input = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]/div[2]/div/input')

adminMgmt_adduser_confirm = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[1]')

adminMgmt_adduser_success = (By.CSS_SELECTOR, '//*[@id="zn5b57uftw"]/div[1]/div/div[2]')
adminMgmt_adduser_repeat = (By.XPATH, '//*[@id="zrh5w484bf"]/div[1]/div/div[2]')
adminMgmt_adduser_abnormal = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]')
adminMgmt_adduser_cancel = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[2]')
adminMgmt_name_rp_close = (By.XPATH, '//*[@id="foai2lwm33"]/button')
adminMgmt_adduser_find = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody')
adminMgmt_username_list = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[1]')
adminMgmt_username_mandatory = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]')
adminMgmt_password_mandatory = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[4]/div[3]')
adminMgmt_surname_mandatory = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[5]/div[3]')
adminMgmt_name_mandatory = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[6]/div[3]')

""""页面底部的共几个用户"""
adminMgmt_user_count = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[2]/div/div/div['
                                  '1]/span/span')

""""第一行用户的数据"""
adminMgmt_firstuser_ID = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]')
adminMgmt_firstuser_name = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]')

""" search user"""
adminMgmt_searchuser = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[1]/div/div['
                                  '2]/div/div/div/div/div/input')

adminMgmt_findusername = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr')
adminMgmt_nofindusername = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div/div/div[1]/table/tbody/tr')

adminMgmt_clearuser = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[1]/div/div['
                                 '2]/div/div/div/div/div/button')
""" user list """
adminMgmt_alluser_list = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]')
adminMgmt_usergroup_list = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div['
                                      '1]/table/tbody/tr/td[4]')

"""delete user"""
adminMgmt_deleteuser_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div['
                                      '1]/table/tbody/tr[1]/td[6]/div/div/button[2]')
adminMgmt_deleteuser_confirm = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div/div[3]/div/div['
                                          '1]/button')

""" select user"""
adminMgmt_selectuser = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div['
                                  '1]/table/tbody/tr')

""" 更多"""
adminMgmt_more_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div['
                                '1]/table/tbody/tr/td[6]/div/div/div/button')
""" 用户分组"""
adminMgmt_usergroup_btn = (By.XPATH, '//*[@id="tabele-operations-menu-0"]/div[3]/ul/li[3]')

""" 重置密码"""
adminMgmt_password_btn = (By.XPATH, '//*[@id="tabele-operations-menu-0"]/div[3]/ul/li[2]')
adminMgmt_userinfo_confirm = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[1]')
adminMgmt_newpass_input = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/input')
adminMgmt_confirm_btn = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[1]')
"""启用、停用"""
adminMgmt_state = (By.XPATH,
                   '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/div/div/span[2]')
adminMgmt_stop_start_btn = (By.XPATH,
                            '//*[@id="mainContent"]/section/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/div/div/button[1]')
adminMgmt_stop_confirm = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[1]/div/span')
adminMgmt_stop_warning = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div')
adminMgmt_stop_confirm_btn = (
By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[3]/div/div[1]/button')
adminMgmt_stop_success = (By.XPATH, '//*[@id="peoqhvvtor"]/div[1]')
adminMgmt_start_success = (By.XPATH, '//*[@id="99b5v53y0p"]/div[1]')

""" 确认用户信息"""
adminMgmt_judguser = (By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div['
                                '2]/div')

""" 勾选普通用户组"""
""" 用户组列表"""
adminMgmt_group_lists = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]')
adminMgmt_Check_lists = (
    By.XPATH, '//*[@id="mainContent"]/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/span/span[1]')

""" 确认分组"""
adminMgmt_group_select_confirm = (By.XPATH, "//*[@id='mainContent']/section/div/div[3]/div/div/div/div[3]/div/div["
                                            "1]/button")

"""用户组选择"""
usergroup_select_basepath = "//main[@id='mainContent']/section/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div["
"""base + {number} + left， checkbox 后面加input就找不到元素"""
usergroup_checkbox_left = "]/div[1]/span/span[1]"
usergroup_text_left = "]/div[2]/div"
