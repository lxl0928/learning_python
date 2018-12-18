#! /usr/bin/env python3 
# coding: utf-8

class MyClass(object):
    """ 本例中的__init__将实例成员参数设置为私有形式，不影响在类本身的其他成员函数中访问这些变量。如：析构函数中访问
        但在类之外的代码无法访问私有成员。
    """
    def show(self):
        print("name: {0}".format(self.__name))
        print("color: {0}".format(self.__color))

    def __init__(self, name="unset", color="black"):
        """ Python使用制定变量名格式的方法定义私有成员，即所有双下划线“__”开始命名的成员都为私有成员
        """
        print("Constructor && __init__ is called with params: {0}, {1}".format(name, color))
        self.__name = name
        self.__color = color

    def __del__(self):
        print("Destructor is called for {0}.".format(self.__name))

print("-----------------------\n")
inst = MyClass("Jojo", "White")
inst.show()

del inst

print("-----------------------\n")
inst = MyClass()
print("inst.__name: {0}".format(inst.__name)) # 在类之外的代码无法访问私有成员
del inst
print("-----------------------\n")
