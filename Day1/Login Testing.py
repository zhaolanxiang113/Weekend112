# 1.打开浏览器
from selenium import webdriver

# 从selenium中导入网络驱动的意思，用代码操作浏览的器
# 1.第一个python语言不需要加冒号
# 2.第二个Chrom后面一定要有括号
# 3. 第三个字体的问题：

driver =webdriver.Chrome()
# 2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 3.输入用户名，首先寻找用户名的输入框
driver.find_element_by_id("username").send_keys("testing")
# 4.输入密码
driver.find_element_by_id("password").send_keys("testing123")
# 5.点击登陆按钮
driver.find_element_by_class_name("login_btn").click()
