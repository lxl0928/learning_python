#! /usr/bin/env python3 
# coding: utf-8

class MyClass(object):
    """构造函数是一种特殊的类成员方法，主要用来创建对象时初始化对象，即为对象成员变量赋初始值。
    """
    message = "Hello, developer"

    def show(self):
        """类的成员函数
        """
        print(self.message)

    def __init__(self):
        """__init__()并不是真正意义上的构造方法
           __init__()方法所做的工作是在类的对象创建好后进行变量的初始化。
           __new__()方法才会真正创建实例，是类的构造方法
           __init__()是实例方法，__new__()是静态方法。不需要显示的返回，默认为None，否则会在运行时输出TypeError
           __new__()方法一般需要返回类的对象，当返回类的对象时将会自动调用__init__()方法进行初始化。
                    如果没有对象返回，则__init__()方法不会被调用。
          
        """
        print("Constructor && __init__ is called")

inst = MyClass()
inst.show()

print("--------------------")

class MyClass1(object):
    """实现多种方式构造对象，则可通过默认参数的方式实现
    """
    message = "Hello, MyClass1"

    def show(self):
        print(self.message)

    def __init__(self, name="unset", color="black"):
        print("__init__ is called with params:{0}, {1}".format(name, color))

inst0 = MyClass1()
inst0.show()

inst1 = MyClass1("David")
inst1.show()

inst2 = MyClass1("Lisa", "Yellow")
inst2.show()

inst3 = MyClass1(color="Green")
inst3.show()


