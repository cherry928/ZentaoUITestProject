# 每次在setUp都需要编写驱动代码 可以放到common模块 作为公共函数
import os
from selenium import webdriver

def set_driver():
    current_path = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current_path, '../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    return driver