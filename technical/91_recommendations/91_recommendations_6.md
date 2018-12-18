## 编写高质量代码(改善Python程序的91个建议)_6: 内部机制

[TOC]

### 54. 理解built-in object

python中一切皆对象: 字符是对象，列表是对象，内建类型(build-in type)是对象， 用户定义的类型是对象，object是对象，type是对象。

### 55. __init__()不是构造方法

__new__()方法才是类的构造方法，而__init__()不是。

1）__init__并不相当于C#中的构造函数，执行它的时候，实例已构造出来了。
```
class A(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return 'A '+self.name
```


当我们执行:
```
a=A('hello')
```
时，可以理解为:
```
a=object.__new__(A)
A.__init__(a,'hello')
```

即__init__作用是初始化已实例化后的对象。

2) 子类可以不重写__init__，实例化子类时，会自动调用超类中已定义的__init__
```
class B(A):
    def getName(self):
        return 'B '+self.name
 
if __name__=='__main__':
    b=B('hello')
    print b.getName()
```
但如果重写了__init__，实例化子类时，则不会隐式的再去调用超类中已定义的__init__:
```
class C(A):
    def __init__(self):
        pass
    def getName(self):
        return 'C '+self.name
 
if __name__=='__main__':
    c=C()
    print c.getName()
```
则会报"AttributeError: 'C' object has no attribute 'name'”错误，所以如果重写了__init__，为了能使用或扩展超类中的行为，最好显式的调用超类的__init__方法:
```
class C(A):
    def __init__(self,name):
        super(C,self).__init__(name)
    def getName(self):
        return 'C '+self.name
 
if __name__=='__main__':
    c=C('hello')    
    print c.getName()
```


### 56. 理解名字查找机制

名字空间:

Python 的名字空间是 Python 一个非常核心的内容。
其他语言中如 C 中，变量名是内存地址的别名，而在 Python 中，名字是一个字符串对象，它与他指向的对象构成一个{name:object}关联。
Python 由很多名字空间，而 LEGB 则是名字空间的一种查找规则。

作用域:

Python 中name-object的关联存储在不同的作用域中，各个不同的作用域是相互独立的。而我们就在不同的作用域中搜索name-object。

举个例子，来说明作用域是相互独立的。
```
>>> i= "G"
>>> 
>>> def test():
...     i = "L"
...     print(i+"in locals")

>>> test()
L in locals

>>> print(i+"in globals")
G in globals
```

在上面的例子中，定义了两次 i，在 test 函数中是 i-L,在外面是 i-G。为什么在 test 函数中，我们 i 指向的是对象 L，而在外面，i 指向的则是 G？这就是 LEGB 的作用。

简而言之，LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
```
   1. locals 是函数内的名字空间，包括局部变量和形参
   2. enclosing 外部嵌套函数的名字空间（闭包中常见）
   3. globals 全局变量，函数定义所在模块的名字空间
   4. builtins 内置模块的名字空间
```
所以，在 Python 中检索一个变量的时候，优先回到 locals 里面来检索，检索不到的情况下会检索 enclosing ，enclosing 没有则到 globals 全局变量里面检索，最后是到 builtins 里面来检索。


### 57. 为什么需要self参数

Python要self的理由

Python的类的方法和普通的函数有一个很明显的区别，在类的方法必须有个额外的第一个参数 (self )，但在调用这个方法的时候不必为这个参数赋值 （显胜于隐 的引发）。Python的类的方法的这个特别的参数指代的是对象本身，而按照Python的惯例，它用self来表示。（当然我们也可以用其他任何名称来代替，只是规范和标准在那建议我们一致使用self）


为何Python给self赋值而你不必给self赋值？

例子说明：创建了一个类MyClass，实例化MyClass得到了MyObject这个对象，然后调用这个对象的方法MyObject.method(arg1,arg2) ，这个过程中，Python会自动转为Myclass.mehod(MyObject,arg1,arg2)
这就是Python的self的原理了。即使你的类的方法不需要任何参数，但还是得给这个方法定义一个self参数，虽然我们在实例化调用的时候不用理会这个参数不用给它赋值。

实例：
```
class Python:
    def selfDemo(self):
        print 'Python,why self?'
p = Python()
p.selfDemo()
```

输出:
```
Python,why self?
```

把p.selfDemo()带个参数如：p.selfDemo(p)，得到同样的输出结果

如果把self去掉的话:
```
class Python:
    def selfDemo():
        print 'Python,why self?'
p = Python()
p.selfDemo()
```
这样就报错了：
```
TypeError: selfDemo() takes no arguments (1 given)
```

扩展

self在Python里不是关键字。self代表当前对象的地址。self能避免非限定调用造成的全局变量。


### 58. 理解MRO与多继承

python中使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承，也叫菱形继承问题）等.

MRO

MRO即method resolution order，用于判断子类调用的属性来自于哪个父类。在Python2.3之前，MRO是基于深度优先算法的，自2.3开始使用C3算法，定义类时需要继承object，这样的类称为新式类，否则为旧式类

