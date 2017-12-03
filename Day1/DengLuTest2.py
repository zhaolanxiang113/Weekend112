from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
cwh =driver.current_window_handle
whs =driver.window_handles
# item表示集合中的一个元素
for item in whs:
    if item ==cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
# 3.输入用户名和密码
driver.find_element_by_id("username").send_keys("testing01")
# 4.点击登陆按钮