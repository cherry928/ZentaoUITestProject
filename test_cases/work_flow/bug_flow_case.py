import time
import unittest
from common import login,set_driver
from common.config_utils import config
from common.create_bug import create_bug
from common.confirm_bug import confirm_bug
from common.fix_bug import fix_bug
from common.close_bug import close_bug

class BugFlowCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()
    def test_bug_flow_01(self):
        '''A用户登录禅道提交bug'''
        login.login(self.driver, username='test01', password='newdream123')
        create_bug(self.driver, title=config.get_title_path)
    def test_bug_flow_02(self):
        '''B用户登录禅道--把bug进行确认操作 -- 然后指派bug给开发人员'''
        login.login(self.driver, username='test', password='newdream123')
        confirm_bug(self.driver, title=config.get_title_path)
    def test_bug_flow_03(self):
        '''C开发人员登录 -- 把bug状态改为已解决'''
        login.login(self.driver, username='dev01', password='newdream123')
        self.driver.refresh()
        fix_bug(self.driver, title=config.get_title_path)
    def test_bug_flow_04(self):
        '''A用户登录 -- 把bug状态改为已关闭'''
        login.login(self.driver, username='test01', password='newdream123')
        self.driver.refresh()
        close_bug(self.driver, title=config.get_title_path)

if __name__=='__main__':
    unittest.main()