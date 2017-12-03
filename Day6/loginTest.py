from selenium import webdriver


import time
from Day6.page_object.personCenterPage import PersonalCenterPage
from Day5.MyTestCase import MyTestCase
from Day6.page_object.loginPage import LoginPage


class LoginTest(MyTestCase):
    def test_login(self):
        # 1.打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")

        Ip = LoginPage(self.driver)
        Ip.open()
        #2.输入用户名

        # self.driver.find_element(By.ID, "username").send_keys("testing")
        Ip.input_username("testing")
        #3.输入密码
        # self.driver.find_element(By.ID, "password").send_keys("testing123")
        Ip.input_password("testing123")
        #4.点击登录按钮
        # self.driver.find_element(By.CLASS_NAME, "login_btn").click()
        Ip.click_login_button()
        #5.验证是否跳转到管理中心页面
        # expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"

        # self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title, self.driver.title)



