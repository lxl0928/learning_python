## 编写高质量代码(改善Python程序的91个建议)_2

[TOC]

### 8. 利用assert语句来发现问题

assert语法: 
```
assert expression1 ["," expression2]
```
其中计算expression1的值会返回True或者False, 当值为False时候会引发AssertError, 
而expression2是可选的, 用来传递具体的异常信息.

例子: 
```
>>> x = 1
>>> y = 2
>>> assert x == y, "not equals"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: not equals.

>>>
```
(1) 不要滥用断言

(2) 如果python本身的异常能够处理就不要再使用断言

(3) 不要用断言检测用户输入

(4) 在函数调用后, 当需要确认返回值是否合理时候, 可以使用断言

(5) 当条件是业务逻辑继续下去的选角条件时可以使用断言

### 9. 数据交换值时, 不要使用中间变量

在python中交换两个变量的值, 推荐 :
```
>>> x, y = y, x
```
上面的形式不需要借助任何中间变量并且能够获得更好的性能.
测试时间: 
```
>>> from timeit import Timer
>>> Timer('temp = x; x = y; y = temp', 'x = 2, y = 3').timeit()
0.10689428530212189

>>> Timer('x, y = y, x', 'x = 2, y = 3').timeit()
0.08492583713832502
```
一般情况下Python表达式的计算顺序是从左到右, 但遇到表达式赋值的时候表达式右边的操作数先于左边的操作数计算, 因此表达式expr3, expr4 = expr1, expr2的计算顺序是expr1, expr2 ->expr3, expr4.因此对于表达式x, y = y, x, 其在内存中执行的顺序如下: 

(1) 先计算右边的表达式y, x, 因此先在内存中创建元祖(y, x)其标识符和值分别为y, x及其对应的值, 其中y和x是在初始化时已经存在于内存中的对象.

(2) 计算表达式左边的值并进行赋值, 元祖被依次分配给左边的标识符,通过解压啊缩, 元组第一标识符(为y)分配给左边第一个元素(此时为x), 元组第二个标识符(为x)分配给第二个元素(此时为y), 从而达道x, y值交换的目的.


### 10. 充分利用Lazy evaluation的特性

Lazy evaluation 通常被理解为"延迟计算"或者"惰性计算", 值得是仅仅在真的需要执行的时候才计算表达式的值, 充分利用Lazy evaluation的特性带来的好处主要体现那在以下两个方面: 
(1) 避免不必要的计算 ,带来性能上的提升.
对于python中的条件表达式if x and, 在x为false的情况下y表达式的值不再计算.而对于if x or y, 当x的值为true的时候将直接返回, 不再计算y的值.因此编程中应该充分利用该特性.
下面的例子用于判断一个单词是不是指定的缩写的形式: 
```
from time import time
t = time
abbreviation = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']
for i in xrange[1000000):
    if w in abbreviations:
    # if w[-1] == '.' and w in abbreviations:
        pass
print "total run time:"
print time()-t
```

如果使用注释行代替第一个if, 运行的时间大约会节省10%.因在编程过程中间, 对于or条件表达式应该将值为真的可能性较高的变量写在or的前面, 而and则应该退后.

(2) 节省空间, 是的无限循环的数据结构成为可能.
pytphon中最典型的使用延迟计算的例子就是生成器表达式, 它仅在每次需要计算的时候才通过yield产生所需要的元素.
例子: 斐波拉契数列: 
```
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

>>> from itertools import islice
>>> print list(islice(fib(), 5))
[0, 1, 1, 2, 3]
```

### 11. 理解枚举替代实现的缺陷

利用python的动态性特征, 枚举的替代实现方式(枚举类型在python3.4版本后提供)

(1) 使用类属性
```
>>> class Seasons:
...    spring = 0
...    summer = 1
...    autumn = 2
...    winter = 3

>>> print Seasons.spring
0
```
可简化为: 
```
class Seasons:
    spring, summer, autumn, winter = range(4)
```

(2) 借助函数
```
def enum(*posarg, **keysarg):
    return type("Enum", (object, ), dict(zip(posarg, xrange(len(posarg))), **keysarg))

>>> Seasons = enum("spring", "summer", "Autumn", winter=1)
>>> Seasons.spring
0
```

