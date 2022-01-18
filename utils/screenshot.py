import os
from config import BASE_PATH

def insert_img(driver, file_name):
    file_path = BASE_PATH + os.sep + "image" + os.sep + file_name
    return driver.get_screenshot_as_file(file_path)