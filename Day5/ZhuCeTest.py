# 有了MyTestCase以后,在写测试用例 就不需要重写setup和teardown方法
import os
from selenium import webdriver

from Day5.MyTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    # 因为MyTestCase已经实现了setup和teardown方法,所以我们以后在写测试用例就不需要在重新实现setup和teardown方法;

    """注册模块测试用例"""
    def test_zhu_ce(self):
         """打开注册页面的测试用例"""
         driver = self.driver
         driver.get("http://localhost/index.php?m=user&c=public&a=reg")
         # driver.current_url # 用来获取当前浏览器的网址
         actual = driver.title # 用来获取当前浏览器中的标签页的title
         expected = "用户注册 - 道e坊商城 - Powered by Haidao"
         base_path = os.path.dirname(__file__)
         path = base_path.replace('Day5','report/image/') # 把第5天替换成这个图片
         # get_screenshot_as_file截取浏览器的图片
         # findElement().get_attribute("value") 获取页面元素的属性值
         driver.get_screenshot_as_file(path + "zhuce.png")
         self.assertEqual(actual,expected)



