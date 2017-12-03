import unittest
from selenium import webdriver

import time
# 这个测试的目的:封装到一个单独的类和方法中,便于调用;

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器升级后,要注销最大化;要想使用必须满足浏览器的版本和driver的版本必须匹配
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()