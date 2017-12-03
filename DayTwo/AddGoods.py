# 1.登陆
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
# 2.商品管理
driver.find_element_by_link_text("商品管理").click()

# 3.添加商品
driver.find_element_by_link_text("添加商品").click()
# 4.商品名称
# 左边有一个导航条的处理方法
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
# 7.提交
driver.find_element_by_class_name("button_search").click()