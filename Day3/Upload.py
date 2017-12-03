from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(30)
# 1.登录
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
# 2.商品管理
driver.find_element_by_link_text("商品管理").click()
time.sleep(5)
# 3.添加商品
driver.find_element_by_link_text("添加商品").click()
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone x")

# 5.商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click() # 第一种实现方法:点击6,在点击7
# 双击的操作实现方法,适用于所有特殊元素操作:ActionChains类
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 第二种实现方法
# driver.find_element_by_id("jiafen").click()
# 6.商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_value('1')
# 7.点击商品图册
driver.find_element_by_link_text("商品图册").click()
# driver.find_element_by_css_selector("rt_rt_1bvor7t99g7d1nr9unk5pe1sgg8")
driver.find_element_by_name("file").send_keys("D:/TU/baby.jpg")
# 输入图片路径
# driver.find_element_by_name("file").send_keys("D:/TU/1.jpg")
# 对滚动条的处理,用于窗口未最大化,点击不到按钮的时候
ac = ActionChains(driver)
for i in range(10):
    ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# 8.确定弹框
time.sleep(3)
driver.switch_to.alert.accept()
# 窗口没有最大化会报错,将窗口最大化就可以了或者加上滚动条的处理
driver.find_element_by_class_name("button_search").click()


