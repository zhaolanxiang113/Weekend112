import unittest
from selenium import webdriver

import time


class MemberManageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        # driver.maximize_window()
    def tearDown(self):
        time.sleep(20) # 正式运行的时候去掉时间等待
        self.driver.quit() #driver要声明在setup之内
    def test_add_member(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("testing04")
        driver.find_element_by_name("mobile_phone").send_keys("13599789990")
        driver.find_element_by_css_selector("[name='sex'][value='1']").click()
        # driver.find_element_by_css_selector("body > div.content > div.install.mt10 > dl > dd > div > div > dl > form > dd > ul > li:nth-child(3) > b").click()
        driver.find_element_by_id("birthday").send_keys("1996-06-08")
        driver.find_element_by_name("email").send_keys("test02@163.com")
        driver.find_element_by_name("qq").send_keys("1584565887")
        driver.find_element_by_class_name("button_search").click()



