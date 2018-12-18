## 编写高质量代码(改善Python程序的91个建议)_3: 基础语法

[TOC]

### 19. 有节制的使用from...import语句.

在使用import的时候注意: 

1) 一般情况下尽量优先使用import a的形式， 如访问B时， 使用import a.B
2) 有节制的使用from a import B形式， 可以直接访问B
3) 尽量避免使用from a import ×，因为这样会污染命名空间并且无法清晰表示导入了哪些对象

无节制使用from a import ...带来的问题:

1) 命名空间的冲突

例子: 假设有如下三个文件， a.py b.py 及importtest.py，其中a和b都定义了add()函数。
当在import test文件中同时采用from...import...的形式导入add的时候，import test中起作用的到底是哪一个函数呢?
```
文件a.py如下:
def add():
    print("add in module A")

文件b.py如下:
def add():
    print("add in module B")

文件importtest.py如下:
from a import add
from b import add

if __name__ == "__main__":
    math()

"""结果：
add in module B
"""
```

由此可见， 实际起作用的是最近导入的add()


2) 循环导入的问题

例子:
```
c1.py:
from c2 import g
def x():
    pass

c2.py:
from c1 import x
def g():
    pass
```
无论运行上面哪一个文件都会报错ImportError的异常。
原因: 执行c1.pu的加载过程中， 需要创建新的模块对象c1然后执行c1.py所对应的字节码。
此时遇到from c2 import g，而c2在sys.modules也不存在， 故此创建c2对应的模块对象并执行c2.py所对应的字节码，而此时from c1 import x中的c1对应的模块对象没有创建完成， 陷入循环， 抛出异常

### 20. 优先使用absolute import 来导入模块

假设有如下文件结构:
```
app/
   __init__.py
   sub1/
       __init__.py
       mod1.py
       string.py
    sub2/
       __init__.py
       mod2.py
       string.py
```
其中app/sub1/string.py中定义了一个lower()方法， 那么当在mod1.py中import string之后
再使用string.lower()方法时，引用的是哪个lower()方法?

答: 它引用的是app/sub1/string.py中的lower()方法。
显然解释器先从当前目录下搜索对应的模块， 当搜到string.py的时候便停止搜索，进行动态加载。

那么，如果要使用python自带的string模块中的方法， 该怎么实现？

答: 使用absolute import 和 relative import(已淘汰)

通过:
```
在模块中使用from __future__ import absolute_import 语句说明后再进行导入。

```
### 21. i+=1 不等于 ++i

有如下代码:
```
i = 0
mylist = [1, 2, 3, 4, 5, 6]
while i < len(mylist):
    print(mylist[i])
    ++i
```

运行这段代码会有什么问题呢?
这段代码不会抛出任何错误， 却会无限循环的输出1.

原因：
因为python解释器将++i操作解释为+(+i), 其中第一个+表示正负号。对于--i操作也是类似
```
>>> +1
1

>>> ++1
1

>>> ++++1
1

>>> -2
-2

>>> --2 # 负负得正
2

>>> -----2
-2

```

因此, ++i在python中语法上是合法的， 但并不是我们理解的通常意义上的自增操作。

### 22. 使用with自动关闭资源

