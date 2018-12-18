#! /usr/bin/env python3 
# coding: utf-8 

class Base(object):
    """ 类之间的继承是面向对象设计的重要方法，通过继承可以达到简化代码和优化设计模式的目的
        Python类在定义时可以在小括号中指定基类，所有Python类都是object类型的子类。
        子类除了具备自己的Block_class中定义的特性，还从父类的非私有特性。
    """
    def __init__(self):
        """ 构造函数
        """
        print("Constructor && __init__ is called!-------In Class Base()")

    def __del__(self):
        """ 析构函数
        """
        print("Destructor is called!-------In Class Base()")

    def move(self):
        """ 成员函数
        """
        print("move called!------In Class Base()")

class SubA(Base):
    def __init__(self):
        """ 继承自Base类，定义重载了构造函数
        """
        print("Constructor && __init__ is called!-------In Class SubA")

    def move(self):
        """ 继承自Base类，定义重载了成员函数
        """
        print("move called!------In Class SubA")

class SubB(Base):
    def __del__(self):
        """ 继承自Base，定义、重载了自己的析构函数
        """
        print("Desctructor is called!-------In Class SubB")
        super(SubB, self).__del__() # 用super关键字调用基类的析构函数__del__(): super(SubClassName, self)，最佳实践，这样做可以让父类资源如期释放

print("instA 调用了子类SubA自己的构造函数和move()方法，但因为SubA()没有重载析构函数，所以对象销毁时系统调用了基类Base的析构函数")
instA = SubA()
instA.move()
del instA

print("\n------------------\n")

print("子类SubB只重载了析构函数，所以instB调用了基类的构造函数和move()方法，在对象销毁时调用了SubB()自己的析构函数，并用super关键字引用了基类的析构函数。")
instB = SubB()
instB.move()
del instB

print("\n------------------\n")
print("move()方法在instA和instB调用时分别展现了不同的行为，这种现象是多态")
