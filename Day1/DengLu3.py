# javascript在python中的使用
from select import select

from selenium import webdriver
driver =webdriver.Chrome()
driver.get("http://localhost/")
js ='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("testing01")
driver.find_element_by_id("password").send_keys("testing1234")
driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_css_selector("#add-new-address > div:nth-child(1) > input").send_keys("陆毅")
driver.find_element_by_css_selector("#add-new-address > div:nth-child(2) > input").send_keys("13666666666")
sheng =driver.find_element_by_id("add-new-area-select")
select(sheng).select_by_value('230000')
shi =driver.find_elements_by_tag_name("select")[1]
select(shi).select_by_index(2)
quxian =driver.find_elements_by_id("linkagesel_221442")
select(quxian).select_by_tag_name("select")[2]
select(quxian).select_by_index(2)