[参考: python_with_usage](https://coding.net/u/lxl0928/p/python/git/blob/master/python_technical_articles/python_with_usage.md)


### 23. 使用else子句简化循环(异常处理)

在python中，不仅if-else分支有else， 在while，for循环，异常处理都有else。语法:
```
while_stmt ::= "while" expression ":" suite
               ["else" ":" suite]

for_stmt ::= "for" target_list "in" expression_list ":" suite
               ["else" ":" suite]

try_stmt ::= try1_stmt |try2_stmt
try1_stmt ::= "try" ":" suite
              ("except" [expression [("as" | ",") target]] ":" suite)+
              ["else" ":" suite]
              ["finally" ":"suite]

try2_stmt ::= "try" ":" suite
              "finally" ":" suite
```

例子: 找素数，for循环使用else
```
def print_prime(n):
    for i in xrange(2, n):
        for j in xrange(2, i):
            if i % j == 0:
                break;
        else:
            print("{number} is a prime number".format(number = i))
```
当循环自然终结(或者循环条件为假)时， else从句会被执行一次，而当循环是由break语句中断时，
esle子句就不会被执行。while循环类似。。。

例子: python异常处理中的try-except-else-finally形式, 把数据写入文件中
```
def save(db, obj):
    try:
        # save attr1
        db.execute('a sql stmt', obj.attr1)
        # save attr2
        db.execute('a sql stmt', obj.attr2)
    except DBError:
        db.rollback()
    else:
        db.commit()
    finally:
        print("执行到finally里了")
```

### 24. 遵循异常处理的几点基本原则

语法形式:
```
try:
    <statements>              # run this main action
except <name1>:
    <statements>              # 当try中发生name1的异常处理
except<name2, name2>:
    <statements>              # 当try中发生name2或者name3的异常处理
except<name4> as <date>:
    <statements>              # 当try中发生name4的异常处理， 并获取对应的实例
except:
    <statements>              # 其它异常发生时
finally:
    <statements>              # 不管有没有异常发生都会执行
```

原则:

1) 不推荐在try中放入过多的代码。

2）谨慎使用单独的except语句处理所有的异常， 最好能定位具体异常

3）注意异常捕获的顺序，在何时的层次捕获异常

4）使用更为友好的异常信息，遵守异常参数的规范

5）如果内建异常类不能满足需求，用户可以在继承内建异常的基础上针对特定的业务逻辑
定义自己的异常类，都需要遵守异常参数规范。

### 25. 避免finally中可能发生的陷阱

无论try语句是否有异常抛出，finally都会被执行， 由于这个特性，finally语句经常被用来做一些清理工作，如打开一个文件， 抛出异常后在finally中对文件句柄进行关闭。

但在使用finally时，要小心一些陷阱:
例子:
```
def finally_test():
    print("I am starting")
    while True:
        try:
            print("I am runing")
            raise IndexError("r") # 抛出IndexError异常
        except NameError, e:
            print("NameError happended %s", e)
            break
        finally:
            print("finally executed")
            break

finally_test()
```

上述程序输出的结果：
```
I am starting
I am running
finally executed
```

原因:
上面的例子，try抛出了IndexError异常，但在except块却没有对应的异常处理，按常理异常会向上层抛出，但是程序输出并没有提示任何异常发生，IndexError异常被丢失了。因为，当try中发生异常的时候，如果在except语句中没有对应的异常处理，那么异常将会被临时保存起来，当finally执行完毕的时候，临时保存的异常将会再次被抛出。但如果finally语句中产生了新的异常或者执行了return或者break时，该临时保存的异常会被丢失，导致异常被屏蔽。

例子:
```
def return_finally_test(a):
    try:
        if a<= 0:
            raise ValueError("data can not be negative")
        else:
            print("In else")
            return a
    except ValueError as e:
        print(e)
    finally:
        print("In finally")
        return -1

print(return_finally_test(0))
print(return_finally_test(2))

"""结果:
data can not negative
In finally
-1


In else: 
In finally
-1

"""
```
原因:
  对于a = 0， 程序输出-1很正常， 为什么a = 2会输出-1，而没有输出2呢？
  因为, 在a = 2时， 执行else语句中的return a前，先执行了finally中的语句，此时由于finally中有return -1，程序直接就返回了，所以永远也不会执行return a
  所以不推荐在finally中用return语句返回.

### 26. 深入理解None, 正确判断对象是否为空

