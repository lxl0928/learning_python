[TOC]

数据结构

数据结构的概念很好理解，就是用来将数据组织在一起的结构。换句话说，数据结构是用来存储一系列关联数据的东西。在Python中有四种内建的数据结构，分别是List、Tuple、Dictionary以及Set。大部分的应用程序不需要其他类型的数据结构，但若是真需要也有很多高级数据结构可供选择，例如Collection、Array、Heapq、Bisect、Weakref、Copy以及Pprint。本文将介绍这些数据结构的用法，看看它们是如何帮助我们的应用程序的。

关于四种内建数据结构的使用方法很简单，并且网上有很多参考资料，因此本文将不会讨论它们。

1. Collections

collections模块包含了内建类型之外的一些有用的工具，例如Counter、defaultdict、OrderedDict、deque以及nametuple。其中Counter、deque以及defaultdict是最常用的类。

1.1 Counter()

如果你想统计一个单词在给定的序列中一共出现了多少次，诸如此类的操作就可以用到Counter。来看看如何统计一个list中出现的item次数：
```
from collections import Counter
 
li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
a = Counter(li)
print a # Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
```
若要统计一个list中不同单词的数目，可以这么用：
```
from collections import Counter
 
li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
a = Counter(li)
print a # Counter({'Dog': 3, 42: 2, 'Cat': 2, 'Mouse': 1})
 
print len(set(li)) # 4
```
如果需要对结果进行分组，可以这么做：
```
from collections import Counter
 
li = ["Dog", "Cat", "Mouse","Dog","Cat", "Dog"]
a = Counter(li)
 
print a # Counter({'Dog': 3, 'Cat': 2, 'Mouse': 1})
 
print "{0} : {1}".format(a.values(),a.keys())  # [1, 3, 2] : ['Mouse', 'Dog', 'Cat']
 
print(a.most_common(3)) # [('Dog', 3), ('Cat', 2), ('Mouse', 1)]
```
以下的代码片段找出一个字符串中出现频率最高的单词，并打印其出现次数。
![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0XbHM3WVtcYSH8powBlCWVgFkbaPdR2p36yzxwcrZ6Ng6TYdQhK9F0Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

1.2 Deque

Deque是一种由队列结构扩展而来的双端队列(double-ended queue)，队列元素能够在队列两端添加或删除。因此它还被称为头尾连接列表(head-tail linked list)，尽管叫这个名字的还有另一个特殊的数据结构实现。

Deque支持线程安全的，经过优化的append和pop操作，在队列两端的相关操作都能够达到近乎O(1)的时间复杂度。虽然list也支持类似的操作，但是它是对定长列表的操作表现很不错，而当遇到pop(0)和insert(0, v)这样既改变了列表的长度又改变其元素位置的操作时，其复杂度就变为O(n)了。

来看看相关的比较结果：
![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0iaOx6AlbNgJsfufVvItD1XCTuHlFD1Qtibh42wGnO9ibvBAwRMOXb4Elg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)


另一个例子是执行基本的队列操作：
```
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q
print q.pop()
print q.popleft()
print q.rotate(3)
print q
print q.rotate(-1)
print q
 
# deque([6, 0, 1, 2, 3, 4, 5])
# 5
# 6
# None
# deque([2, 3, 4, 0, 1])
# None
# deque([3, 4, 0, 1, 2])
```
译者注:rotate是队列的旋转操作，Right rotate(正参数)是将右端的元素移动到左端，而Left rotate(负参数)则相反。

1.3 Defaultdict

这个类型除了在处理不存在的键的操作之外与普通的字典完全相同。当查找一个不存在的键操作发生时，它的default_factory会被调用，提供一个默认的值，并且将这对键值存储下来。其他的参数同普通的字典方法dict()一致，一个defaultdict的实例同内建dict一样拥有同样地操作。

defaultdict对象在当你希望使用它存放追踪数据的时候很有用。举个例子，假定你希望追踪一个单词在字符串中的位置，那么你可以这么做：
```
from collections import defaultdict
 
s = "the quick brown fox jumps over the lazy dog"
 
words = s.split()
location = defaultdict(list)
for m, n in enumerate(words):
    location[n].append(m)
 
print location
 
# defaultdict(<type 'list'>, {'brown': [2], 'lazy': [7], 'over': [5], 'fox': [3],
# 'dog': [8], 'quick': [1], 'the': [0, 6], 'jumps': [4]})
```
是选择lists或sets与defaultdict搭配取决于你的目的，使用list能够保存你插入元素的顺序，而使用set则不关心元素插入顺序，它会帮助消除重复元素。
```
from collections import defaultdict
 
s = "the quick brown fox jumps over the lazy dog"
 
words = s.split()
location = defaultdict(set)
for m, n in enumerate(words):
    location[n].add(m)
 
print location
 
# defaultdict(<type 'set'>, {'brown': set([2]), 'lazy': set([7]), 
# 'over': set([5]), 'fox': set([3]), 'dog': set([8]), 'quick': set([1]), 
# 'the': set([0, 6]), 'jumps': set([4])})
```
另一种创建multidict的方法：
```
s = "the quick brown fox jumps over the lazy dog"
d = {}
words = s.split()
 
for key, value in enumerate(words):
    d.setdefault(key, []).append(value)
print d
 
# {0: ['the'], 1: ['quick'], 2: ['brown'], 3: ['fox'], 4: ['jumps'], 5: ['over'], 6: ['the'], 7: ['lazy'], 8: ['dog']}
```
一个更复杂的例子：
```
class Example(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
 
a = Example()
 
a[1][2][3] = 4
a[1][3][3] = 5
a[1][2]['test'] = 6
 
print a # {1: {2: {'test': 6, 3: 4}, 3: {3: 5}}}
```
2. Array

array模块定义了一个很像list的新对象类型，不同之处在于它限定了这个类型只能装一种类型的元素。array元素的类型是在创建并使用的时候确定的。

如果你的程序需要优化内存的使用，并且你确定你希望在list中存储的数据都是同样类型的，那么使用array模块很合适。举个例子，如果需要存储一千万个整数，如果用list，那么你至少需要160MB的存储空间，然而如果使用array，你只需要40MB。但虽然说能够节省空间，array上几乎没有什么基本操作能够比在list上更快。

在使用array进行计算的时候，需要特别注意那些创建list的操作。例如，使用列表推导式(list comprehension)的时候，会将array整个转换为list，使得存储空间膨胀。一个可行的替代方案是使用生成器表达式创建新的array。看代码：
```
import array
 
a = array.array("i", [1,2,3,4,5])
b = array.array(a.typecode, (2*x for x in a))
```
因为使用array是为了节省空间，所以更倾向于使用in-place操作。一种更高效的方法是使用enumerate：
```
import array
 
a = array.array("i", [1,2,3,4,5])
for i, x in enumerate(a):
    a[i] = 2*x
```
对于较大的array，这种in-place修改能够比用生成器创建一个新的array至少提升15%的速度。

那么什么时候使用array呢？是当你在考虑计算的因素之外，还需要得到一个像C语言里一样统一元素类型的数组时。
```
import array
from timeit import Timer
 
def arraytest():
    a = array.array("i", [1, 2, 3, 4, 5])
    b = array.array(a.typecode, (2 * x for x in a))
 
def enumeratetest():
    a = array.array("i", [1, 2, 3, 4, 5])
    for i, x in enumerate(a):
        a[i] = 2 * x
 
if __name__=='__main__':
    m = Timer("arraytest()", "from __main__ import arraytest")
    n = Timer("enumeratetest()", "from __main__ import enumeratetest")
 
    print m.timeit() # 5.22479210582
    print n.timeit() # 4.34367196717
```
3. Heapq

heapq模块使用一个用堆实现的优先级队列。堆是一种简单的有序列表，并且置入了堆的相关规则。

堆是一种树形的数据结构，树上的子节点与父节点之间存在顺序关系。二叉堆(binary heap)能够用一个经过组织的列表或数组结构来标识，在这种结构中，元素N的子节点的序号为2*N+1和2*N+2(下标始于0)。简单来说，这个模块中的所有函数都假设序列是有序的，所以序列中的第一个元素(seq[0])是最小的，序列的其他部分构成一个二叉树，并且seq[i]节点的子节点分别为seq[2*i+1]以及seq[2*i+2]。当对序列进行修改时，相关函数总是确保子节点大于等于父节点。
```
import heapq
 
heap = []
 
for value in [20, 10, 30, 50, 40]:
    heapq.heappush(heap, value)
 
while heap:
    print heapq.heappop(heap)
```
heapq模块有两个函数nlargest()和nsmallest()，顾名思义，让我们来看看它们的用法。
```
import heapq
 
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
```
两个函数也能够通过一个键参数使用更为复杂的数据结构，例如：
```
import heapq
 
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
 
print cheap
 
# [{'price': 16.35, 'name': 'YHOO', 'shares': 45},
# {'price': 21.09, 'name': 'FB', 'shares': 200}, {'price': 31.75, 'name': 'HPQ', 'shares': 35}]
 
print expensive
 
# [{'price': 543.22, 'name': 'AAPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 
# 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}]
```
来看看如何实现一个根据给定优先级进行排序，并且每次pop操作都返回优先级最高的元素的队列例子。

![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo07LNoKlhcvuLxoMzpmU0yPAgZfXGW0pxia3aNib8W1Iwv1yraWJIzrAJw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

4. Bisect

bisect模块能够提供保持list元素序列的支持。它使用了二分法完成大部分的工作。它在向一个list插入元素的同时维持list是有序的。在某些情况下，这比重复的对一个list进行排序更为高效，并且对于一个较大的list来说，对每步操作维持其有序也比对其排序要高效。

假设你有一个range集合：
```
a = [(0, 100), (150, 220), (500, 1000)]
```
如果我想添加一个range (250, 400)，我可能会这么做：
```
import bisect
 
a = [(0, 100), (150, 220), (500, 1000)]
 
bisect.insort_right(a, (250,400))
 
print a # [(0, 100), (150, 220), (250, 400), (500, 1000)]
```
我们可以使用bisect()函数来寻找插入点：
```
import bisect
 
a = [(0, 100), (150, 220), (500, 1000)]
 
bisect.insort_right(a, (250,400))
bisect.insort_right(a, (399, 450))
print a # [(0, 100), (150, 220), (250, 400), (500, 1000)]
 
print bisect.bisect(a, (550, 1200)) # 5
```
bisect(sequence, item) => index 返回元素应该的插入点，但序列并不被修改。
```
import bisect
 
a = [(0, 100), (150, 220), (500, 1000)]
 
bisect.insort_right(a, (250,400))
bisect.insort_right(a, (399, 450))
print a # [(0, 100), (150, 220), (250, 400), (500, 1000)]
 
print bisect.bisect(a, (550, 1200)) # 5
bisect.insort_right(a, (550, 1200))
print a # [(0, 100), (150, 220), (250, 400), (399, 450), (500, 1000), (550, 1200)]
```
新元素被插入到第5的位置。

5. Weakref

weakref模块能够帮助我们创建Python引用，却不会阻止对象的销毁操作。这一节包含了weak reference的基本用法，并且引入一个代理类。

在开始之前，我们需要明白什么是strong reference。strong reference是一个对对象的引用次数、生命周期以及销毁时机产生影响的指针。strong reference如你所见，就是当你将一个对象赋值给一个变量的时候产生的：
```
>>> a = [1,2,3]
>>> b = a
```
在这种情况下，这个列表有两个strong reference，分别是a和b。在这两个引用都被释放之前，这个list不会被销毁。
```
class Foo(object):
    def __init__(self):
        self.obj = None
        print 'created'
 
    def __del__(self):
        print 'destroyed'
 
    def show(self):
        print self.obj
 
    def store(self, obj):
        self.obj = obj
 
a = Foo() # created
b = a
del a
del b # destroyed
```
Weak reference则是对对象的引用计数器不会产生影响。当一个对象存在weak reference时，并不会影响对象的撤销。这就说，如果一个对象仅剩下weak reference，那么它将会被销毁。

你可以使用weakref.ref函数来创建对象的weak reference。这个函数调用需要将一个strong reference作为第一个参数传给函数，并且返回一个weak reference。
```
>>> import weakref
>>> a = Foo()
created
>>> b = weakref.ref(a)
>>> b
```
一个临时的strong reference可以从weak reference中创建，即是下例中的b()：
```
>>> a == b() 
True
>>> b().show()
None
```
请注意当我们删除strong reference的时候，对象将立即被销毁。
```
>>> del a
destroyed
```
如果试图在对象被摧毁之后通过weak reference使用对象，则会返回None：
```
>>> b() is None
True
```
若是使用weakref.proxy，就能提供相对于weakref.ref更透明的可选操作。同样是使用一个strong reference作为第一个参数并且返回一个weak reference，proxy更像是一个strong reference，但当对象不存在时会抛出异常。
```
>>> a = Foo()
created
>>> b = weakref.proxy(a)
>>> b.store('fish')
>>> b.show()
fish
>>> del a
destroyed
>>> b.show()
Traceback (most recent call last):
  File "", line 1, in ?
ReferenceError: weakly-referenced object no longer exists
```
完整的例子：

引用计数器是由Python的垃圾回收器使用的，当一个对象的应用计数器变为0，则其将会被垃圾回收器回收。

最好将weak reference用于开销较大的对象，或避免循环引用(虽然垃圾回收器经常干这种事情)。
```
import weakref
import gc
 
class MyObject(object):
    def my_method(self):
        print 'my_method was called!'
 
obj = MyObject()
r = weakref.ref(obj)
 
gc.collect()
assert r() is obj #r() allows you to access the object referenced: it's there.
 
obj = 1 #Let's change what obj references to
gc.collect()
assert r() is None #There is no object left: it was gc'ed.
```
提示：只有library模块中定义的class instances、functions、methods、sets、frozen sets、files、generators、type objects和certain object types(例如sockets、arrays和regular expression patterns)支持weakref。内建函数以及大部分内建类型如lists、dictionaries、strings和numbers则不支持。

6. Copy()

通过shallow或deep copy语法提供复制对象的函数操作。

shallow和deep copying的不同之处在于对于混合型对象的操作(混合对象是包含了其他类型对象的对象，例如list或其他类实例)。

对于shallow copy而言，它创建一个新的混合对象，并且将原对象中其他对象的引用插入新对象。
对于deep copy而言，它创建一个新的对象，并且递归地复制源对象中的其他对象并插入新的对象中。

普通的赋值操作知识简单的将心变量指向源对象。
![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0XvLxupwlvmUwvcIiaflib2ApX5zxicNiaD0s2GbV0lRIE5SHia9zTz0ia7Hg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

shallow copy (copy())操作创建一个新的容器，其包含的引用指向原对象中的对象。

deep copy (deepcopy())创建的对象包含的引用指向复制出来的新对象。

复杂的例子：

假定我有两个类，名为Manager和Graph，每个Graph包含了一个指向其manager的引用，而每个Manager有一个指向其管理的Graph的集合，现在我们有两个任务需要完成：

1) 复制一个graph实例，使用deepcopy，但其manager指向为原graph的manager。

2) 复制一个manager，完全创建新manager，但拷贝原有的所有graph。

![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0aoQgdvYjNqN2QYhPXjiaGXuU0NRmPAQUTichZHyGy1PHJo5cSx7udJEg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)


7. Pprint()

Pprint模块能够提供比较优雅的数据结构打印方式，如果你需要打印一个结构较为复杂，层次较深的字典或是JSON对象时，使用Pprint能够提供较好的打印结果。

假定你需要打印一个矩阵，当使用普通的print时，你只能打印出普通的列表，不过如果使用pprint，你就能打出漂亮的矩阵结构

如果
``
import pprint
 
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
a = pprint.PrettyPrinter(width=20)
a.pprint(matrix)
 
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
```
额外的知识

一些基本的数据结构

1. 单链链表

![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0tLJWWyWGsymsTTXGAiaHAcsjLiciaZSo4wibjXK05bV2pAu85BF4wicA7Gw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

2. 用Python实现的普林姆算法

译者注：普林姆算法(Prims Algorithm)是图论中，在加权连通图中搜索最小生成树的算法。

![test](http://mmbiz.qpic.cn/mmbiz_png/fhujzoQe7TpXpRObNPvDNicxsFFqLhVo0m1p547IXxLu8Yaib1HQuXw6JENAkZbtOZFtSZCddqfql8xgW1zDznYA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)