(3) 使用collections.namedtuple
```
>>> Seasons = nametuple('Seasons', 'Spring, Summer, Autumn, Winter')._make(range(4))
>>> print Seasons.Spring
0
```

(4) python2.7后另一种替代选择: 第三方的flufl.enum
flufl.enum包含两种枚举类: 一种是Enum, 只要保证枚举值唯一即可, 对值的类型没有限制.
还有一种是IntEnum, 器枚举值为int型.
```
from flufl.enum import Enum
class Seasons(Enum):
    Spring = "Spring"
    Summer = 2
    Autumn = 3
    Winter = 4

>>> Seasons = Enum('Seasons', 'Spring Summer Autumn Winter')
```

flufl.enum提供了__members__属性, 可以对枚举名称进行迭代: 
```
for member in Seasons.__members__:
    print member

"""结果:
Spring
Summer
Autumn
Winter
"""
```
可以直接使用 value属性获取枚举元素的值, 
```
>>> print Seasons.Summer.value
2
```

flufl.enum不支持枚举元素的比较
```
>>> Seasons.Summer < Sessons.Autumn # flufl.enum不支持无意义的操作
NotImplementedError
```
python3.4增加对枚举类型的支持参考了flufl.enum

问题: 为什么要求语言实现枚举类型?
```
 1) 替代实现有其不合理的地方, 替代方案允许枚举值重复
 2) 替代支持无意义的操作, 枚举值相加
 3) python3.4提供枚举类型支持, 可以有效避免上述两种情况
```

### 12. 不推荐使用type来进行类型检查

作为动态性的强类型脚本语言, python中的变量在定义的时候并不会指定具体的类型,
python解释器会在运行时自动进行类型检查并更具需要进行隐式的类型转换.
例子: add()
```
def add(a, b):
    return a+b

print add(1, 2j)          # 复数相加
print add('a', 'b')       # 字符串连接
print add(1, 2)           # 整数相加
print add(1.0, 2.3)       # 浮点数
print add([1, 2], [2, 3]) # 处理列表
print add(1, 'a')         # 不同类型

"""结果:
(1+2j)
ab
3
3.3
[1, 2, 2, 3]
TypeError....
"""
```

内建函数type(object)用于返回当前对象的类型, 如type(1)返回<type 'int'>
例子: 判断一个变量a是不是list类型
```
if type(a) is types.listType:
    pass
```
所有基本类型都可以在types模块中找到: types.BoolenType, types.IntType, tupes.StringType, types.DictType等.

主张"不推荐使用type类进行变量类型检查"原因: 

(1) 基于内建类型扩展的用户自定义类型, type函数并不能准确返回结果
例子: 下例中的UserInt继承Inr类实现定制化, 它不支持操作符 +=
```
imoprt types
class UserInt(int): 
    def __init__(self, val=0):
        self._val = int(val)

    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val = val._val)
        return self._val + val

    def __iadd__(self, val):
        raise NotImplementeError("not support operation")

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return "Integer(%s)' %self._val

n = UserInt()
print n

m = UserInt(2)
print m

print m + n

print type(n)

print type(n) is types.IntType

print isinstance(n, int)    # 推荐使用

"""结果:
0
2
2
<class '__main__.UserInt'>
False    # 输出False, 说明type()函数认为n并不是int类型, 但UserInt继承自int, 这种判断显然不合理
True
"""
```

(2) 在古典类中, 任意类型的实例的type()返回的结果都是<type 'instance'>
在古典类中, 所有类的实例的type值都相等
```
class A:
    pass

class B:
    pass

a = A()
b = B()

print type(a)
print type(b)
print type(a) == type(b)
"""结果: 
<type 'instance'>
<type 'instance'>
True
"""
```

问题: 应怎样来约束用户的输入类型从而使之与我们期望的类型一致呢?
答案: 如果类型有对应的工厂函数, 可以使用工厂函数对类型做相应的转换.如list(listing), str(name)等, 
否则可以使用isinstance()函数来检测: 
```
isinstance(object, classinfo);
```
其中, classinfo可以为直接或者间接的类名, 基本类型名或者由他们组成的元组
例子: 
```
>>> isinstance(2, float)
False

>>> isinstance("a", (str, unicode))
True

>>> isinstance((2, 3), (str, list, tuple))
True
```