python中哪些形式的数据为空？
```
1）常量None
2) 常量False
3) 任何形式的数值类型零
4）空的序列，如“ ，(), []”
5) 空的字典, 如"{}"
6) 当用户定义的类中定义了nonzero()方法和len(0方法，并且该方法返回整数0或者布尔值False时候。

其中， 常量None特殊在既不是0，False， 也不是空字符串，他就是一个空值对象。其数据类型为NoneType, 遵循单例模式，是唯一的，因而不能创建None对象，所有赋值为None的变量都相等，并且None与任何其它非None的对象相比较的结果都为False.

__nonzero__()方法:
该内部方位用于对自身对象的空值测试。返回0/1,True/False.
如果一个对象没有定义该方法，Python将获取__len__()方法调用的结果进行判断。
__len__()返回值为0则表示为空。如果一个类中既没有定义__len__()也没有定义__nonzero__()方法，该类实例用if判断的结果都为True：
```
class A:
    def __nonzero__(self): # 类中实现了__nonzero__()方法
        print("testing A.__nonzero__()")
        return True
    def __len__(self):
        print("get length")
        return False

if A(): # 自动执行的时候会自动调用__nonzero__()方法
    print("not empty")
else:
    print("empty")

"""结果:
testing A.__nonzero__()
not empty
"""
```
```


### 27. 连接字符串应优先使用join而不是+

字符传连接的两种方式:

1) 使用操作符 "+" 连接字符串
```
>>> str1, str2, str3 = "testing", "string", "concatenating"
>>> str1+str2+str3
'testing string concatenating'
```

2) 使用join方法连接字符串:
```
>>> str1, str2, str3 = "testing", "string", "concatenating"
>>> ''.join([str1, str2, str3])
'tesing string concatenting'
```

使用 "join"会比 "+"快速很多

"+"时间复杂度: O(n^2)
"join"时间复杂度: O(n)

### 28. 格式化字符串使尽量用.format方式而不是%

python中的%操作符和.format方式都可用于格式化字符串。
```
1) 格式化字符串转换标记(略)

2) 格式化字符串转换类型

3) %操作符格式化字符串几种常见用法: 直接格式化，元组形式格式化，以字典形式格式化

4）.format
4.1. .format方式格式化字符串的对齐方式
4.2. .format方式格式化字符串符号列表
4.3. .format方法集中常见的用法如下:

使用位置符号:
>>> "The number {0:,} in hex is : {0:#x}, the number {1} in oct is {1:#o}".format(4746, 45)
'The number 4,746 in hex is: 0x128a, the number 45 in oct is 0o55'
  
使用名称:
>>> print("The max number is {max}, the min is {min}, the average number is {average:0.3f}".format(max=189, min=12.6, average=23.5))
The max number is 189, the min is 12.6, the average number is 23.500

通过属性:
>>> class Customer(object):
...     def __init__(self, name, gender, phone):
...         self.name = name
...         self.gender = gender
...         self.phone = phone
...     def __str__(self):
...         return 'Customer({self.name}, {self.gender}, {self.phone})'.format(self=self)

>>> str(Customer('Lisa', 'Female', '67889')
'Customer(Lisa, Female, 67889)'
```

通过格式化元组具体项:
>>> point = (1, 3)
>>> 'X: {0 [0]}; Y: {1 [1]}'.format(point)
'X: 1; Y:3'

4.4 .format优势
理由1: format更加灵活， 参数顺序没有要求
理由2: format方便传递参数
理由3: %号最终会被format替代
理由4: %方法在某些特殊情况下要特别小心


### 29. 区别对待可变对象和不可变对象

python中一切皆对象，每一个对象都有一个唯一的标识符(id())，类型(type()), 以及值。
对象根据其值能否修改分为可变对象和不可变对象。

可变对象: 字典，列表，字节数组

不可变对象: 数字，字符串，元组

