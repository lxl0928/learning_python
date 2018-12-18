# python必考的8个笔试题

[TOC]

### 1. 下面这段代码输出结果是什么？请解释
```
#! /usr/bin/env python3
# coding: utf-8

def extendList(val, test_list=[]):
    test_list.append(val)
    return test_list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = {0}".format(list1))
print("list2 = {0}".format(list2))
print("list3 = {0}".format(list3))

list1.append(100)
list2.append(200)
list3.append(300)


print("list1 = {0}".format(list1))
print("list2 = {0}".format(list2))
print("list3 = {0}".format(list3))
```

上面代码输出结果将是：
```
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
list1 = [10, 'a', 100, 300]
list2 = [123, 200]
list3 = [10, 'a', 100, 300]
```
解释：新的默认列表只在函数被定义的那一刻创建一次。
当extendList被没有指定特定参数list调用时，这组list的值随后将被使用。
这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在被调用时被计算。
因此，list1和list3是在同一个默认列表上进行操作计算的。
而list2是在一个分离的列表上进行操作计算的(通过传递一个自有的空列表作为列表参数的数值)。
简单解释: list=[]是一个可变对象，函数传参既不是传值也不是传引用，而是传递对象。
默认参数是函数的一个属性，当list1传递一个参数val时，list使用[]，当在函数内部append(val)后，默认参数为[val]。
后面list3使用的是修改后的默认参数[val]。内存使用同一块内存。
当list2定义时，直接使用指定的参数和内存。
```
def extendList(val, test_list=None):
    if test_list is None:
        test_list = []
    test_list.append(val)
    return test_list

print(extendList(10))
print(extendList(123, []))
print(extendList('a'))
```

这时结果变成: 
```
list1 = [10]
list2 = [123]
list3 = ['a']
```

### 2. 下面这段代码的输出是什么？请解释
```
def multipliers():
    return [lambda x: i*x for i in range(4)] # i的值已经确定为3，不管返回的函数是否调用，都已确定。

print([m(2) for m in multipliers()]) # m(2)表示调用匿名函数的返回结果m，传递值为2
```

答案：
```
[6,6,6,6]
```
原因：
上面代码输出的结果是[6, 6, 6, 6] (不是我们想的[0, 2, 4, 6])。

上述问题产生的原因是Python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内进行查找。因此，当任何由multipliers()返回的函数被调用时，i的值将在附近的范围进行查找。那时，不管返回的函数是否被调用，for循环已经完成，i被赋予了最终的值3。

因此，每次返回的函数乘以传递过来的值3，因为上段代码传过来的值是2，它们最终返回的都是6。(3*2)碰巧的是，《The Hitchhiker’s Guide to Python》也指出，在与lambdas函数相关也有一个被广泛被误解的知识点，不过跟这个case不一样。由lambda表达式创造的函数没有什么特殊的地方，它其实是和def创造的函数式一样的。

下面是解决这一问题的一些方法。
一种解决方法就是用Python生成器。

```
def multipliers():
  for i in range(4): yield lambda x : i * x
```

另外一个解决方案就是创造一个闭包，利用默认函数立即绑定。
```
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
```
还有种替代方案:
```
from functools import partial
from oprator import mul

def multipliers():
    return [partial(mul, i) for i in range(4)]
```

### 下面这段代码将输出什么？请解释
```
class Parent(object):
    x=1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```
结果如下:
```
1, 1, 1
1, 2, 1
3, 2, 3
```
解释：
让很多人困惑或惊讶的是最后一行输出为什么是3 2 3 而不是 3 2 1.为什么在改变parent.x的同时也改变了child2.x的值？但与此同时没有改变Child1.x的值？

此答案的关键是，在Python中，<code>类变量在内部是以字典的形式进行传递。</code>

如果一个变量名没有在当前类下的字典中发现。则在更高级的类（如它的父类）中尽心搜索直到引用的变量名被找到。（如果引用变量名在自身类和更高级类中没有找到，将会引发一个属性错误。）

