import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self): # 在测试前执行。setUp()方法尝试创建一个测试环境，类似运行中的程序。
        self.app = create_app('testing') # 首先，使用测试配置创建爱你程序
        self.app_context = self.app.app_context() # 然后，激活上下文，确保在测试中使用current_app()
        self.app_context.push() # 提交新的上下文请求
        db.create_all() # 创建一个全新的数据库，以备不时之需

    def tearDown(self): # 在测试后进行
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self): # 以test_开头的函数都是作为测试执行。test_app_exists确保程序实例存在
        self.assertFalse(current_app is None)

    def test_app_is_testing(self): # 确保程序在测试配置中运行。
        self.assertTrue(current_app.config['TESTING'])

    # 若想把tests文讲夹当作包使用，则需要添加tests/__init__.py文件，不过这个文件可以为空，因为unittest包会扫描所有模块并查找测试。

