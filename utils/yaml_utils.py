import os
import yaml
from config import BASE_PATH


class GetYaml:
    def __init__(self, filename):
        self.path = BASE_PATH + os.sep + "data"

    def get_yaml(self, filename):
        filepath = self.path + os.sep + filename
        try:
            f = open(filepath, encoding="utf-8")
            data = yaml.safe_load(f)
            f.close()
            return data
        except Exception as msg:
            print("exceptionmsg-> {0}".format(msg))

    def get_yaml_As_List(self, filename):
        file_path = self.path + os.sep + filename
        arr = []
        with open(file_path, "r", encoding="utf-8") as f:
            for datas in yaml.safe_load(f).values():
                arr.append(tuple(datas.values()))
        return arr

    def get_dev_LoginInfo(self):
        data = self.get_yaml("Login.yaml")
        return data['vstudio_dev']['username'], data['vstudio_dev']['password']

    def get_admin_LoginInfo(self):
        data = self.get_yaml("Login.yaml")
        return data['admin']['username'], data['admin']['password']

    def get_invalid_userInfo(self):
        data = self.get_yaml("Login.yaml")
        return data['invalid_user']['username'], data['invalid_user']['password']

    def get_fileMgmt_DirSelect(self):
        data = self.get_yaml("file_Mgmt.yaml")
        return data['DirSelect']['dirname']

    def getUploadInfo(self):
        data = self.get_yaml("file_Mgmt.yaml")
        return data['uploadFile']['filepath'], data['uploadFile']['filename']

    def get_abnormaluserMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['abnormal']['username'], data['user_Mgmt']['abnormal']['email'], \
               data['user_Mgmt']['abnormal']['password'], data['user_Mgmt']['abnormal']['surname'], \
               data['user_Mgmt']['abnormal']['name']

    def get_normaluserMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['normal']['username'], data['user_Mgmt']['normal']['email'], \
               data['user_Mgmt']['normal']['password'], data['user_Mgmt']['normal']['surname'], \
               data['user_Mgmt']['normal']['name']

    def find_userMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['normal']['username']

    def get_normalUser_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['normalUser_group_Mgmt']['groupname'], data['normalUser_group_Mgmt']['rolename']

    def find_normalUser_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['normalUser_group_Mgmt']['groupname']

    def get_operator_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['operator_group_Mgmt']['groupname'], data['operator_group_Mgmt']['rolename']

    def find_operator_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['operator_group_Mgmt']['groupname']

    def get_downloader_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['downloader_group_Mgmt']['groupname'], data['downloader_group_Mgmt']['rolename']

    def find_downloader_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['downloader_group_Mgmt']['groupname']

    def get_acquisition_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['acquisition_group_Mgmt']['groupname'], data['acquisition_group_Mgmt']['rolename']

    def find_acquisition_groupMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['acquisition_group_Mgmt']['groupname']

    def get_vstudio_URL(self):
        data = self.get_yaml("config.yaml")
        return data['vstudio_URL']['URL']

    def get_DC_URL(self):
        data = self.get_yaml("config.yaml")
        return data['datacollector_URL']['URL']

    def get_wkspace_Info(self):
        data = self.get_yaml("new_workspace.yaml")
        return data["workspace"]["spacename"], \
               data["workspace"]["spacenamefir"], \
               data["workspace"]["spacenamesen"], \
               data["workspace"]["spacename_chinese"]

    def get_fuzzy_list(self):
        data = self.get_yaml("new_workspace.yaml")
        return data["fuzzy_list"]

    def get_workspace_list(self):
        data = self.get_yaml("new_workspace.yaml")
        return data["workspace"]

    def get_groupNames_Mgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['groupNames']

    def get_im_space(self):
        data = self.get_yaml("new_workspace.yaml")
        return data['workspace_in']['filepath'], data['workspace_in']['filename']

    def get_im_upname(self):
        data = self.get_yaml("new_workspace.yaml")
        return data['workspace_upname']['filepath'], data['workspace_upname']['filename']

    def get_im_updes(self):
        data = self.get_yaml("new_workspace.yaml")
        return data['workspace_updes']['filepath'], data['workspace_updes']['filename']

    def get_index_url(self):
        data = self.get_yaml("config.yaml")
        return data['index_URL']['URL']

    def get_normal1userMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['normal1']['username'], data['user_Mgmt']['normal1']['email'], \
               data['user_Mgmt']['normal1']['password'], data['user_Mgmt']['normal1']['surname'], \
               data['user_Mgmt']['normal1']['name']

    def find_user1Mgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['normal1']['username']

    def get_role_LoginInfo(self):
        data = self.get_yaml("Login.yaml")
        return data['vstudio_role']['username'], data['vstudio_role']['password']

    def get_rules_userMgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['user_Mgmt']['rules']['username'], data['user_Mgmt']['rules']['email'], data['user_Mgmt']['rules'][
            'password'], data['user_Mgmt']['rules']['surname'], data['user_Mgmt']['rules']['name']

    def get_abuserinfo_Mgmt(self):
        data = self.get_yaml("user_Mgmt.yaml")
        return data['abuserinfo']