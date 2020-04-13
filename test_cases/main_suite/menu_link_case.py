import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
    def test_my_link(self):
        '''登录后查看页面title'''
        login.login(self.driver, username='test01', password='newdream123')
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

if  __name__=='__main__':
    unittest.main()