import time

from selenium import webdriver
import pytest
import page.Login
from utils.driver_utils import GetDriver
from config import BASE_PATH
import os

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            """file_name = report.nodeid.replace("::", "_") + ".png"
            """
            filename = (
                    time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())) + "_pytest" + ".png"
            )
            image = BASE_PATH + os.sep + 'image' + os.sep + filename
            _capture_screenshot(image)
            if image:
                html = '<div><img src="%s" alt = "screenshot" style ="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % image
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    GetDriver.get_web_driver(page.Login.url_vstudio).get_screenshot_as_file(name)


