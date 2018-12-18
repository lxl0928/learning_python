#! /usr/bin/env python3
# coding: utf-8 

class MyClass(object):
    """析构函数是构造函数的反函数，在销毁或者释放对象时将调用他们。析构函数往往用来作清理善后工作
    """
    message = "Hello, Developer."

    def show(self):
        print(self.message)

    def __init__(self, name="unset", color="black"):
        print("Constructors && __init__ is called with params: {0}, {1}.".format(name, color))

    def __del__(self):
        """ 析构函数: 
            与Java类似，Python解释器的堆中存储着正在运行的应用程序所建立的所有对象，
            但是它们不需要程序代码显示的来释放，因为Python解释器会自动跟踪它们的引用计数，
            并自动销毁（同时调用析构函数）已经没有被任何变量引用的对象。
            在这种场景中，开发者并不知道对象的析构函数在何时被调用。
        """
        print("Destructor is called!")

inst = MyClass()
inst.show()

inst1 = MyClass("David")
inst1.show()

del inst, inst1 # Python提供显示销毁对象的方法: del关键字，用del释放对象时，析构函数会被自动调用。

inst2 = MyClass("Lisa", "Yellow")
inst2.show()

del inst2

