import os
import smtplib
import unittest
# HTMLTestRunner是基于unittest框架的一个扩展,是python3的;
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
   f = open(path, 'rb')
   mail_body = f.read() # 读取html二进制文件,作为邮件的正文
   f.close()

   # 将二进制的内容转成普通格式:MIME(是对邮件协议的扩展,使邮件不仅支持文本还支持多媒体等多种格式:图片 音频)
   # msg是字典的意思;他是无序的
   msg = MIMEText(mail_body, 'html', 'utf-8')
   # 设置邮件主题
   msg['Subject'] = Header("自动化测试报告",'utf-8')
   # 用客户端软件或者自己写代码登录邮箱,很多类型的邮件,需要单独设置一个客户端授权码
   msg['From'] = 'bwftest126@126.com'
   msg['To'] = '1691846400@qq.com'
   # 发邮件
   # 1.链接邮箱服务器,登录邮箱页面
   # 链接服务器之前,首先弄清除网络传输协议的类型
   # 发邮件的协议一般有三种,首先查看邮箱支持那种协议:pop3.smtp.imap
   # 选择一种传输协议
   # 首先导入smtplib库
   smtp = smtplib.SMTP() # 实例化了一个SMTP对象
   smtp.connect("smtp.126.com") # 链接126邮箱服务器的地址

   # 2.登录邮箱
   smtp.login('bwftest126@126.com','abc123asd654')
   # 3.发送邮件
   smtp.sendmail('bwftest126@126.com', '1691846400@qq.com', msg.as_string())
   # 4.退出邮件
   smtp.quit()
   print("email has sent out!")

if __name__ == '__main__':
    # 写个时间戳
    # str 是String  f是format格式
    # strftime()通过这个方法定义时间的格式
    # Y year是年,m 是月,d 是日,H 是 hour小时.M minute分,S second 秒
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./Day5','*Test.py')
    # HTMLTestRunner():用html测试用例运行器
    # html测试用例运行器最终生成一个html格式的测试报告
    # 指定路径存放测试报告
    # 创建一个文件
    base_path = os.path.dirname(__file__)  # 固定格式
    path = base_path + "/report/report" + now + ".html"
    file = open(path, 'wb')

    HTMLTestRunner(stream=file, title="海盗商城的测试报告", description="测试环境:Window Server 2008 + Chrome").run(suite)
    file.close()
    # 此时生成的测试报告只显示了包名.类名和方法名,只能给专业人士看,我们应该把相关的手动测试用例的标题加到测试报告里
    # 自动化测试用例是从手工测试用例挑选出来的,只需将手工测试用例转化成代码的形式生成测试报告
    # 加一个时间戳,按照当前时间计算一个数字,把数字作为文件名的一部分,用于区分每次运行的测试报告,避免文件名重复;
    # 将生成的html格式的报告生成一封提醒邮件
    # 把html文件作为邮件正文,发邮件
    send_mail(path)
