import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner
from selenium.webdriver.support.wait import WebDriverWait

current_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current_path, '../../webdriver/chromedriver')

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的配置项初始化
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self) -> None:
        time.sleep(2)

    def test_my_link(self):
        '''登录后查看页面title'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

if  __name__=='__main__':
    unittest.main()