### 13. 尽量转换为浮点类型后再做除法

当涉及除法运算时候尽量先将操作数转化为浮点类型再做运算
```
>>> gpa = float((4*94 + 3*85 + 5*98 + 2*70)*4)/float((4 + 3 + 5 + 2)*100)
>>> print gpa
3.62571428571
```

虽则Python语言的发展, 对整数除法问题也做了一定的修正, 在Python3中这个问题已经不存在了,python3之前的版本可以通过: 
from __future__ import division机制使整数除法不再截断, 这样及时不进行浮点类型转换, 输出的结果也是正确的.

注意: 上面gpa的例子是浮点数运算精确, 有些情况下浮点运算是不精确的.
```
>>> i = 1
>>> while i != 1.5:
...     i = i + 0.1
...     print i

```

### 14. 警惕eval()的安全漏洞

(1) python中eval()函数将字符串str当成有效的表达式来求值并返回计算结果．其函数申明如下:
```
eval(expression[, globals[, locals]])
```
其中，　参数globals为字典形式，locals为任何映射对象, 它们分别表示全局和局部变量命名空间.
如果传入globals参数的字典中缺少__builtins__的时候, 当前的局部命名空间将作为globals参数输入冰球在表达式计算之前被解析.
locals参数默认与globals相同, 如果两者都省略的话, 表达式将在eval()调用的环境中执行.
例子: 
```
>>> eval("1+1 = 2")
True

>>> eval("'A' + 'B'")
'AB'

>>> eval("1+2")
3

>>>
```

(2) eval()安全漏洞问题
例子:
```
import sys
from math import *
def ExpCalcBot(string):
    try:
        print "Your answer is", eval(user_func)   # 计算输入的值
    except NameError:
        print "The expression you enter is not valid"

print "Hi, I am ExpCalcBot. please input your expression or enter e to end"
inputstr = ""
while 1:
    print "Please enter a number or operation, Enter c to complete. :"
    inputstr = raw_input()
    if inputstr == str('e'):    # 遇到e时退出
        sys.exit()
    elif repr(inputstr) != repr(''):
        ExpCalcBot(inputstr)
        inputstr = ''
```
上面这段代码的主要功能: 根据用户的输入, 计算Python表达式的值.
基于用户并不都可信, 会出现一系列安全问题.
问题1:
  用户输入: __import__("os").system("dir")
  结果: 显示当前目录下所有文件列表

