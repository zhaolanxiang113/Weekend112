import unittest

import time

from Day5.MyTestCase import MyTestCase
from Day6.data_base.connectDB import connectDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("testing02")
        driver.find_element_by_name("password").send_keys("testing12345")
        driver.find_element_by_name("userpassword2").send_keys("testing12345")
        driver.find_element_by_name("mobile_phone").send_keys("13677777776")
        driver.find_element_by_name("email").send_keys("yangyange@163.com")
        driver.find_element_by_class_name("reg_btn").click()
        # 检查数据库中新增的用户名和我们新注册的用户名是否一致
        expected = "testing02"
        time.sleep(3)
        actual = connectDb()[1]
        self.assertEqual(expected, actual)
        print(connectDb()[1])