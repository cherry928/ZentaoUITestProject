import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
    def test_login_01(self):
        '''test01进行登录'''
        login.login(self.driver, username='test01', password='newdream123')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'), '测试人员1')) # EC 断言
    def test_login_02(self):
        '''test02进行登录'''
        login.login(self.driver, username='test02', password='newdream123')
        self.driver.refresh()
        actual_reslut = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_reslut, '测试人员2', 'test_login执行失败')

if  __name__=='__main__':
    unittest.main()