问题2:
  用户输入: __import__("os").system("del" * /Q")
  结果: 当前目录下的所有文件都被删除

问题3:
  在globals参数中禁止全局命名空间的访问.
```
def ExpCalcBot(string):
    try:
        math_fun_list = ['acos', 'asin', 'atan', 'cos', 'e', 'log', 'log10', 'pi', 'pow', 'sin', 'sqrt', 'tan']
        math_fun_dict = dict([ (k, globals().get(k)) for k in math_fun_list ])

        print "Your answet is", eval(string, {"__builtins__": None}, math_fun_dict)
    except NameError:
        print "The expression you enter is not valid"
```

  用户输入: [c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == 'Quitter'][0](0)()
  结果: 直接导致<F12>程序退出
  ().__class__.__base__[0].__subclasses__()用来显示object类的所有子类.类Quitter与"quit"功能绑定, 因此上面的输入会直接导致程序退出.



### 15. 使用enumerate()获取序列迭代的索引和值

基本上所有的项目中都存在对序列进行迭代并获取序列中的元素进行处理的场景.
例子: 

方法1: 在每次循环中对索引变量进行自增
```
li = ['a', 'b', 'c', 'd', 'e']
index = 0    # index为列表开始的索引下标
for i in li:
    print("index: ", index, "element: ", li[i])

"""结果:
index: 0 element:  a
index: 1 element:  b
index: 2 element:  c
index: 3 element:  d
index: 4 element:  e
"""
```

方法2: 使用range()和len()方法结合
```
li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
    print("index: ", i, "element: ", li[i])

"""结果:
index: 0 element:  a
index: 1 element:  b
index: 2 element:  c
index: 3 element:  d
index: 4 element:  e
"""
```

方法3: 使用while循环, 用len()获取循环次数
```
li = ['a', 'b', 'c', 'd', 'e']
index = 0
while index < len(li):
    print("index: ", index, "element: ", li[index])
    index += 1

"""结果:
index: 0 element:  a
index: 1 element:  b
index: 2 element:  c
index: 3 element:  d
index: 4 element:  e
"""
```

方法4: 使用zip()方法
```
li = ['a', 'b', 'c', 'd', 'e']
for i, e in zip(range(len(li)), li):
    print("index: ", i, "element: ", e)
"""结果:
index: 0 element:  a
index: 1 element:  b
index: 2 element:  c
index: 3 element:  d
index: 4 element:  e
"""
```

方法5: 使用enumerate()获取序列迭代的索引和值:
```
li = ['a', 'b', 'c', ''d', 'e']
for i, e in enumerate(li):
    print("index: ", i, "element: ", e)

"""结果:
index: 0 element:  a
index: 1 element:  b
index: 2 element:  c
index: 3 element:  d
index: 4 element:  e
"""
```

这里推荐的是使用方法5, 因为它代码清晰简介, 可读性最好.
函数enumerate()实在python2.3中引入的, 主要是为了解决在循环中获取索引以及对应值的问题.它具有一定的惰性, 每次仅在
需要的时候才会产生一个(index, item)对, 其函数签名如下:
```
enumerate(sequence, start=0)
```
其中, sequence可以为序列, 如list, set等, 也可以为一个iterato或者任何可以迭代的对象, 默认的start为0, 函数返回本质上为一个迭代器, 可以使用next()方法获取下一个迭代元素, 如:
```
>>> li = ['a', 'b', 'c', 'd', 'e']
>>> print(enumerate(li))
<enumerate object at 0x00373E18>
>>> e = enumerate(li)
>>> e.next()
(0, 'a')

>>> e.next()
(1, 'b')
```

enumerate()函数的内部实现非常简单(类似下面):
```
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

因此利用这个特性用户还可以自己实习那enumerate()函数. 比如, myenumerate()以反转的形式获取序列的索引和值:
```
def myenumerate(sequence):
    n = -1
    for elem in reversed(sequence):
        yield len(sequence)+n, elem
        n = n-1

li = ['a', 'b', 'c', 'd', 'e']]
for i, e in myenumerate(li):
    print("index: ", i, "element: ", e)

"""结果:
index: 4 element:  e
index: 3 element:  d
index: 2 element:  c
index: 1 element:  b
index: 0 element:  a
"""
```
需要提醒的是: 对于字典的迭代循环, enumerate()函数并不适合, 虽然在使用上并不会提示错误, 但出书的结果与期望结果大相庭径.
这时因为字典默认被转换成了序列进行处理.
例子: 
```
personinfo = {'name': 'Jon', 'age': '20', 'hobby':'football'}
for k, v in enumerate(personinfo):
    print("key: ", k, "value: ", v)

"""结果:
0 hobby
1 age
2 name
"""

要获取迭代过程中的字典的key和value, 应该使用下面的iteritems()(python2支持)方法:
```
for k, v in personinfo.iteritems():
    print("key: ", k, "value: ", v)


"""结果:
('key: ', 'hobby', 'value: ', 'football')
('key: ', 'age', 'value: ', '20')
('key: ', 'name', 'value: ', 'Tom')
"""
```

### 16. 分清 == 与 is 的适用场景

判断两个字符串是否相等的时候, 混用is和==是很多初学者经常犯得错误, 造成的结果是程序在不同的情况下表现不一.
例子: 
```
>>> a = "Hi"
>>> b = "Hi"
>>> a is b
True

>>> a == b  # is和 == 结果一样
True

>>> a1 = "I am using long string for testing"
>>> b1 = "I am using long string for testing"
>>> a1 is b1
False

>>> a1 == b1
True

>>> str1 = "string"
>>> str2 = "".join(['s', 't', 'r', 'i', 'n', 'g'])
>>> print str1
string
>>> print str2
string

>>> str1 is str2
False

>>> str1 == str2 # is 和 == 在这种情况下也不一样
True
```

