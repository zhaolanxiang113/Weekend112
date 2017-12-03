import unittest
from selenium import webdriver

import time


class DengLuTest(unittest.TestCase):
    # 3个双引号表示文档字符串,也是一种注释,会显示的文档中;
    """登录模块测试用例"""

    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器升级后,要注销最大化;要想使用必须满足浏览器的版本和driver的版本必须匹配
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("testing")
        driver.find_element_by_id("password").send_keys("testing123")
        driver.find_element_by_class_name("login_btn").click()
        print("当前用户名:testing")



