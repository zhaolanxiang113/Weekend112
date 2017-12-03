# 测试框架:组织和执行测试用例
# 1.导入unittest框架
import unittest
# TestCase是测试用例;即在UnittestDemo中编写测试用例
class UnittestDemo(unittest.TestCase):
    # def是方法的关键字
    def setUp(self):
        print("这个方法将会在测试用例执行之前先执行")

    def tearDown(self):
        print("这个方法将会在测试用例执行完毕后执行")

# 编写测试用例方法
    # 只有以test开头命名的方法才是测试用例方法,才能直接运行;
    # 其他的普通方法不能直接运行,只有被调用才能执行
    def test_log_in(self):
        print("登录测试用例")
        self.zhu_ce() # 被调用后才能运行

    def zhu_ce(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")

if __name__ == '__main__': # 直接执行该文件,则下面的代码执行,否则执行其他文件时,不执行该代码


   #  unittest.main() # 执行当前文件中所有unnittest的测试用例

     UnittestDemo().zhu_ce()

