import unittest
import ddt
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Day4.readCsv2 import read


# shift+tab可以缩进4个空格;tab键是前进4个空格
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    member_info = read("member_info.csv")
    global driver

    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法执行之前,只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(
            Keys.ENTER).perform()
    # python中集合前面的*号表示把集合中的所有元素拆开,一个一个写;就是把一个列表拆成两个string
    @ddt.data(*member_info)  # 测试数据的来源实现方法,来源于read()方法
    def test_b_add_member(self, row):
        # 每组测试数据都是一条测试用例,每条测试用例都是独立的,不会因为上一条测试用例执行失败就会导致下一条数据不能被正常执行
        # 用ddt装饰器,去修饰这个方法,达到每条测试用例独立执行的目的
        # ddt是数据驱动的意思
        # print("添加会员")
        driver = self.driver
        # for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        # driver.find_element_by_css_selector("[value'{0}']".format(row[2])).click
        driver.find_element_by_css_selector("[name='sex'][value='" + row[2] + "']").click()  # "+变量+"可以实现字符串的获取

        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        # 切换到父框架
        # driver.switch_to.parent_frame()

        # actual:实际结果,是执行测试用例之后,页面上实际显示的结果;
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        # expected:期望结果,来自于需求文档或者测试用例.配置文件
        expected = row[0]
        # 添加断言:用assert,是框架提供的,调用断言需要加self.
        self.assertEqual(actual, expected)
        # 切换到网页的根节点
        driver.switch_to.default_content()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