因此,在父类中设定x = 1,让变量x类(带有值1)能够在其类和其子类中被引用到。这就是为什么第一个打印语句输出结果是1 1 1

因此，如果它的任何一个子类被覆写了值（例如说，当我们执行语句Child.x = 2）,这个值只在子类中进行了修改。这就是为什么第二个打印语句输出结果是1 2 1

最终，如果这个值在父类中进行了修改，（例如说，当我们执行语句Parent.x = 3）,这个改变将会影响那些还没有覆写子类的值（在这个例子中就是Child2）这就是为什么第三打印语句输出结果是3 2 3

### 下面这段代码在Python2中输出的结果是什么?
```
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)
```
在Python3下结果会有怎样的不同？（当然，假设上述打印语句被转换成Python3的语法）

在Python2中，上述代码输出将是
```
5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
```
默认情况下，Python 2 自动执行整形计算如果两者都是整数。因此,5/2 结果是2，而5./2结果是2.5

注意，在Python2中，你可以通过增加以下引用来覆写这个行为。
```
from future import division
```
同时要注意的是，//操作符将总是执行整形除法，不管操作符的类型。这就是为什么即使在Python 2中5.0//2.0的结果是2.0。然而在Python3中，没有此类特性，

例如，在两端都是整形的情况下，它不会执行整形除法

因此，在Python3中，将会是如下结果：
```
5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
```

### 下面代码的输出结果将是什么？
```
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]
```
下面的代码将输出[],不会产生IndexError错误。就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。

例如，尝试获取list[10]和之后的成员，会导致IndexError.

然而，尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError,而是仅仅返回一个空列表。
这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致bug很难被追踪到。

### 考虑下列代码片段：
```
1. list = [ [ ] ] * 5
2. list  # output?
3. list[0].append(10)
4. list  # output?
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output?
```
2,4,6,8行将输出什么结果？试解释。

输出的结果如下：
```
[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```
解释如下：
第一行的输出结果直觉上很容易理解，例如 list = [ [ ] ] * 5 就是简单的创造了5个空列表。然而，理解表达式list=[ [ ] ] * 5的关键一点是它不是创造一个包含五个独立列表的列表，而是它是一个创建了包含对同一个列表五次引用的列表。只有了解了这一点，我们才能更好的理解接下来的输出结果。

list[0].append(10) 将10附加在第一个列表上。

但由于所有5个列表是引用的同一个列表，所以这个结果将是：
```
[[10], [10], [10], [10], [10]]
```
同理，list[1].append(20)将20附加在第二个列表上。但同样由于5个列表是引用的同一个列表，所以输出结果现在是：
```
`[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]].`
```
作为对比， list.append(30)是将整个新的元素附加在外列表上，因此产生的结果是： [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

### Given a list of N numbers。
给定一个含有N个数字的列表。

使用单一的列表生成式来产生一个新的列表，该列表只包含满足以下条件的值：
(a)偶数值
(b)元素为原始列表中偶数切片。

例如，如果list[2]包含的值是偶数。那么这个值应该被包含在新的列表当中。因为这个数字同时在原始列表的偶数序列（2为偶数）上。然而，如果list[3]包含一个偶数，那个数字不应该被包含在新的列表当中，因为它在原始列表的奇数序列上。
对此问题的简单解决方法如下：
```
[x for x in list[::2] if x%2 == 0]
```

例如，给定列表如下：
```
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
```

列表生成式[x for x in list[::2] if x%2 == 0] 的结果是，
```
[10, 18, 78]
```

这个表达式工作的步骤是，第一步取出偶数切片的数字，
第二步剔除其中所有奇数。

8、下面的代码能够运行么？为什么？
给定以下字典的子类：
```
class DefaultDict(dict):
  def __missing__(self, key):
    return []
```
结果: 
```
d = DefaultDict()
d['florp'] = 127
```

能够运行。
当key缺失时，执行DefaultDict类，字典的实例将自动实例化这个数列。
