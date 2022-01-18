import logging
from time import sleep

from page import role_Mgmt
from page.page_base import PageBase


class PageRoleMgmt(PageBase):
    logger = logging.getLogger(__name__)

    # 开发运营人员devOper菜单
    def page_devOper_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_devOper_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_devOper_list)

    # 开发运营人员devOper菜单点击
    def page_devOper_main_1(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_devOper_1)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_devOper_main_2(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_devOper_2)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
    def page_devOper_main_3(self):
        self.logger.info("点击部署审批菜单")
        self.element_click(role_Mgmt.roleMgmt_devOper_3)
        self.logger.info("返回部署审批页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)

    # 普通用户dev菜单
    def page_dev_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_dev_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_dev_list)

    # 普通用户dev菜单点击
    def page_dev_main_1(self):
        self.logger.info("点击主页菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_1)
        self.logger.info("返回主页面")
        self.element_find(role_Mgmt.roleMgmt_main)
    def page_dev_main_2(self):
        self.logger.info("点击工作空间菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_2)
        self.logger.info("返回工作空间页面")
        self.element_find(role_Mgmt.roleMgmt_workspace_main)
    def page_dev_main_3(self):
        self.logger.info("点击最近改动菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_3)
        self.logger.info("返回最近改动页面")
        self.element_find(role_Mgmt.roleMgmt_Recent_changes_main)
    def page_dev_main_4(self):
        self.logger.info("点击最近执行菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_4)
        self.logger.info("返回最近执行页面")
        self.element_find(role_Mgmt.roleMgmt_Recent_perform_main)
    def page_dev_main_5(self):
        self.logger.info("点击收藏夹菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_5)
        self.logger.info("返回收藏夹页面")
        self.element_find(role_Mgmt.roleMgmt_favorites_main)
    def page_dev_main_6(self):
        self.logger.info("点击文件管理菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_6)
        self.logger.info("返回文件管理页面")
        self.element_find(role_Mgmt.roleMgmt_File_management_main)
    def page_dev_main_7(self):
        self.logger.info("点击部署历史菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_7)
        self.logger.info("返回部署历史页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_history_main)
    def page_dev_main_8(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_8)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_dev_main_9(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_9)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
    def page_dev_main_10(self):
        self.logger.info("点击参数配置菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_10)
        self.logger.info("返回参数配置页面")
        self.element_find(role_Mgmt.roleMgmt_Parameter_configuration_main)
    def page_dev_main_11(self):
        self.logger.info("点击事件历史菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_11)
        self.logger.info("返回事件历史页面")
        self.element_find(role_Mgmt.roleMgmt_Events_history_main)

    # 数采运营人员ac菜单
    def page_ac_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_ac_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_ac_list)

    # 数采运营人员ac菜单点击
    def page_ac_main_1(self):
        self.logger.info("点击灵活采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_1)
        self.logger.info("返回灵活采集页面")
        self.element_find(role_Mgmt.roleMgmt_Flexible_acquisition_main)
    def page_ac_main_2(self):
        self.logger.info("点击事件采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_2)
        self.logger.info("返回事件采集页面")
        self.element_find(role_Mgmt.roleMgmt_Event_collection_main)
    def page_ac_main_3(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_3)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_ac_main_4(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_4)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_ac_main_5(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_5)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)


    # 数据下载人员download菜单
    def page_download_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_download_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_download_list)

    # 数据下载人员download菜单点击
    def page_download_main_1(self):
        self.logger.info("点击全量下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_1)
        self.logger.info("返回全量下载页面")
        self.element_find(role_Mgmt.roleMgmt_Full_download_main)
    def page_download_main_2(self):
        self.logger.info("点击数采下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_2)
        self.logger.info("返回数采下载页面")
        self.element_find(role_Mgmt.roleMgmt_Data_download_main)
    def page_download_main_3(self):
        self.logger.info("点击事件下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_3)
        self.logger.info("返回事件下载页面")
        self.element_find(role_Mgmt.roleMgmt_Event_download_main)
    def page_download_main_4(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_4)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_download_main_5(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_5)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)

    # 数采运营ac+数据下载download菜单list
    def page_ac_download_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_ac_download_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_ac_download_list)

    # 数采运营ac+数据下载download菜单点击
    def page_ac_download_main_1(self):
        self.logger.info("点击灵活采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_1)
        self.logger.info("返回灵活采集页面")
        self.element_find(role_Mgmt.roleMgmt_Flexible_acquisition_main)
    def page_ac_download_main_2(self):
        self.logger.info("点击事件采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_2)
        self.logger.info("返回事件采集页面")
        self.element_find(role_Mgmt.roleMgmt_Event_collection_main)
    def page_ac_download_main_3(self):
        self.logger.info("点击全量下载菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_3)
        self.logger.info("返回全量下载页面")
        self.element_find(role_Mgmt.roleMgmt_Full_download_main)
    def page_ac_download_main_4(self):
        self.logger.info("点击数采下载菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_4)
        self.logger.info("返回数采下载页面")
        self.element_find(role_Mgmt.roleMgmt_Data_download_main)
    def page_ac_download_main_5(self):
        self.logger.info("点击事件下载菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_5)
        self.logger.info("返回事件下载页面")
        self.element_find(role_Mgmt.roleMgmt_Event_download_main)
    def page_ac_download_main_6(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_6)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_ac_download_main_7(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_7)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_ac_download_main_8(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_download_8)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)

    # 开发运营devOper+普通用户dev菜单list
    def page_dev_devOper_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_dev_devOper_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_dev_devOper_list)

    # 开发运营devOper+普通用户dev菜单点击
    def page_dev_devOper_main_1(self):
        self.logger.info("点击主页菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_1)
        self.logger.info("返回主页页面")
        self.element_find(role_Mgmt.roleMgmt_main)
    def page_dev_devOper_main_2(self):
        self.logger.info("点击工作空间菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_2)
        self.logger.info("返回工作空间页面")
        self.element_find(role_Mgmt.roleMgmt_workspace_main)
    def page_dev_devOper_main_3(self):
        self.logger.info("点击最近改动菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_3)
        self.logger.info("返回最近改动页面")
        self.element_find(role_Mgmt.roleMgmt_Recent_changes_main)
    def page_dev_devOper_main_4(self):
        self.logger.info("点击最近执行菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_4)
        self.logger.info("返回最近执行页面")
        self.element_find(role_Mgmt.roleMgmt_Recent_perform_main)
    def page_dev_devOper_main_5(self):
        self.logger.info("点击收藏夹菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_5)
        self.logger.info("返回收藏夹页面")
        self.element_find(role_Mgmt.roleMgmt_favorites_main)
    def page_dev_devOper_main_6(self):
        self.logger.info("点击文件管理菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_6)
        self.logger.info("返回文件管理页面")
        self.element_find(role_Mgmt.roleMgmt_File_management_main)
    def page_dev_devOper_main_7(self):
        self.logger.info("点击部署历史菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_7)
        self.logger.info("返回部署历史页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_history_main)
    def page_dev_devOper_main_8(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_8)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_dev_devOper_main_9(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_9)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_dev_devOper_main_10(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_10)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
    def page_dev_devOper_main_11(self):
        self.logger.info("点击部署审批菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_11)
        self.logger.info("返回部署审批页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)
    def page_dev_devOper_main_12(self):
        self.logger.info("点击参数配置菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_12)
        self.logger.info("返回参数配置页面")
        self.element_find(role_Mgmt.roleMgmt_Parameter_configuration_main)
    def page_dev_devOper_main_13(self):
        self.logger.info("点击事件历史菜单")
        self.element_click(role_Mgmt.roleMgmt_dev_devOper_13)
        self.logger.info("返回事件历史页面")
        self.element_find(role_Mgmt.roleMgmt_Events_history_main)

    # 数采运营+开发运营人员vstudio菜单
    def page_ac_devOper_vstudio_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_ac_devOper_vstudio_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_ac_devOper_vstudio_list)

    # 数采运营人员ac菜单vstudio点击
    def page_ac_devOper_vstudio_main_1(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_vstudio_1)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_ac_devOper_vstudio_main_2(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_vstudio_2)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_ac_devOper_vstudio_main_3(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_vstudio_3)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)
    def page_ac_devOper_vstudio_main_4(self):
        self.logger.info("点击部署审批菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_vstudio_4)
        self.logger.info("返回部署审批页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)

    # 数采运营人员+开发运营人员datacollector菜单
    def page_ac_devOper_datacollector_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_ac_devOper_datacollector_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_ac_devOper_datacollector_list)

    # 数采运营人员+开发运营人员datacollector菜单点击
    def page_ac_devOper_datacollector_main_1(self):
        self.logger.info("点击灵活采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_datacollector_1)
        self.logger.info("返回灵活采集页面")
        self.element_find(role_Mgmt.roleMgmt_Flexible_acquisition_main)
    def page_ac_devOper_datacollector_main_2(self):
        self.logger.info("点击事件采集菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_datacollector_2)
        self.logger.info("返回事件采集页面")
        self.element_find(role_Mgmt.roleMgmt_Event_collection_main)
    def page_ac_devOper_datacollector_main_3(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_datacollector_3)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)
    def page_ac_devOper_datacollector_main_4(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_datacollector_4)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)
    def page_ac_devOper_datacollector_main_5(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_ac_devOper_datacollector_5)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)

    # 数据下载+开发运营人员vstudio菜单
    def page_download_devOper_vstudio_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_download_devOper_vstudio_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_download_devOper_vstudio_list)

    # 数据下载人员download菜单vstudio点击
    def page_download_devOper_vstudio_main_1(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_vstudio_1)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)

    def page_download_devOper_vstudio_main_2(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_vstudio_2)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)

    def page_download_devOper_vstudio_main_3(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_vstudio_3)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)

    def page_download_devOper_vstudio_main_4(self):
        self.logger.info("点击部署审批菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_vstudio_4)
        self.logger.info("返回部署审批页面")
        self.element_find(role_Mgmt.roleMgmt_Deployment_approval_main)

    # 数据下载人员+开发运营人员datacollector菜单
    def page_download_devOper_datacollector_list(self):
        self.logger.info("查找菜单组")
        self.elements_find(role_Mgmt.roleMgmt_download_devOper_datacollector_list)
        return self.elements_get_text(role_Mgmt.roleMgmt_download_devOper_datacollector_list)

    # 数据下载人员+开发运营人员datacollector菜单点击
    def page_download_devOper_datacollector_main_1(self):
        self.logger.info("点击全量下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_1)
        self.logger.info("返回全量下载页面")
        self.element_find(role_Mgmt.roleMgmt_Full_download_main)

    def page_download_devOper_datacollector_main_2(self):
        self.logger.info("点击数采下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_2)
        self.logger.info("返回数采下载页面")
        self.element_find(role_Mgmt.roleMgmt_Data_download_main)

    def page_download_devOper_datacollector_main_3(self):
        self.logger.info("点击事件下载菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_3)
        self.logger.info("返回事件下载页面")
        self.element_find(role_Mgmt.roleMgmt_Event_download_main)

    def page_download_devOper_datacollector_main_4(self):
        self.logger.info("点击资源监控菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_4)
        self.logger.info("返回资源监控页面")
        self.element_find(role_Mgmt.roleMgmt_Resource_monitoring_main)

    def page_download_devOper_datacollector_main_5(self):
        self.logger.info("点击信号查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_5)
        self.logger.info("返回信号查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_matrix_main)

    def page_download_devOper_datacollector_main_6(self):
        self.logger.info("点击版本查询菜单")
        self.element_click(role_Mgmt.roleMgmt_download_devOper_datacollector_6)
        self.logger.info("返回版本查询页面")
        self.element_find(role_Mgmt.roleMgmt_Signal_correlation_main)