例子: 修改字符串中某个字符的值:
```
# 错误的做法
teststr = "I am a pytlon string"
teststr[11] = 'h'
print(teststr)
"""结果
I am a pytlon string
"""

# 正确的做法
teststr = "I am a pytlon string"
import array
a = array.array('c', teststr)
a[10] = 'h'
print(a.tostring())
"""结果:
I am a python string
"""
```

例子: 
```
class Student(object):
    def __init__(self, name, course=[]):
        self.name = name
        self.course = course
    def addcourse(self, coursename):
        self.course.append(coursename)
    def printcourse(self):
        for item in self.course:
            print(item)

stuA = Student("Wang Yi")
stuA.addcourse("English")
stuA.addcourse("Math")
print("-----------------")
stuA.printcourse()

stuB = Student("Li san")
stuB.addcourse("Chinese")
stuB.addcourse("Physics")
print("-----------------")
stuB.printcourse()

"""结果：
----------------
English
Math

----------------
English
Math
Chinese
Physics
"""
```
正确做法:
```
def __init__(self, name, course=None):
    self.name = name
    if course is None:
        course = []
    self.course = course
```

对于可变对象:
list的切片操作实际上会生成新的对象，因为切片相当于浅拷贝。

```
>>> a = 1
>>> id(a)
12184696

>>> id(1)
12184696

>>> a += 2
>>> a 
3
>>> id(a)
12184672
>>> id(3)
12184672
```

问题： a是属于数值类型,不可变对象，怎么会发生改变?

答: 数值不可便对象是指1,为不可变， a存放的只是1在内存中的地址，在上面过程中，改变的是a所指向的对象的地址，1并没有变化，当执行a += 2时，重新分配了一块内存地址存放结果3，并将a的引用改为该内存的地址，而1所在内存空间最终会被垃圾回收器回收。

### 30. [], (), {}: 一致容器初始化形式

列表是一个很有用的数据结构，在python中属于可变对象，列表中的元素没有限制，可以重复，可以嵌套，操作上支持切片，单个元素的读取修改，还支持排序，插入，删除。

例子：去掉单词所包含的空格后判断首字母是否大写
```
words = [' Are', ' abandon', 'Passion', 'Business', ' fruit ', 'quit']
size = len(words)

newlist = []
for i in range(size):
    if words[i].strip().istitle():
        newlist.append(words[i])
print(newlist)
```

更好的实现方式，列表解析
```
[expr for iter_item in iterable if cond_expr]
```
它迭代iterable中的每一个元素，当条件满足时候便根据表达式expr计算的内容生成一个元素并放入新的列表中。依次类推。
等价于:
```
Newlist = []
for iter_item in iterable:
    if cond_expr:
        Newlist.append(expr)
```

其中条件表达式不是必需的，如果没有条件表达式，就直接将expr中计算出的元素加入List中，列表解析的使用非常灵活。

1)支持多重嵌套
```
>>> nested_list = [['Hello', 'World'], ['Goodbye', 'World']]
>>> nested_list = [[s.upper() for s in xs] for xs in nested_list]
[['HELLO', 'WORLD'], ['GOODBYE', 'WORLD']]
```

2) 支持多重迭代。下面的例子中a, b分别对应两个列表中的元素，[(a,b) for a in ['a', '1', 1, 2] for b in ['1', 3, 4, 'b'] if a != b表示:
列表['a', '1', 1, 2]和['1', 2, 4, 'b']依次来迪卡尔积之后并去掉元素值相同的元组之后所身下的元组的集合
```
>>> [(a, b) for a in ['a', '1', 1, 2] for b in ['1', 3, 4, 'b'] if a != b
...结果...
```

3)列表解析语法中的表达式可以是简单表达式，也可以是负责表达式，甚至是函数:
```
def f(v):
    if v%2 == 0:
        v = v**2
    else:
        v = v+1
    return v

>>> [f(v) for v in [2, 3, 4, -1] if v > 0 # 表达式可以是函数
＃在[2, 3, 4, -1]中迭代，如果v>0，就执行函数ｆ(v)
```

