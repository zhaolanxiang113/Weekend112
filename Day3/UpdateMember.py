# 1. 登录
from selenium import webdriver

# from selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("testing")
ActionChains(driver).send_keys(Keys.TAB).send_keys("testing123").send_keys(Keys.ENTER).perform()
# 2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
# 3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
# 4a.修改个人信息
driver.find_element_by_id("true_name").clear()# 清空原来的内容
driver.find_element_by_id("true_name").send_keys("测试")
# 4b.修改性别
driver.find_element_by_css_selector("#xb[value='1']").click() # "#xb"是他们共同的id
# 4c.生日
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
# driver.execute_script("return document.getElementById('date')")跟date = driver.find_element_by_id("date").click()效果一样
date.clear()
date.send_keys("1990-11-12")
# 5.QQ号
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1671746400")
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
# 6.弹框的处理
# 首先切换窗口,定位到弹出框的窗口,用alert方法处理
driver.switch_to.alert.accept() #accept是确定按钮的意思;







