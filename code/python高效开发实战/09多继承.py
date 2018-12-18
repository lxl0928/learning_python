#! /usr/bin/env python3 
# coding: utf-8

class BaseA(object):
    def move(self):
        print("move called in BaseA")

class BaseB(object):
    def move(self):
        print("move called in BaseB")

class SubC(BaseA):
    def move(self):
        print("move called in SubC")

class SubD(SubC, BaseB):
    pass

print("该段代码定义了两个基类: BaseA, BaseB, 两个基类中都定义了move()方法。\n SubC继承自BaseA并且重载了move()函数。\nSubD继承自SubC和BaseB,并且没有定义自己的成员。")
print("\n--------------------------\n")
inst = SubD()
inst.move()
del inst
print("\n--------------------------\n")

print("当子类SubD继承多个父类时, 并且调用一个在几个父类中共有的成员函数move()时，Python解释器会选择距离子类SubD最近的一个基类SubC的成员方法")
print("本例中SubD继承自SubC, 则搜索顺序是: SubD, SubC, BaseA, BaseB。 所以选择了SubC")

print("\n--------------------------\n")

print("在设计多父类继承时，尽量避免多个父类中定义同名成员，实在无可避免，也要注意子类定义中引用父类的顺序。")