4) 列表解析语法中iterable可以是任意可迭代对象。
例子:把文件句柄当作一个可迭代对象，课轻易读出文件内容。
```
fh = open("test.txt", "r")
result = [i for i in fh if "abc" in i] # 文件句柄可以当作可迭代对象
print(result)
```

使用列表解析原因:

1) 使用列表解析，代码更简洁只管清晰
2) 列表解析效率更高

### 31. 记住函数传参既不是传也不是传引用

问题: python中的函数参数到底是传值还是传引用呢?

答: 都不是，正确的说法应该是传递对象(call by object)或者说传对象的引用。
函数参数传递的过程中将整个对象传入，对可变对象的修改在函数的外部以及内部都可见。调用者和被调用者之间共享这个对象，而对于不可便对象，由于并不能真正被修改，因此，修改往往是通过生成一个新对象让后赋值来实现.

### 32. 警惕默认参数潜在的问题

默认参数可以给函数的使用带来很大的灵活性,当函数调用没有指定与形参对应的实参就会自动使用默认参数:
```
def appendtest(newitem, list_a = []):  # 默认参数列表为空
    print(id(list_a))
    lista.append(newitem)
    print(id(list_a))
    return list_a
```
```
>>> appendtest('a', ['b', 2, 4, [1, 2]])
"""结果
39644126
39644126
['b', 2, 4, [1, 2], 'a']
"""
```

问题: 如果第二个参数采取默认参数，连续调用两次appendtest(1), appendtest('a'), 函数返回值是多少?

期望结果: [1] 和 ['a']
实际结果: [1] 和 [1, 'a']

原因:
def在python中是一个课执行的语句，当解释器执行def的时候，默认参数也会被计算，并存在函数的.func_defaults属性中，由于python中函数参数传递的是对象，可变对象在调用者和被调用者之间共享，因此当首次调用appendtest()的时候, []变为[1], 而再次调用的时候是由于默认参数不会被重新计算，在[1]的基础上便变为了[1, 'a']. 我们可以通过查看函数的func_defaults来确认这一点。
```
appendtest.func_defaults
```

正确的做法:
```
def appendtest(newitem, list_a = None):
    if list_a is None:
        list_a = []
    list_a.append(newitem)
    return list_a
```

### 33. 慎用变长参数

python支持可变长参数列表，可以通过在函数定义的时候使用*args和**kwargs这两个特殊语法来实现。其中args和kwargs可以替换成任意合法的变量名。

1) 使用*args来实现可变参数列表: *args用于接受一个包装为元组形式的参数列表来传递非关键字参数，参数的个数可以任意:
```
def SumFun(*args):
    result = 0
    for x in args[0:]:
        result += x
    return result

print(SumFun(2,4))
print(SumFun(1,2,3,4,5))
print(SumFun())
```

2) 使用**kwargs接受字典形式的关键字参数列表，其中字典的键值对分别表示不可变参数的参数名和值。如下:
```
def category_table(**kwargs):
    for name, value in kwargs.items():
        print('{0} is a kind of {1}'.format(name, value))
category_tavle(apple='fruit', carrot='vegetable', Python='programming language')
category_table(BMW='Car')

```

问题: 当一个函数中间同时定义了普通参数，默认参数，以及上述两种形式的可变参数，那么使用情况又是怎么样的呢？

答: 如def set_axis(x, y, xlabel="x", ylabel="y", *args, **kwargs)
如果四种不同形式的参数同时存在的情况下，会首先满足普通函数，然后是默认参数，如果剩余的参数个数嗯呢狗狗覆盖所有的默认参数，则默认参数会使用传递时候的值。

为什么慎用可变长度参数?

1) 使用过于灵活，而不便于函数的调用

2）如果一个函数的参数列表很长，可变长参数来简化函数定义，但这 意味着有更好的方法重构这个函数。

