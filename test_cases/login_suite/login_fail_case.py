import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
from common import login

class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的配置项初始化
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
    def test_login(self):
        '''用户登录失败'''
        login.login(self.driver, username='test100', password='newdream123')
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))

if  __name__=='__main__':
    unittest.main()