造成这种奇怪现象的原因是什么呢?
提示: id()函数可查看变量在内存中的具体存储空间
is表示的是对象标识符(object indetify), ==表示意思是相等.
根本原因: is的作用是用来检查对象的标识符是否一样, 也就是比较两个对象在内存中是否拥有同一块内存空间, 它并不适合用来判断两个字符串是否相等.
x is y 仅当x和y是同一个对象的时候才返回True, x is y基本相当于  id(x) == id(y).
而 x == y才是用来检验两个对象的值是否相等的, 它实际调用内部__eq__()方法, 
因此a == b相当于a.__eq__(b), 所以==操作符使可以被重载的, 而is不能被重载.
一般情况下: 
  如果 x is y 是True的话, x == y的值也为True(特殊情况除外, 如NaN, a=float("NaN"), 
  a is a为True, a == a为False

### 17. 考虑兼容性, 尽可能的使用Unicode

python内建的字符串有两种类型: str, Unicode, 他们拥有共同的祖先basestring
其中, Unicode是python2.0引入的一种新的数据类型, 所有Unicode字符串都是Unicode类型的实例

(1) 字符串解码decode()
将其它编码对应的字符串解码成Uniclde
```
str.decode([编码参数 [, 错误处理]])
```

(2) 字符串编码encode()
将Unicode编码转换成另一种编码
```
str.encode([编码参数 [, 错误处理]])
```

(3) 对源文件编码声明
  1)
  ```
  # coding=<encoding name>
  ```
  2)
  ```
  #! /usr/bin/python
  # -*- coding: <encoding name> -*-
  ```
  3)
  ```
  #!/usr/bin/python
  #vim: set fileencoding=<encoding name> :
  ```


### 18. 构建合理的包层次来管理module

本质上每一个Python文件都是一个模块,使用模块可以增强代码的科维护性和可重用性.

问题：什么是包？
简单说包就是目录，　但与普通目录不同，　它除了包含常规的python文件(模块)外,
还包含一个__init__.py文件, 同时,它允许嵌套, 包的结构如下:
```
Package/ __init__.py
    Module1.py
    Module2.py
    Subpackage/ __init__.py
        Module1.py
        Module2.py
```

包中的模块通过"."访问符进行访问, 即:"包名.模块名"
包中的模块导入其它模块的方法:

(1) 直接导入一个包
```
import Package
```

(2) 导入子模块或者子包, 包嵌套的情况下可以进行嵌套导入
```
from Pakckage import Module1
import Package.Module1
from Package import Subpackage
import Package.Subpackage
from Package.Subpackage imoprt Module1
import Package.Subpackage.Module1
```

前面提到包对应的目录下包含__init__.py文件, 这个文件的作用是什么?
```
1) 区分包和普通目录
2) 可以在该文件中申明模块级别的import语句, 从而使其变成包级别可见
3) 通过在该文件中定义__all__变量, 控制需要导入的子包或者模块.
```
上例中, 如果要import包Package下Module1中的类Test, 当__init__.py文件为空时, 需要使用弯针的路径来申明import语句:
```
from Package.Module1 imoprt Test
```

但如果在__init__.py中添加:
```
from Module1 import Test
# 该语句, 则可以直接使用from Package import Test来导入类Test.
```

当__init__.py文件为空, 当意图使用from Package import *将包Package中所有模块导入当前名字空间时, 并不能是的导入的模块生效, 这时因为不同平台间的文件的命名规则不同, Python解释器并不能正确的判断模块在对应的平台该如何导入.
因此, 它仅仅执行__init__.py文件, 如果需要控制模块导入, 则需要对__init__.py文件做修改.

```
# filename: __init__.py
__all__ = ['Module1', 'Module2', 'Subpackage']
```

之后运行:
```
>>> from Package import *
>>> dir()
['Module1', 'Module2', 'Subpackage', '__builtins__', __doc__', '__name__', '__package__']

```

包能够带来以下便利:

1) 合理组织代码, 便于维护使用
```
ProjectName/
|---README
    |----LIICENSE
    |----setup.py
    |----requirements.txt
    |----sample/
    |    |----__init__.py
    |    |----core.py
    |    |----helpers.py
    |----docs/
    |    |----conf.py
    |    |----index.rst
    |----bin/
    |----package/
    |    |----__init__.py
    |    |----subpackage/
    |    |----....
    |----tests/
    |    |----test_basic.py
    |    |----test_advaced.py
```

2) 能够有效避免名称空间冲突
