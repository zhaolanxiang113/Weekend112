import time
from select import select

from selenium import webdriver
# 45版本一下的firefox浏览器,不需要驱动文件
# 46版本以上的friefox浏览器,也需要把driver.exe文件放在
# driver =webdriver.firefox()
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)  # 设置默认最大等待时间后,以后的代码自动执行
# driver.maximize_window()  # 窗口最大化,设置默认最大等待时间后,以后的代码自动执行
driver.get("http://localhost/")
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link) # 删除跳转页面的方法,其中login_link是对应参数的个数0
login_link.click()
driver.find_element_by_id("username").send_keys("testing")
driver.find_element_by_id("password").send_keys("testing123")
driver.find_element_by_id("username").submit() # 不建议使用该方法
# time.sleep(5)  # Alt加回车可以添加import time
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# iphone_img ="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > qdiv.shop_01-imgbox > a > img"
# iphone_img ="div.shop_01-imgbox > a > img" #将上面的代码优化,删除多余的代码,简化代码,运行快;编码变动不影响,可维护性好
iphone_link ="div.shop_01-imgbox > a"
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
driver.find_element_by_id("joinCarButton").click()
time.sleep(5)
driver.find_element_by_class_name("shopCar_T_span3").click()
time.sleep(5)
driver.find_element_by_class_name("shopCar_btn_03").click()
driver.find_element_by_class_name("add-address").click()
# 输入收货人信息
driver.find_element_by_css_selector("#add-new-address > div:nth-child(1) > input").send_keys("陆毅")
driver.find_element_by_css_selector("#add-new-address > div:nth-child(2) > input").send_keys("13666666666")
# 选择地区
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value('230000')
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
quxian = driver.find_elements_by_tag_name("select")[2]
Select(quxian).select_by_visible_text("建华区") #第二种实现的方法
# Select(shi).select_by_index(3)
# 选择地区,第二种方法:
# driver.find_element_by_css_selector("[value='230000']").click()
# driver.find_element_by_css_selector("[value='230100']").click()
# driver.find_element_by_css_selector("[value='230106']").click()
driver.find_element_by_name("address[address]").send_keys("香坊路1号")
driver.find_element_by_name("address[zipcode]").send_keys("100000")
driver.find_element_by_class_name("aui_state_highlight").click()