![MRO](http://7xorah.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE20161101160703.png)

从图中可以看出，旧式类查找属性时是深度优先搜索，新式类则是广度优先搜索C3算法最早被提出是用于Lisp的，应用在Python中是为了解决原来基于深度优先搜索算法不满足本地优先级，和单调性的问题。
```
本地优先级：
指声明时父类的顺序，比如C(A,B)，如果访问C类对象属性时，应该根据声明顺序，优先查找A类，然后再查找B类。

单调性：
如果在C的解析顺序中，A排在B的前面，那么在C的所有子类里，也必须满足这个顺序
```
看下面的例子:
```
class X(object):
    def f(self):
        print 'x'


class A(X):
    def f(self):
        print 'a'

    def extral(self):
        print 'extral a'


class B(X):
    def f(self):
        print 'b'

    def extral(self):
        print 'extral b'


class C(A, B, X):
    def f(self):
        super(C, self).f()
        print 'c'


print C.mro()

c = C()
c.f()
c.extral()
```

根据广度搜索原则最先搜索到A，所以结果很明显，如下所示:

![结果](http://7xorah.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE20161101161015.png)

类C没有extral函数，调用的是子类的该函数。这种类的部分行为由父类来提供的行为，叫做抽象超类.

关于super

从mro就能知道，super指的是 MRO 中的下一个类，而不是父类。super所做的事如下面代码所示：
```
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```

对于在子类中调用父类方法，要么直接使用父类名来调用方法，要么在子类中用super，保持一致，最好不要混用


### 59. 理解描述符机制

简介

Python 2.2 引进了 Python 描述符，同时还引进了一些新的样式类，但是它们并没有得到广泛使用。Python 描述符是一种创建托管属性的方法。除了其他优点外，托管属性还用于保护属性不受修改，或自动更新某个依赖属性的值。

描述符增加了对 Python 的理解，改善了编码技能。本文介绍了描述符协议，并演示了如何创建和使用描述符。

描述符协议

Python 描述符协议 只是一种在模型中引用属性时指定将要发生事件的方法。它允许编程人员轻松、有效地管理属性访问：
```
set
get
delete
```

在其他编程语言中，描述符被称作 setter 和 getter，而公共函数用于获得 (Get) 和设置 (Set) 一个私有变量。Python 没有私有变量的概念，而描述符协议可以作为一种 Python 的方式来实现与私有变量类似的功能。

总的来说，描述符就是一个具有绑定行为的对象属性，其属性访问将由描述符协议中的方法覆盖。这些方法为 __get__、__set__ 和 __delete__。如果这些方法中的任何一个针对某个对象定义，那么它就被认为是一个描述符。通过 

描述符方法
```
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```

其中：
```
__get__ 用于访问属性。它返回属性的值，或者在所请求的属性不存在的情况下出现 AttributeError 异常。
__set__ 将在属性分配操作中调用。不会返回任何内容。
__delete__ 控制删除操作。不会返回内容。
```
需要注意，描述符被分配给一个类，而不是实例。修改此类，会覆盖或删除描述符本身，而不是触发它的代码。

需要使用描述符的情况

考虑 email 属性。在向该属性分配值之前，需要对邮件格式进行检验。该描述符允许通过一个正则表达式处理电子邮件，然后对格式进行检验后将它分配给一个属性。

在其他许多情况下，Python 协议描述符控制对属性的访问，如保护 name 属性。

创建描述符

您可以通过许多方式创建描述符：
```
创建一个类并覆盖任意一个描述符方法：__set__、__ get__ 和 __delete__。当需要某个描述符跨多个不同的类和属性，例如类型验证，则使用该方法。

使用属性类型，这种方法可以更加简单、灵活地创建描述符。

使用属性描述符，它结合了属性类型方法和 Python 描述符。
```

以下示例在其操作方面均相似。不同之处在于实现方法。

使用类方法创建描述符
```
class Descriptor(object):

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        print "Getting: %s" % self._name
        return self._name

    def __set__(self, instance, name):
        print "Setting: %s" % name
        self._name = name.title()

    def __delete__(self, instance):
        print "Deleting: %s" %self._name
        del self._name

class Person(object):
    name = Descriptor()
```

使用这些代码并查看输出：
```
>>> user = Person()
>>> user.name = 'john smith'
Setting: john smith
>>> user.name
Getting: John Smith
'John Smith'
>>> del user.name
Deleting: John Smith
```

通过以下方法覆盖父类的 __set__()、__get__() 和 __delete__() 方法，创建一个描述符类：
```
get 将输出 Getting
delete 将输出 Deleting
set 将输出 Setting
```

并在分配之前将属性值修改为标题（第一个字母大写，其他字母为小写）。这样做有助于存储和输出名称。
大写转换同样可以移动到 __get__() 方法。_value 有一个初始值，并根据 get 请求转换为标题。


使用属性类型创建描述符

虽然上述代码中定义的描述符是有效的且可以正常使用，但是还可以使用属性类型的方法。通过使用 property()，可以轻松地为任意属性创建可用的描述符。创建 property() 的语法是 property(fget=None, fset=None, fdel=None, doc=None)，其中：
```
fget：属性获取方法
fset：属性设置方法
fdel：属性删除方法
doc：docstring
```

使用属性类型创建描述符
```
class Person(object):
    def __init__(self):
        self._name = ''

    def fget(self):
        print "Getting: %s" % self._name
        return self._name
    
    def fset(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    def fdel(self):
        print "Deleting: %s" %self._name
        del self._name
    name = property(fget, fset, fdel, "I'm the property.")
```

使用该代码并查看输出：
```
>>> user = Person()
>>> user.name = 'john smith'
Setting: john smith
>>> user.name
Getting: John Smith
'John Smith'
>>> del user.name
Deleting: John Smith
```

显然，结果是相同的。注意，fget、fset 和 fdel 方法是可选的，但是如果没有指定这些方法，那么将在尝试各个操作时出现一个 AttributeError 异常。例如，声明 name 属性时，fset 被设置为 None，然后开发人员尝试向 name 属性分配值。这时将出现一个 AttributeError 异常。

这种方法可以用于定义系统中的只读属性。
```
name = property(fget, None, fdel, "I'm the property")
user.name = 'john smith'
```
输出为：
```
Traceback (most recent call last):
File stdin, line 21, in mоdule
user.name = 'john smith'
AttributeError: can't set attribute
```

使用属性修饰符创建描述符

可以使用 Python 修饰符创建描述符，如下列代码所示。Python 修饰符是对 Python 语法的特定修改，能够更方便地更改函数和方法。在本例中，将修改属性管理方法。在 developerWorks 文章 Decorators make magic easy 中寻找更多有关应用 Python 修饰符的信息。

使用属性修饰符创建描述符
```
class Person(object):

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print "Getting: %s" % self._name
        return self._name

    @name.setter
    def name(self, value):
        print "Setting: %s" % value
        self._name = value.title()

    @name.deleter
    def name(self):
        print ">Deleting: %s" % self._name
        del self._name
```

在运行时创建描述符

前面的所有例子都使用了 name 属性。该方法的局限性在于需要对各个属性分别覆盖 __set__()、__get__() 和 __delete__()。下列代码提供了一个可能的解决方案，帮助开发人员在运行时添加 property 属性。该解决方案使用属性类型构建数据描述符。

在运行时创建描述符
```
class Person(object):

    def addProperty(self, attribute):
        # create local setter and getter with a particular attribute name 
        getter = lambda self: self._getProperty(attribute)
        setter = lambda self, value: self._setProperty(attribute, value)

        # construct property attribute and add it to the class
        setattr(self.__class__, attribute, property(fget=getter, \
                                                    fset=setter, \
                                                    doc="Auto-generated method"))

    def _setProperty(self, attribute, value):
        print "Setting: %s = %s" %(attribute, value)
        setattr(self, '_' + attribute, value.title())    

    def _getProperty(self, attribute):
        print "Getting: %s" %attribute
        return getattr(self, '_' + attribute)
```
让我们运行这段代码：
```
>>> user = Person()
>>> user.addProperty('name')
>>> user.addProperty('phone')
>>> user.name = 'john smith'
Setting: name = john smith
>>> user.phone = '12345'
Setting: phone = 12345
>>> user.name
Getting: name
'John Smith'
>>> user.__dict__
{'_phone': '12345', '_name': 'John Smith'}
```

这将在运行时创建 name 和 phone 属性。它们可以根据相应的名称进行访问，但是按照 _setProperty 方法中的定义，将在对象名称空间目录中存储为 _name 和 _phone。基本上，name 和 phone 是对内部的 _name 和 _phone 属性的访问符。

当开发人员尝试添加 name property 属性时，您可能对系统中的 _name 属性存在疑问。实际上，它将用新的 property 属性覆盖现有的 _name 属性。这些代码允许控制如何在类内部处理属性。


结束语

Python 描述符可以利用新的样式类实现强大而灵活的属性管理。通过结合使用描述符，可以实现优雅的编程，允许创建 Setters 和 Getters 以及只读属性。它还允许您根据值或类型请求进行属性验证。您可以在许多不同的领域应用描述符，但是使用时需保持谨慎的态度，避免由于覆盖普通对象行为而产生不必要的代码复杂性。


### 60. 区别__getattr__()和__getattribute__()方法



### 61. 使用更为安全的property



### 62. 掌握metaclass



### 63. 熟悉Python对象协议



### 64. 利用操作符重载实现中缀语法



### 65. 熟悉Python的迭代器协议



### 66. 属性Python的生成器



### 67. 基于生成器的协程及greenlet



### 68. 理解GIL的局限性



### 69. 对象的管理与垃圾回收
