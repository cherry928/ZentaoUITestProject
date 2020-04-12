import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner

current_path = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current_path, '../../webdriver/chromedriver')

class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:  # 把selenium的配置项初始化
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')

    def tearDown(self) -> None:
        time.sleep(2)

    def test_login_01(self):
        '''test01进行登录'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        # actual_reslut = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # self.assertEqual(actual_reslut, '测试人员1', 'test_login执行失败')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'), '测试人员1')) # EC 断言

    def test_login_02(self):
        '''test02进行登录'''
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test02')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        actual_reslut = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_reslut, '测试人员2', 'test_login执行失败')

if  __name__=='__main__':
    suite01 = unittest.TestSuite(unittest.makeSuite(LoginSuccessCase))
    now_time = time.strftime('%y_%m_%d_%H_%M_%S')
    file = open('result_%s.html' % now_time, 'wb')
    html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                                title='newdream测试',
                                                description='测试描述')
    html_runner.run(suite01)