#! /usr/bin/env python3 
# coding: utf-8 

class MyClass(object):
    """测试类的基本使用

    """
    message = "Hello, developer!"   # 类的成员变量

    def show(self):                 # 类的成员函数
        print(self.message)

print(MyClass.message)              # 通过类名读取成员变量，通过MyClass.show()调用会报错：缺少self参数
MyClass.message = "Hello, tester!"  # 修改成员变量
MyClass.show(MyClass)               # 通过类名调用成员函数需将类的名字作为参数传入

print("------------")

instance1 = MyClass()               # 实例化一个MyClass对象，__new__实例化对象，__init__初始化成员变量
instance1.show()                    # 实例化对象调用成员函数，无需传入self参数。