3）可变长参数适合在如下情况下使用:
  3.1 为函数添加一个装饰器
```
def myDecorator(fun):
    def new(*args, **kwargs):
        # ...
    return new

```

  3.2 如果参数的数目不确定
```
  # func(**kwargs)用于读取一些配置文件职工的值并进行全局变量的初始化
  from ConfigParser import ConfigParser
  conf = ConfigParser()
  cong.read('test.cfg')
  cong_dict = dict(conf.items('Defaults'))

  def func(**kwargs):
      kwargs.update(conf_dict)
      global name
      name = kwargs.get('name')
      global version
      version = kwargs.get('version')
      global platform
      platform = kwargs.get('platform')

```
  
  3.3 用来实现函数的多态或者在继承情况下子类需要调用父类的某些方法的时候。
```
class A(object):
    def somefun(self, p1, p2):
        pass

class B(A):
    def myfun(self, p3, *args, **kwargs):
        super(B, self).somefun(*args, **kwargs)

```
### 34. 深入理解str()和repr()的区别

str()和repr()区别:

1) 两者之间的目标不同，str()是面向用户，其目的是可读性，返回形式为用户友好性和可读性都较强的字符串类型；而repr()面向的是python解释器，或者说开发人员，其目的是准确性，器返回值表示pyhton解释器内部的含义，常作开发人员debug用途。

2) 在解释器直接输入a时默认调用repr()函数，而print a则调用str()函数

3) repr()的返回值一般可以用eval()函数来还原对象，通常有:
```
obj == eval(repr(obj))
```

但需要注意的是，这个等式不是所有情况都成立，如果用户重新实现的repr()方法如下。
```
>>> s = "' '"
>>> str(s)
"''"

>>> repr(s)
'"\' \'"'

>>> eval(repr(s)) == s
True

>>> eval(str(s))
' '

>>> eval(str(s)) == s
False
```

4) 这两个方法分别调用内建的__str__()和__repr__方法，一般来说在类中都应该定义__repr__()方法，而__str__()方法则为可选，当可读性比较重要的时候应该考虑定义__str__()方法。

### 35. 分清staticmethod 和 classmethod的适用场景

python中静态方法(staticmethod)和类方法(classmethod)都依赖于装饰器(decorator)来实现。

静态方法:
```
class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        pass
```

类方法；
```
class C(object):
    @classsmethod
    def f(cls, arg1, arg2, ...)
        pass
```

静态方法和类方法都可以通过类名.方法名（如C.f())或者实例.方法名(C().f())的形式来访问。
其中静态方法没有常规方法的特殊行为，如绑定，非绑定，隐式参数等规则，而类方法的调用使用类本身作为其隐含参数，但调用本身并不需要显示提供该参数。

```
class A(object):
    def instance_method(self, x):
        print("calling instance method instance_method(%s, %s)" % (self, x))

    @classmethod
    def class_method(cls, x):
        print("calling class_method(%s, %s)" % (cls, x))

    @staticmethod
    def static_method(x):
        print("calling static_method(%s)" % x)
a = A()
a.instance_method("test")
# 输出 calling instance method instance_method(<__main__.A object at 0x00D66B50>, test)

a.class_method("test")
# 输出 calling class_method(<class '__main__.A'>, test)

a.static_method("test")
# 输出 calling static_method(test)

```

上面的例子是类方法和静态方法的简单应用，从程序的输出可以看出岁让类方法在调用的时候没有显式声明cls, 但实际上类本身是作为隐含参数传入的。

问题: 为什么需要静态方法和类方法， 它们和实例方法之间存在什么区别呢？

答：假设有水果类Fruit, 它用属性total表示总量，Fruit中已经有方法set()来设置总量，
print_total()方法来打印水果数量。类Apple和类Orange继承自Fruit.
我们需要分别跟踪不同类型的水果的总量。

