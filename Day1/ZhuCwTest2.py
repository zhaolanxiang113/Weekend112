from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("注册").click()
# 窗口切换：把selenium切换到新的窗口工作
cwh =driver.current_window_handle  #浏览器当前窗口的句柄，是一个属性
whs =driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)

driver.find_element_by_name("username").send_keys("testing02")
