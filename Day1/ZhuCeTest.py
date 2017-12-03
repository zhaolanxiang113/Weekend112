# 1.打开浏览器
from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("testing01")
driver.find_element_by_name("password").send_keys("testing1234")
driver.find_element_by_name("userpassword2").send_keys("testing1234")
driver.find_element_by_name("mobile_phone").send_keys("13677777777")
driver.find_element_by_name("email").send_keys("yangyang@163.com")
driver.find_element_by_class_name("reg_btn").click()


