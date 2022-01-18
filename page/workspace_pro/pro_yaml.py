# _*_coding: utf-8_*_
#
# @Project_Name:GUIAutoTest
# @File_name: pro_yaml.py
# @author: kyle
# @date: 2022/1/7 16:03
from utils.yaml_utils import GetYaml


class ProYaml(GetYaml):

    def get_index_url(self):
        data = self.get_yaml("config.yaml")
        return data['index_URL']['URL']

    def get_LoginInfo(self):
        data = self.get_yaml("workspace_pro.yaml")
        return data['login_info']['username'], data['login_info']['password']

    def get_space_name(self):
        return GetYaml.get_yaml(self, "workspace_pro.yaml")['base_space']['spaceName']

    def get_new_project(self):
        data = GetYaml.get_yaml(self, "workspace_pro.yaml")
        return data['new_project']['projectName'], \
               data['new_project']['projectSpaceName'], \
               data['new_project']['projectSpecialName']


