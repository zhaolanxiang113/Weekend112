import unittest


if __name__ == '__main__':
    # defaultTestLoader默认的测试用例加载器,用于寻找符合一定规则的测试用例
    # discover 发现 ".表示当前路径'"*表示所有的测试用例"
    # suite表示一组测试用例,可以随便起名字
    suite = unittest.defaultTestLoader.discover('./Day5', pattern='*Test.py')
    # 执行suit中的所有测试用例
    # TextTestRunner 文本的测试用例运行器.后面加()将TextTestRunner 这个类实例化对象,才能调用测试方法,python中实例化不需要new关键字,直接在类后面加一对小括号就行;
    unittest.TextTestRunner().run(suite)