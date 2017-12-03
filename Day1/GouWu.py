import time
from select import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
cwh = driver.current_window_handle
whs = driver.window_handles
# item表示集合中的一个元素
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("username").send_keys("testing")
driver.find_element_by_id("password").send_keys("testing123")
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
time.sleep(5)
#iphone_img ='body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img'
driver.find_element_by_css_selector("body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img").click()
cwh = driver.current_window_handle
whs = driver.window_handles
# item表示集合中的一个元素
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
time.sleep(5)
driver.find_element_by_id("joinCarButton").click()
time.sleep(5)
driver.find_element_by_class_name("shopCar_T_span3").click()
time.sleep(5)
driver.find_element_by_class_name("shopCar_btn_03").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)
driver.find_element_by_css_selector("#add-new-address > div:nth-child(1) > input").send_keys("陆毅")
driver.find_element_by_css_selector("#add-new-address > div:nth-child(2) > input").send_keys("13666666666")
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value('230000')
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
quxian = driver.find_elements_by_tag_name("select")[2]
Select(quxian).select_by_visible_text("建华区")






