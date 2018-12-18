#! /usr/bin/env python3 
# coding: utf-8

class MyClass(object):
    
    message = "Hello, Developer!"

    def show(self):
        print("message: {0}".format(self.message))
        print("Here is {0} in {1}.".format(self.name, self.color))

    @staticmethod
    def printMessage():
        """ 静态函数，可以访问类成员message，通过类名MyClass.printMessage()调用
        """
        print("printMessage is called")
        print("MyClass.message: {0}".format(MyClass.message))

    @classmethod
    def createObj(cls, name, color):
        """ 类方法createObj()
            params:
                cls: 类方法定义中的第一个参数必须为隐形参数cls, 
                     在createObj()中可以通过cls替代类名本身。
                     在本例中createObj建立并返回一个Myclass的实例。
                name: string
                color: string
            example:
                inst = MyClass.createObj("name", "color")
        """
        print("Object will be created: {0}({1}, {2})".format(cls.__name__, name, color))
        return cls(name, color)

    def __init__(self, name="unset", color="black"):
        print("Constructor && __init__ is called with params: {0}, {1}".format(name, color))
        self.name = name
        self.color = color

    def __del__(self):
        print("Destructor is called")

MyClass.printMessage()

print("\n---------------\n")

inst = MyClass.createObj("Toby", "Red")
print("inst.message: {0}.".format(inst.message))

print("\n---------------\n")

inst1 = MyClass.createObj("Timilong", "Green")
print("inst1.message: {0}.".format(inst1.message))

print("\n---------------\n")

del inst, inst1
