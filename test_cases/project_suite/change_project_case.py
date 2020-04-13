import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver,login

class ChangeProjectCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
    def test_change_project(self):
        ''' 切换项目'''
        login.login(self.driver, username='test01', password='newdream123')
        self.driver.find_element(By.XPATH, '//a[text()="项目"]').click()
        self.driver.find_element(By.XPATH, '//button[@data-toggle="dropdown"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//a[text()=" 项目主页"]').click()
        self.driver.find_element(By.XPATH, '//button[@id="currentItem"]').click()
        self.driver.find_element(By.XPATH, '//a[@title="湖南中医药测试实训"]').click()
        time.sleep(1)
        self.assertTrue(EC.title_is("湖南中医药测试实训::任务列表 - 禅道"))

if __name__=='__main__':
    unittest.main()