方法一： 利用普通的实例方法来实现
在Apple和Orange类中分别定义类变量total，然后再覆盖基类的set()和print_total()方法，但这会导致代码冗余，因为本质上这些方法所实现的功能相同
```
class Fruit(object):
    total = 0
    def __init__(self, name, total):
        self.name = name
        self.total = total
    def set(self, total):
        self.name = name
        self.total = total
    def print_total(self, total):
        print("name is: ", self.name, "total is: ", self.total")

apple = Fruit('Apple', '50')
orange = Fruit('Orange', '30')

```

方法二: 使用类方法实现
```
class Fruit(object):
    total = 0
    @classmethod
    def print_total(cls):
        print cls.total
        # prin(id(Fruit.total))
        # print(id(cls.total))
    
    @classmethod
    def set(cls, value):
        # print("calling class_method(%s, %s") % (cls, value))
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

app1 = Apple()
app1.set(200)

app2 = Apple()

org1 = Orange()
org1.set(300)

org2 = Orange()

app1.print_total() # output 200
org1.print_total() # output 300
```

删除上面代码中的注释语句后运行程序会得到以下结果:
```
calling class_method(<class '__main__.Apple'>, 200)
calling class_method(<class '__main__.Orange'>, 300)
200
12184820----->Fruit类的类变量
12186364----->动态生成的Apple类的类变量
300
12184820----->Fruit类的类变量
13810996----->动态生成的Orange类的类变量
```

简单分析:

针对不同种类的水果对象调用set()方法的时候，隐形传入的参数为该对象是哟对应的类，在调用set()的过程中动态生成了对应的类的类变量。这就是classmethod的妙处。

问题: 此处是否可以使用staticmethod方法?
答: 不可行

例子: 必须使用类方法而不是静态方法的例子: 假设对于每一个Fruit类我们提供三个实例属性: area表示区域代码，category表示种类代码，batch表示批次号。现在需要一个方法能够将area-category-batch形式表示的字符串形式输入转化为对应的属性并以对象的方式返回

假设Fruit有如下初始化方法，并且有静态方法Init_Product()能够满足上面所有的需求
```
def __init__(self, area="", categoty="", batch=""):
    self.area = area
    self.category = category
    self.batch = batch
    @staticmethod
    def Init_Product(product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = Fruit(area, category, batch)
        return fruit
```

使用静态方法带来的问题:
```
app1 = Apple(2, 5, 10)
org1 = Orange.Init_Product("3-3-9")

print("app1 is instance of Apple: "+str(isinstance(app1, Apple)))
print("org1 is instance of Orange: "+str(isinstance(org1, Orange)))
```

运行程序，发现isinstance(org1, Orange)的值为False.
因为静态方法相当于定义在类里面的函数，Init_Product返回的实际是Fruit的对象，所以它不会是Orange的实例。Init_Product()的功能类似于工厂方法，能欧根据不同类型返回对应的类的实例，因此使用静态方法并不能获得期望的结果， 类方法才是正确的解决方案, 修改如下:

```
@classmethod
def Init_Product(cls, product_info):
    area, category, batch = map(int, product_info.split('-'))
    fruit = Fruit(area, category, batch)
    return fruit
```

静态方法作用?什么情况下可以使用静态方法？

继续上面的例子, 假设我们还需要一个方法来验证输入的和合法性， 方法具体实现如下:
```
def is_input_valid(product_info):
    area, category, batch = map(int, product_info.split('-'))
    try:
        assert 0 <= area <= 10
        assert 0 <= category <= 15
        assert 0 <= batch <= 99
    except AssertionError:
        return False
    return True
```

那么应该将其声明为静态方法还是类方法呢？

答： 两者都可
甚至将其作为一个定义在类外部的函数都是可以的。最好的方式是声明为静态方法。

静态方法定义在类中，较之外部函数，能够更加有效的将代码阻止起来，从而使相关代码垂直距离接近，提高代码的可维护性。


