## 编写高质量代码(改善Python程序的91个建议)_4: 库

[TOC]

### 36. 掌握字符串的基本用法

判断一个变量s是不是字符串应该使用isinstance(s, basestring), 注意这里的参数是basestring而不是str.
```
>>> a = "hi"
>>> isinstance(a, str)    # ....①
True
>>> b = u"hi"
>>> isinstance(b, str)    # ....②
False

>>> isinstance(b, basestring)
True

>>> isinstance(b, unicode)
True

>>> isinstance(a, unicode)
False

```

1) 字符串-性质判定

str对象有以下几个方法: isalnum(), isalpah(), isdigit(), islower(), isupper(), isspace(), istitle(), startswith(prefix[, start[, end]]), endswith(suffix[,start[,end]]), 前面几个is*()形式的函数很简单故名思议无非就是判定是否是数字，字母，大小写，空白符， istitle()是判定字符串是否每个单词的首字母有且只有首字母是大写。

```
>>> assert "Hello World!".istitle() == True
>>> assert "HEllo World!".istitle() == False
```

需要注意的是*with()函数族的prefix参数可以接受tuple类型的实参，当实参中的某个元素能够匹配时，返回True

2) 查找替换

count( sub[, start[, end]]),
find( sub[, start[, end]]),
index( sub[, start[, end]]),
rfind( sub[, start[, end]]),
rindex( sub[, start[, end]])
这些方法都接受start, end参数， 善加利用，可以优化性能。
其中count()能够查找子串sub在字符串中出现的次数，这个数值在调用replace方法的时候用得着。
此外，需要注意find()和index()方法的不同:
find()函数族找不到时放回-1, index()函数族则抛出ValueError异常。
但对于判定是否包含子串的判定并不推荐调用这些方法，而是推荐使用in和not in操作符。
```
>>> str = "Test if a string contains some special substrings"
>>> if str.find("some") != -1: # 使用find方法进行判定
...     print("Yes, it contains")

Yes, it contains

>>> if "some" in str: # 使用in或者not in操作符
...     print("Yes, it contains using in"

Yes, it contains using in

```

replace(old, new[, count])用以替换字符串的某些子串，如果指定count参数的话，就最多替换xount次，如果不指定，就会全部替换

3) 分切与连接

在这里主要讲分切:
partition(sep),
rpartition(sep),
splitlines([keepends]),
split([sep [, maxsplit]]),
rsplit([sep[, maxsplit]])

别看这些方法好像很多，其实至于弄清楚partition()和split()就可以了。

*partition()函数族是python2.5版本新增的方法，它接受一个字符串参数，并返回一个3个元素组成的元组对象。
如果sep没有出现中母串中，返回值是(sep, ","); 否则，返回的第一个元素是sep左端的部分，第二个元素是sep自身，第三个元素是sep右端部分。
而split()的参数maxsplit是分切的次数，即最大分切次数，所以返回值最多有maxsplit+1个元素。
但split()有不少小陷阱，需要注意。

比如，对字符串s, s.split(), s.split(")的返回值是不相同的。

```
>>> ' hello world!'.split()
['hello', 'world!']

>>> '  hello  world!'.split(' ')
['', '', 'hello', '', '', 'world!']

```
产生差异源于: 当忽略sep参数或者sep参数为None时与明确给sep富裕字符串值时，split()采用两种不同的算法。对于前者，split()先去除字符串两端的空白符，然后以任意长度的空白符作为界定符分切字符串（即连续的空白符串被当作单一的空白符看待）；对于后者则认为两个连续的sep之间存在一个空字符串。
因此对于空字符串(或者空白字符串)，它们返回值也不同:
```
>>> ''.split()
[]

>>> ''.split(' ')
['']
```

4) 变形

lower(),
upper(),
capitalize(),
swapcase(),
title()
。
其中title()函数并不去除字符串两端的空白符也不会把连续的空白符替换为一个空格，所以不能把title()理解为先以空白符分切字符串，然后调用capitalize()处理每个字词以使其首字母大写，再用空格将它们直接连接在一起。

如果你有这样的需求，建议使用string模块中的capwords(s)函数，它能够去除两端的空白符，再将空白符用一个空格代替。
```
>>> ' hello  world'.title()
' Hello World'

>>> string.capwords(' hello world')
' Hello World'

```

5) 删减与填充

删减在文本处理是很常用，我们常常得把字符串掐头去尾，就用得上它们。

如果strip([chars]), lstrip([chars]), rstrip([chars])中的chars参数没有指定，就是删除空白符，空白符由string.whitespace常量定义。

填充则常用于字符串的输出，借助他们能够排出漂亮的排版

center(width[, fillchar]), 居中
ljust(width[, fillchar]), 左对齐
rjust(width[, fillchar]), 右对齐
zfill(width), expandtabs([tabsize]). 以字符串0进行填充
expandtabs默认tab是8， 它的功能是把字符串中的制表符(tab)转换为适当数量的空格。



### 37. 按需选择sort()或者sorted()

1) 相比于sort()，sorted()使用范围更为广泛，两者的函数形式分别如下:
```
sorted(iterable[, cmp[, key[, reverse]]])

s.sort([cmp[, key[, reverse]]])
```
这两个方法有以下三个共同的参数:
```
1. cmp为用户定义的任何比较函数

2. key是带一个参数的函数，用来为每个元素提取比较值，默认为None(即直接比较每个元素)

3. reverse表示排序结果是否反转


```
从函数的定义形式可以看出，sorted()作用域任意可迭代的对象，而sort()一般作用域列表。

2) 当排序对象为列表的时候，两者适应的场景不同。

sorted()函数实在python2.4后加入的。在这之前智游sort()函数。
sorted()函数返回一个排序后的列表，原有列表保持不变，而sort()函数会直接修改原来的列表，函数返回为None.

3) 无论是sort()函数函数sorted()函数，传入参数key比传入参数cmp效率要高。

4) sorted()函数功能非常强大，使用它可以方便的针对不同的数据结构进行排序，从而满足不同的需求。
例子:
```
  1) 对字典进行给你排序：下面的例子中根据自定的值进行排序，即将phonebook对应的电话号码按照数字大小进行排序。
>>> phonebook = { "Linda": '7750', "Bob": '9345', "Carot": '5834' }
>>> from operator import itemgetter
>>> sorted_pb = soeted(phonebook.iteritems(), key=itemgetter(1))
>>> print(sorted_pb)
[('Carot', '5834), ('Linda', '7750'), ('Bob', '9345')]
```
  2) 多维list排序: 实际情况下也会碰到需要对多个字段进行排序的情况，如根据学生的成绩，对应的等级进行依次排序。
>>> from operator import itemgetter
>>> gameresult = [['Bob', 95.00, 'A'], ['Alan', 86.0, 'C'], ['Mandy', 82.5, 'A'], ['Rob', 86, 'E']]
>>> sorted(gamereult, key=operator.itemgetter(2, 1))
[['Mandy', 82.5, 'A'], ['Bob', 85.0, 'A'], ['Alan', 86.0, 'C'], ['Rob', 86, 'E']] #当第二个字段成绩相同的时候按照等级从低到高排序

  3) 字典中混合list排序: 如果字典中的key或者值为列表，需要对列表中的某一个位置的元素排序也是可以做到的，下面的例子中针对字典mydict的value结构[n, m]中的m按照从小到大的顺序排列
>>> mydict = {
    'Li': ['M', 7],
    'Zhang': ['E', 2],
    'Wang': ['P', 3],
    'Du': ['C', 2],
    'Ma': ['C', 9],
    'Zhe': ['H', 7]
}
>>>
>>> from operator import itemgetter
>>> sorted(mydict.iteritems(), key=lambda (k, v): operator.itemgetter(1)(v))
[('Zhang', ['E', 2]), ('Du', ['C', 2]), ('Wang', ['P', 3]), ('Li', ['M', 7]), ('Zhe', ['H', 7]), ('Ma', ['C', 9])]

  4) List中混合字典排序: 如果列表中的每一个元素为字典形式，需要针对字典的多个key值进行排序也不难实现。下面例子是针对list中的字典元素按照rating和name进行排序的实现方法。
  >>> gameresult = [{"name":"Bob", "wins":10, "losses":3, "rating":75.00},
                    {"name":"David", "wins":3, "losses":5, "rating":57.00},
                    {"name":"Carol", "wins":4, "losses":5, "rating":57.00},
                    {"name":"Parry", "wins":9, "losses":3, "rating":71.48}]
  >>> from operator import itemgetter
  >>> sorted(gameresult, key=operator.itemgetter("rating", "name"))
  >>> [{"wins":4, "losses":5, 'name':'Carol', "rating":57.00},
       {"wins":3, "losses":5, "name":"David", "rating":57.00},
       {"wins":9, "losses":3, "name":"Patty", "rating":71.48},
       {"wins":10, "lossws":3, "name":"Bob", "rating":75.00}]

### 38. 使用copy模块深拷贝对象

讨论copy与deepcopy的区别这个问题要先搞清楚python中的引用、python的内存管理。

python中的一切事物皆为对象，并且规定参数的传递都是对象的引用。可能这样说听起来比较难懂。参考下面一段引用：

1.Python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。实际上，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值——相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象——相当于通过“传值”来传递对象。

2.当人们复制列表或字典时，就复制了对象列表的引用，如果改变引用的值，则修改了原始的参数。

3.为了简化内存管理，Python通过引用计数机制实现自动垃圾回收功能，Python中的每个对象都有一个引用计数，用来计数该对象在不同场所分别被引用了多少次。每当引用一次Python对象，相应的引用计数就增1，每当消毁一次Python对象，则相应的引用就减1，只有当引用计数为零时，才真正从内存中删除Python对象。

所谓“传值”也就是赋值的意思了。那么python参数传递有什么特殊呢？看例子：

```
>>> seq = [1, 2, 3]
>>> seq_2 = seq
>>> seq_2.append(4)
>>> print seq, seq_2
[1, 2, 3, 4] [1, 2, 3, 4]
>>> seq.append(5)
>>> print seq, seq_2
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
```
如果按照传统的观念，seq和seq_2这两个变量对应两个不同的存储地址，自然对应不同的值，是毫无关联的，但是在python中确令我们大跌眼镜。再看下面的例子：

```
>>> a = 1
>>> b = a
>>> b = 2
>>> print a, b
1 2
>>> c = (1, 2)
>>> d = c
>>> d = (1, 2, 3)
>>> print c, d
(1, 2) (1, 2, 3)
```

显然和上面的例子有冲突吗？看开头引用的话就明白了，当引用的原始对象改变的时候，他俩就没有关系了，也就是说他俩是两个不同对象的引用，对应各自引用计数加减1；而第一个例子中seq和seq_2都是对原始对象[1, 2, 3]这个lis对象的引用，所以不管append()还是pop()都不会改变原始对象，只是改变了它的元素，这样也就不难理解第二个例子了，因为b = 2就是创建了一个新的 int 对象。
接下来再通过例子看copy与deepcopy的区别：
```
>>> seq = [1, 2, 3]
>>> seq_1 = seq
>>> seq_2 = copy.copy(seq)
>>> seq_3 = copy.deepcopy(seq)
>>> seq.append(4)
>>> print seq, seq_1, seq_2, seq_3
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3] [1, 2, 3]
>>> seq_2.append(5)
>>> print seq, seq_1, seq_2, seq_3
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 5] [1, 2, 3]
>>> seq_3.append(6)
>>> print seq, seq_1, seq_2, seq_3
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 5] [1, 2, 3, 6]
```

这个例子看不出copy之后和之前的联系，也看不出copy与deepcopy的区别。那么再看：
```
>>> m = [1, ['a'], 2]
>>> m_1 = m
>>> m_2 = copy.copy(m)
>>> m_3 = copy.deepcopy(m)
>>> m[1].append('b')
>>> print m, m_1, m_2, m_3
[1, ['a', 'b'], 2] [1, ['a', 'b'], 2] [1, ['a', 'b'], 2] [1, ['a'], 2]
>>> m_2[1].append('c')
>>> print m, m_1, m_2, m_3
[1, ['a', 'b', 'c'], 2] [1, ['a', 'b', 'c'], 2] [1, ['a', 'b', 'c'], 2] [1, ['a'], 2]
>>> m_3[1].append('d')
>>> print m, m_1, m_2, m_3
[1, ['a', 'b', 'c'], 2] [1, ['a', 'b', 'c'], 2] [1, ['a', 'b', 'c'], 2] [1, ['a', 'd'], 2]
```

从这就看出来区别了，copy拷贝一个对象，但是对象的属性还是引用原来的，deepcopy拷贝一个对象，把对象里面的属性也做了拷贝，deepcopy之后完全是另一个对象了。再看一个例子：
```
>>> m = [1, [2, 2], [3, 3]]
>>> n = copy.copy(m)
>>> n[1].append(2)
>>> print m, n
[1, [2, 2, 2], [3, 3]] [1, [2, 2, 2], [3, 3]]
>>> n[1] = 0
>>> print m, n
[1, [2, 2, 2], [3, 3]] [1, 0, [3, 3]]
>>> n[2].append(3)
>>> print m, n
[1, [2, 2, 2], [3, 3, 3]] [1, 0, [3, 3, 3]]
>>> m[1].pop()
2
>>> print m, n
[1, [2, 2], [3, 3, 3]] [1, 0, [3, 3, 3]]
>>> m[2].pop()
3
>>> print m, n
[1, [2, 2], [3, 3]] [1, 0, [3, 3]]
```

### 39. 使用Counter进行计数统计

计数统计就是统计某一项出现的次数。实际应用中很多需求需要用到这个模型。比如测试样本中某一指出现的次数、日志分析中某一消息出现的频率等等‘这种类似的需求有很多实现方法。下面就列举几条。

1) 使用dict.
看下面代码:
```
# coding = utf-8
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = dict()
for one in data:
     if one in count_frq:
          count_frq[one] += 1
     else:
          count_frq[one] = 1

print count_frq
```

输出结果如下：
```
{'a': 3, 2: 1, 'b': 1, 4: 2, 5: 2, 7: 1, '2': 2, 'z': 1, 'd': 1}
```
这种方法最简单，也是最容易想到的，鄙人这写这篇博文之前用的最多，不过以后应该不会用来，我们应该使代码更加Pythonic.

2) 使用set和list.
代码如下:
```
# coding = utf-8
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
data_set = set(data)
count_list = []
for one in data_set:
     count_list.append((one, data.count(one)))

print count_list
```

输出结果如下：
```
[('a', 3), (2, 1), ('b', 1), (4, 2), (5, 2), (7, 1), ('2', 2), ('z', 1), ('d', 1)]
````
这里面利用了list的通用方法和集合(set)的特性，集合是一个无序不重复的元素集，而工厂函数set()可以将列表转换为一个无序不重复的元素集合。

3) Counter类
以上方法都很简单，但不够Pythonic。下面来介绍collections中的Counter类。

Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）支持集合操作+、-、&、|，其中&、|操作分别返回两个Counter对象各元素的最大值和最小值。

  3.1 Counter的初始化
```
c = Counter("hello world")         #可迭代对象创建

c = Counter(h=1, l=3, o=2)           #关键字创建

c = Counter({'h':1, 'l':3, 'o':2})   #字典创建

c = Counter()                      #空Counter类
```
  3.2 Counter类常见方法
```
elements()：返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。所有元素按照字母序排序，个数小于1的元素不被包含。

update()：用于统计对象元素的更新，原有的Counter计数器对象与新增元素的统计计数值相加而不是直接替换。

subtract()：该方法用于计数器对象中元素统计值减少，输入输出的统计值书可以为0或者负数的。

most_common([n])：可以查找出前n个出现频率最高的元素以及它们对于的次数，也就是说频率搞的排在最前面。

copy()：浅拷贝。
```

所以上面的例子用Counter类的话，也很简单，代码如下：
```
#coding = utf-8
from collections import Counter
data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
c = Counter(data)
print c
```
输出结果如下：
```
Counter({'a': 3, 4: 2, 5: 2, '2': 2, 2: 1, 'b': 1, 7: 1, 'z': 1, 'd': 1})
```

  3.3 算术和集合操作
```
#coding = utf-8
from collections import Counter
data = ['a', '2', '2', 'b', 'a', 'd', 'a']
c = Counter(data)
b = Counter(a=1, b=2)
print c
print b
print b+c     # c[x] + d[x]
print c-b     # subtract（只保留正数计数的元素）
print c&b     # 交集:  min(c[x], d[x])
print c|b     # 并集:  max(c[x], d[x])
```
输出结果如下：

```
Counter({'a': 3, '2': 2, 'b': 1, 'd': 1})

Counter({'b': 2, 'a': 1})

Counter({'a': 4, 'b': 3, '2': 2, 'd': 1})

Counter({'a': 2, '2': 2, 'd': 1})

Counter({'a': 1, 'b': 1})

Counter({'a': 3, '2': 2, 'b': 2, 'd': 1})
```

  3.4 其它

Counter类返回值跟字典很类似，所以字典类的方法对Counter对象也适用。如下：
```
# coding = utf-8
from collections import Counter
data = ['a', '2', 2,4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
c = Counter(data)
print c.keys()
print c.has_key('a')
print c.get('a')
print c.items()
print c.values()
print c.viewitems()
print c.viewkeys()
```

输出如下：
```
['a', 2, 'b', 4, 5, 7, '2', 'z', 'd']
True
3
[('a', 3), (2, 1), ('b', 1), (4, 2), (5, 2), (7, 1), ('2', 2), ('z', 1), ('d', 1)]
[3, 1, 1, 2, 2, 1, 2, 1, 1]
dict_items([('a', 3), (2, 1), ('b', 1), (4, 2), (5, 2), (7, 1), ('2', 2), ('z', 1), ('d', 1)])
dict_keys(['a', 2, 'b', 4, 5, 7, '2', 'z', 'd'])
```
这只是其中一部分，其它的方法可以参考字典类的方法。
另外，Counter对象还支持工厂函数操作set()、list()、dict().


### 40. 深入掌握ConfigParser

1) 基本的读取配置文件
```
-read(filename) 直接读取ini文件内容
-sections() 得到所有的section，并以列表的形式返回
-options(section) 得到该section的所有option
-items(section) 得到该section的所有键值对
-get(section,option) 得到section中option的值，返回为string类型
-getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
```

2) 基本的写入配置文件
```
-add_section(section) 添加一个新的section
-set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。
```

3) 基本例子

test.cnf
```
[sec_a]
a_key1 = 20
a_key2 = 10

[sec_b]
b_key1 = 121
b_key2 = b_value2
b_key3 = $r
b_key4 = 127.0.0.1
```

parse_test_conf.py
```
import ConfigParser
cf = ConfigParser.ConfigParser()
# read config
cf.read("test.conf")
# return all section
secs = cf.sections()
print 'sections:', secs

opts = cf.options("sec_a")
print 'options:', opts

kvs = cf.items("sec_a")
print 'sec_a:', kvs

# read by type
str_val = cf.get("sec_a", "a_key1")
int_val = cf.getint("sec_a", "a_key2")

print "value for sec_a's a_key1:", str_val
print "value for sec_a's a_key2:", int_val

# write config
# update value
cf.set("sec_b", "b_key3", "new-$r")
# set a new value
cf.set("sec_b", "b_newkey", "new-value")
# create a new section
cf.add_section('a_new_section')
cf.set('a_new_section', 'new_key', 'new_value')

# write back to configure file
cf.write(open("test.conf", "w"))
```
得到终端输出：
```
sections: ['sec_b', 'sec_a']
options: ['a_key1', 'a_key2']
sec_a: [('a_key1', "i'm value"), ('a_key2', '22')]
value for sec_a's a_key1: i'm value
value for sec_a's a_key2: 22
```

更新后的test.conf
```
[sec_b]
b_newkey = new-value
b_key4 = 127.0.0.1
b_key1 = 121
b_key2 = b_value2
b_key3 = new-$r

[sec_a]
a_key1 = i'm value
a_key2 = 22

[a_new_section]
new_key = new_value
```

4) Python的ConfigParser Module中定义了3个类对INI文件进行操作。分别是RawConfigParser、ConfigParser、SafeConfigParser。RawCnfigParser是最基础的INI文件读取类，ConfigParser、SafeConfigParser支持对%(value)s变量的解析。

设定配置文件test2.conf
```
[portal]
url = http://%(host)s:%(port)s/Portal
host = localhost
port = 8080
```

使用RawConfigParser：
```
import ConfigParser

cf = ConfigParser.RawConfigParser()

print "use RawConfigParser() read"
cf.read("test2.conf")
print cf.get("portal", "url")

print "use RawConfigParser() write"
cf.set("portal", "url2", "%(host)s:%(port)s")
print cf.get("portal", "url2")
```
得到终端输出:
```
use RawConfigParser() read
http://%(host)s:%(port)s/Portal
use RawConfigParser() write
%(host)s:%(port)s
```

得到终端输出：
```
use RawConfigParser() read
http://%(host)s:%(port)s/Portal
use RawConfigParser() write
%(host)s:%(port)s
```

改用ConfigParser：
```
import ConfigParser

cf = ConfigParser.ConfigParser()

print "use ConfigParser() read"
cf.read("test2.conf")
print cf.get("portal", "url")

print "use ConfigParser() write"
cf.set("portal", "url2", "%(host)s:%(port)s")
print cf.get("portal", "url2")
```

得到终端输出：
```
use ConfigParser() read
http://localhost:8080/Portal
use ConfigParser() write
localhost:8080
```

改用SafeConfigParser：
```
import ConfigParser

cf = ConfigParser.SafeConfigParser()

print "use SafeConfigParser() read"
cf.read("test2.conf")
print cf.get("portal", "url")

print "use SateConfigParser() write"
cf.set("portal", "url2", "%(host)s:%(port)s")
print cf.get("portal", "url2")
```

得到终端输出(效果同ConfigParser)：
```
use SafeConfigParser() read
http://localhost:8080/Portal
use SateConfigParser() write
localhost:8080
```

### 41. 使用argparse处理命令行参数

python中的命令行解析最简单最原始的方法是使用sys.argv来实现，更高级的可以使用argparse这个模块。argparse从python 2.7开始被加入到标准库中，所以如果你的python版本还在2.7以下，那么需要先手动安装。

1) 基本使用
```
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("echo",help="echo the string")
args=parser.parse_args()
print args.echo
```

2) 参数介绍

上面这个例子是最简单的一个使用例子，功能是把你的输入参数打印到屏幕 。不过对于基本的使用需求，这几行代码应该就已经够用，更加高级的用法可以参考官方文档。

下面介绍例子代码:
```
1、导入argparse模块

2、创建解析器对象ArgumentParser，可以添加参数。

description：描述程序

parser=argparse.ArgumentParser(description="This is a example program ")

add_help：默认是True，可以设置False禁用

3、add_argument()方法，用来指定程序需要接受的命令参数

定位参数：

parser.add_argument("echo",help="echo the string")

可选参数：

parser.add_argument("--verbosity", help="increase output verbosity")

在执行程序的时候，定位参数必选，可选参数可选。

add_argument()常用的参数：

dest：如果提供dest，例如dest="a"，那么可以通过args.a访问该参数

default：设置参数的默认值

action：参数出发的动作

store：保存参数，默认

store_const：保存一个被定义为参数规格一部分的值（常量），而不是一个来自参数解析而来的值。

store_ture/store_false：保存相应的布尔值

append：将值保存在一个列表中。

append_const：将一个定义在参数规格中的值（常量）保存在一个列表中。

count：参数出现的次数

parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")

version：打印程序版本信息

type：把从命令行输入的结果转成设置的类型

choice：允许的参数值

parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")

help：参数命令的介绍
```

### 42. 使用pandas处理大型CSV文件

CSV(Comma Separated Values)作为一种逗号分隔型值的纯文本格式文件，在实际应用中经常使用到。如数据库的导入导出，数据分析中记录的存储等。因此很多语言都提供了对CSV文件处理的模块。

python处理csv的csv模块的api：
```
1) reader(csvfile[, dialect='excel'][, fmtparam]), 主要用于CSV文件的读取，返回一个reader对象用于在CSV文件内容上进行行的迭代。
参数csvfile： 需要是支持迭代的对象，通常对文件对象或者列表对象都是适用的，并且每次调用next()方法返回值都是字符串(string); 参数dialect的默认值为excel, 与excel兼容；fmtparam是一系列的参数列表，主要用于需要覆盖默认的DIalect设置的情形。

2) csv.writer(csvfile, dialect="excel", **fmtparams), 用于写入CSV文件，参数同上。

3）csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect="excel", *args, **kwds),同reader()方法类似，不同的是将读入的信息映射到一个字典中去，其中字典的key由fieldnames指定，该值省略的话将适用CSV文件第一行的数据作为key值。
如果读入行的字段的个数大于filednames中指定的个数，多余的字段名将会存放在restkey中，而热死tv阿里】
主要用于当读取行的域的个数小于fieldnames的时候，它的值将会被用作剩下的key对应的值。

4) csv.DictWriter(csvfile, fieldnames, restval=", extrasaction='raise', dialect='excel', *args, **kwds), 用于支持字典的写入。

注意: csv模块对处理大文件无能为力。
```

python的pandas模块: Python Data Analysis Library
是为了解决数据分析而创建的第三方工具，它不仅提供了丰富的数据模型，而且支持多种文件格式处理。
包括: csv, hdf5, html等。
能提供高效的大型数据处理。其支持两种数据结构:

1) Series

它是一种类似数据的待索引的一维数据结构，支持的类型与NumPy兼容。

2) DataFrame

类似电子表格，其数据为排好序的数据列的集合，每一列都可以是不同的数据类型， 它类似于一个二维的数据结构，支持行和列的索引。


### 43. 一般情况使用ElementTree解析XML

Element类型是一种灵活的容器对象，用于在内存中存储层次数据结构。可以说是list和dictionary的交叉。

ElementTree 生来就是为了处理 XML ，它在 Python 标准库中有两种实现。一种是纯 Python 实现例如 xml.etree.ElementTree ，另外一种是速度快一点的 xml.etree.cElementTree 。你要记住： 尽量使用 C 语言实现的那种，因为它速度更快，而且消耗的内存更少。如果你的电脑上没有 _elementtree (见注释4) 那么你需要这样做：
```
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
```
这是一个让 Python 不同的库使用相同 API 的一个比较常用的办法。还是那句话，你的编译环境和别人的很可能不一样，所以这样做可以防止一些莫名其妙的小问题。注意：从 Python 3.3 开始，你没有必要这么做了，因为 ElementTree 模块会自动寻找可用的 C 库来加快速度。所以只需要 import xml.etree.ElementTree 就可以了。但是在 3.3 正式推出之前，你最好还是使用我上面提供的那段代码。

1) 将 XML 解析为树的形式

XML 是一种分级的数据形式，所以最自然的表示方法是将它表示为一棵树。ET 有两个对象来实现这个目的 － ElementTree 将整个 XML 解析为一棵树， Element 将单个结点解析为树。如果是整个文档级别的操作(比如说读，写，找到一些有趣的元素)通常用 ElementTree 。单个 XML 元素和它的子元素通常用 Element 。下面的例子能说明我刚才啰嗦的一大堆。(见注释5)
```
<?xml version="1.0"?>
<doc>
    <branch name="testing" hash="1cdf045c">
        text,source
    </branch>
    <branch name="release01" hash="f200013e">
        <sub-branch name="subrelease01">
            xml,sgml
        </sub-branch>
    </branch>
    <branch name="invalid">
    </branch>
</doc>
```

让我们加载并且解析这个 XML ：
```
>>> import xml.etree.cElementTree as ET
>>> tree = ET.ElementTree(file='doc1.xml')
```

然后抓根结点元素：
```
>>> tree.getroot()
<Element 'doc' at 0x11eb780>
```

和预期一样，root 是一个 Element 元素。我们可以来看看：
```
>>> root = tree.getroot()
>>> root.tag, root.attrib
('doc', {})
```

看吧，根元素没有任何状态(见注释6)。就像任何 Element 一样，它可以找到自己的子结点：
```
>>> for child_of_root in root:
...   print child_of_root.tag, child_of_root.attrib
...
branch {'hash': '1cdf045c', 'name': 'testing'}
branch {'hash': 'f200013e', 'name': 'release01'}
branch {'name': 'invalid'}
```

我们也可以进入一个指定的子结点：
```
>>> root[0].tag, root[0].text
('branch', '\n        text,source\n    ')
```

2) 找到我们感兴趣的元素

从上面的例子我们可以轻而易举的看到，我们可以用一个简单的递归获取 XML 中的任何元素。然而，因为这个操作比较普遍，ET 提供了一些有用的工具来简化操作.

Element 对象有一个 iter 方法可以对子结点进行深度优先遍历。 ElementTree 对象也有 iter 方法来提供便利。
```
>>> for elem in tree.iter():
...   print elem.tag, elem.attrib
...
doc {}
branch {'hash': '1cdf045c', 'name': 'testing'}
branch {'hash': 'f200013e', 'name': 'release01'}
sub-branch {'name': 'subrelease01'}
branch {'name': 'invalid'}
```

遍历所有的元素，然后检验有没有你想要的。ET 可以让这个过程更便捷。 iter 方法接受一个标签名字，然后只遍历那些有指定标签的元素：
```
>>> for elem in tree.iter(tag='branch'):
...   print elem.tag, elem.attrib
...
branch {'hash': '1cdf045c', 'name': 'testing'}
branch {'hash': 'f200013e', 'name': 'release01'}
branch {'name': 'invalid'}
```

3) 来自 XPath 的帮助

为了寻找我们感兴趣的元素，一个更加有效的办法是使用 XPath 支持。 Element 有一些关于寻找的方法可以接受 XPath 作为参数。 find 返回第一个匹配的子元素， findall 以列表的形式返回所有匹配的子元素， iterfind 为所有匹配项提供迭代器。这些方法在 ElementTree 里面也有。

给出一个例子：
```
>>> for elem in tree.iterfind('branch/sub-branch'):
...   print elem.tag, elem.attrib
...
sub-branch {'name': 'subrelease01'}
```
这个例子在 branch 下面找到所有标签为 sub-branch 的元素。然后给出如何找到所有的 branch 元素，用一个指定 name 的状态即可：
```
>>> for elem in tree.iterfind('branch[@name="release01"]'):
...   print elem.tag, elem.attrib
...
branch {'hash': 'f200013e', 'name': 'release01'}
```
想要深入学习 XPath 的话，请看http://effbot.org/zone/element-xpath.htm 。

4) 建立 XML 文档

ET 提供了建立 XML 文档和写入文件的便捷方式。 ElementTree 对象提供了 write 方法。

现在，这儿有两个常用的写 XML 文档的脚本。

修改文档可以使用 Element 对象的方法：
```
>>> root = tree.getroot()
>>> del root[2]
>>> root[0].set('foo', 'bar')
>>> for subelem in root:
...   print subelem.tag, subelem.attrib
...
branch {'foo': 'bar', 'hash': '1cdf045c', 'name': 'testing'}
branch {'hash': 'f200013e', 'name': 'release01'}
```
我们在这里删除了根元素的第三个子结点，然后为第一个子结点增加新状态。然后这个树可以写回到文件中。
```
>>> import sys
>>> tree.write(sys.stdout)   # ET.dump can also serve this purpose
<doc>
    <branch foo="bar" hash="1cdf045c" name="testing">
        text,source
    </branch>
<branch hash="f200013e" name="release01">
    <sub-branch name="subrelease01">
        xml,sgml
    </sub-branch>
</branch>
</doc>
```
注意状态的顺序和原文档的顺序不太一样。这是因为 ET 讲状态保存在无序的字典中。语义上来说，XML 并不关心顺序。

建立一个全新的元素也很容易。ET 模块提供了 SubElement 函数来简化过程：
```
>>> a = ET.Element('elem')
>>> c = ET.SubElement(a, 'child1')
>>> c.text = "some text"
>>> d = ET.SubElement(a, 'child2')
>>> b = ET.Element('elem_b')
>>> root = ET.Element('root')
>>> root.extend((a, b))
>>> tree = ET.ElementTree(root)
>>> tree.write(sys.stdout)
<root><elem><child1>some text</child1><child2 /></elem><elem_b /></root>
```
使用 iterparse 来处理 XML 流
就像我在文章一开头提到的那样，XML 文档通常比较大，所以将它们全部读入内存的库可能会有点儿小问题。这也是为什么我建议使用 SAX API 来替代 DOM 。

我们刚讲过如何使用 ET 来将 XML 读入内存并且处理。但它就不会碰到和 DOM 一样的内存问题么？当然会。这也是为什么这个包提供一个特殊的工具，用来处理大型文档，并且解决了内存问题，这个工具叫 iterparse 。

我给大家演示一个 iterparse 如何使用的例子。我用 自动生成 拿到了一个 XML 文档来进行说明。这只是开头的一小部分：
```
<?xml version="1.0" standalone="yes"?>
<site>
    <regions>
        <africa>
            <item id="item0">
                <location>United States</location>    <!-- Counting locations -->
                <quantity>1</quantity>
                <name>duteous nine eighteen </name>
                <payment>Creditcard</payment>
                <description>
                    <parlist>
[...]
```
我已经用注释标出了我要处理的元素，我们用一个简单的脚本来计数有多少 location 元素并且文本内容为“Zimbabwe”。这是用 ET.parse 的一个标准的写法：
```
tree = ET.parse(sys.argv[2])

count = 0
for elem in tree.iter(tag='location'):
    if elem.text == 'Zimbabwe':
        count += 1
print count
```
所有 XML 树中的元素都会被检验。当处理一个大约 100MB 的 XML 文件时，占用的内存大约是 560MB ，耗时 2.9 秒。

注意：我们并不需要在内存中加载整颗树。它检测我们需要的带特定值的 location 元素。其他元素被丢弃。这是 iterparse 的来源：
```
count = 0
for event, elem in ET.iterparse(sys.argv[2]):
    if event == 'end':
        if elem.tag == 'location' and elem.text == 'Zimbabwe':
            count += 1
    elem.clear() # discard the element

print count
````
这个循环遍历 iterparse 事件，检测“闭合的”(end)事件并且寻找 location 标签和指定的值。在这里 elem.clear() 是关键 － iterparse 仍然建立一棵树，只不过不需要全部加载进内存，这样做可以有效的利用内存空间(见注释7)。

处理同样的文件，这个脚本占用内存只需要仅仅的 7MB ，耗时 2.5 秒。速度的提升归功于生成树的时候只遍历一次。相比较来说， parse 方法首先建立了整个树，然后再次遍历来寻找我们需要的元素(所以慢了一点)。

结论
在 Python 众多处理 XML 的模块中， ElementTree 真是屌爆了。它将轻量，符合 Python 哲学的 API ，出色的性能完美的结合在了一起。所以说如果要处理 XML ，果断地使用它吧！

这篇文章简略地谈了谈 ET 。我希望这篇拙作可以抛砖引玉。


### 44. 理解模块pickle优劣

Python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：
```
　　pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　　　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为3。
　　　　　file：对象保存到的类文件对象。file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。文件对象需要是二进制模式打开的。

　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。
```

使用help(pickle.dump)查看详细信息

例子：
```
#持久化类对象和列表对象  
import pickle  
  
class Person:    
    def __init__(self,n,a):    
        self.name=n    
        self.age=a    
    def show(self):    
        print( self.name+"_"+str(self.age) )  
          
aa = Person("JGood", 2)    
aa.show()     
f=open('H:\\p.txt','wb')  #必须以二进制打开，否则有错  
pickle.dump(aa,f,0)  
  
l1 = [ 1, 2, 3 ]  
pickle.dump( l1, f, 0 )  
f.close()    #必须先关闭，否则pickle.load(f1)会出现EOFError: Ran out of input  
  
f=open('H:\\p.txt','rb')    
bb=pickle.load(f)    
bb.show()  
  
l2 = pickle.load(f)  
print(l2)  
f.close() 
```

输出：
```
JGood_2
JGood_2
[1, 2, 3]
```

### 45. 序列化的另一个不错的选择-JSON

在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
```
d = dict(name='Bob', age=20, score=88)
```
可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
Python提供了pickle模块来实现序列化。

首先，我们尝试把一个对象序列化并写入文件：
```
>>> import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
```

pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like:
```
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
```

看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
```
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}
```
变量的内容又回来了！

当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

SON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

JSON类型  Python类型
{}          dict
[]          list
"string"    str
1234.56     int或float
true/false  True/False
null        None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
```
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
```
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
```
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{'age': 20, 'score': 88, 'name': 'Bob'}
```

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

JSON进阶

Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
```
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
```

运行代码，毫不留情地得到一个TypeError：
```
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
```

错误的原因是Student对象不是一个可序列化为JSON的对象。
如果连class的实例对象都无法序列化为JSON，这肯定不合理！
别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
```
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
```

这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
```
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
```
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
```
print(json.dumps(s, default=lambda obj: obj.__dict__))
```
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
```
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
```
运行结果如下：
```
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
```
打印出的是反序列化的Student实例对象。

小结

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。


### 46. 使用traceback获取栈信息

python中用于处理异常栈的模块是traceback模块，它提供了print_exception、format_exception等输出异常栈等常用的工具函数。
```
def func(a, b):
  return a / b
if __name__ == '__main__':
  import sys
  import traceback
  try:
    func(1, 0)
  except Exception as e:
    print "print exc"
    traceback.print_exc(file=sys.stdout)
```

输出结果：
```
print exc
Traceback (most recent call last):
  File "./teststacktrace.py", line 7, in <module>
    func(1, 0)
  File "./teststacktrace.py", line 2, in func
    return a / b
```

其实traceback.print_exc()函数只是traceback.print_exception()函数的一个简写形式，而它们获取异常相关的数据都是通过sys.exc_info()函数得到的。
```
def func(a, b):
  return a / b
if __name__ == '__main__':
  import sys
  import traceback
  try:
    func(1, 0)
  except Exception as e:
    print "print_exception()"
    exc_type, exc_value, exc_tb = sys.exc_info()
    print 'the exc type is:', exc_type
    print 'the exc value is:', exc_value
    print 'the exc tb is:', exc_tb
    traceback.print_exception(exc_type, exc_value, exc_tb)
```

输出结果：
```
print_exception()
the exc type is: <type 'exceptions.ZeroDivisionError'>
the exc value is: integer division or modulo by zero
the exc tb is: <traceback object at 0x104e7d4d0>
Traceback (most recent call last):
  File "./teststacktrace.py", line 7, in <module>
    func(1, 0)
  File "./teststacktrace.py", line 2, in func
    return a / b
ZeroDivisionError: integer division or modulo by zero
```
sys.exc_info()返回的值是一个元组，其中第一个元素，exc_type是异常的对象类型，
exc_value是异常的值，exc_tb是一个traceback对象，对象中包含出错的行数、位置等数据。然后通过print_exception函数对这些异常数据进行整理输出。

traceback模块提供了extract_tb函数来更加详细的解释traceback对象所包含的数据：
```
def func(a, b):
  return a / b
if __name__ == '__main__':
  import sys
  import traceback
  try:
    func(1, 0)
  except:
    _, _, exc_tb = sys.exc_info()
    for filename, linenum, funcname, source in traceback.extract_tb(exc_tb):
      print "%-23s:%s '%s' in %s()" % (filename, linenum, source, funcname)
```
输出结果：
```
samchimac:tracebacktest samchi$ python ./teststacktrace.py 
./teststacktrace.py    :7 'func(1, 0)' in <module>()
./teststacktrace.py    :2 'return a / b' in func()
```

### 47. 使用logging记录日志信息

简单将日志打印到屏幕：
```
import logging  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  
```

输出:
```
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
```

可见，默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），默认的日志格式为日志级别：Logger名称：用户输出消息。

灵活配置日志级别，日志格式，输出位置
```
import logging  
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='/tmp/test.log',  
                    filemode='w')  
  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  
```

查看输出：
```
cat /tmp/test.log 
Mon, 05 May 2014 16:29:53 test_logging.py[line:9] DEBUG debug message
Mon, 05 May 2014 16:29:53 test_logging.py[line:10] INFO info message
Mon, 05 May 2014 16:29:53 test_logging.py[line:11] WARNING warning message
Mon, 05 May 2014 16:29:53 test_logging.py[line:12] ERROR error message
Mon, 05 May 2014 16:29:53 test_logging.py[line:13] CRITICAL critical message
```

可见在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
```
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。 
datefmt：指定日期时间格式。 
level：设置rootlogger（后边会讲解具体概念）的日志级别 
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
```

format参数中可能用到的格式化串：
```
%(name)s                Logger的名字
%(levelno)s             数字形式的日志级别
%(levelname)s           文本形式的日志级别
%(pathname)s            调用日志输出函数的模块的完整路径名，可能没有
%(filename)s            调用日志输出函数的模块的文件名
%(module)s              调用日志输出函数的模块名
%(funcName)s            调用日志输出函数的函数名
%(lineno)d              调用日志输出函数的语句所在的代码行
%(created)f             当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d     输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s             字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45, 896”。逗号后面的是毫秒
%(thread)d              线程ID。可能没有
%(threadName)s          线程名。可能没有
%(process)d             进程ID。可能没有
%(message)s             用户输出的消息
```

若要对logging进行更多灵活的控制有必要了解一下Logger，Handler，Formatter，Filter的概念

上述几个例子中我们了解到了
logging.debug()、
logging.info()、
logging.warning()、
logging.error()、
logging.critical()（分别用以记录不同级别的日志信息），
logging.basicConfig()（用默认日志格式（Formatter）
为日志系统建立一个默认的流处理器（StreamHandler），
设置基础配置（如日志级别等）并加到rootlogger（根Logger）中）这几个logging模块级别的函数，
另外还有一个模块级别的函数是logging.getLogger([name])（返回一个logger对象，如果没有指定名字将返回root logger）

先看一个具体的例子
```
#coding:utf-8  
import logging  
  
# 创建一个logger    
logger = logging.getLogger()  
  
logger1 = logging.getLogger('mylogger')  
logger1.setLevel(logging.DEBUG)  
  
logger2 = logging.getLogger('mylogger')  
logger2.setLevel(logging.INFO)  
  
logger3 = logging.getLogger('mylogger.child1')  
logger3.setLevel(logging.WARNING)  
  
logger4 = logging.getLogger('mylogger.child1.child2')  
logger4.setLevel(logging.DEBUG)  
  
logger5 = logging.getLogger('mylogger.child1.child2.child3')  
logger5.setLevel(logging.DEBUG)  
  
# 创建一个handler，用于写入日志文件    
fh = logging.FileHandler('/tmp/test.log')  
  
# 再创建一个handler，用于输出到控制台    
ch = logging.StreamHandler()  
  
# 定义handler的输出格式formatter    
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
#定义一个filter  
#filter = logging.Filter('mylogger.child1.child2')  
#fh.addFilter(filter)    
  
# 给logger添加handler    
#logger.addFilter(filter)  
logger.addHandler(fh)  
logger.addHandler(ch)  
  
#logger1.addFilter(filter)  
logger1.addHandler(fh)  
logger1.addHandler(ch)  
  
logger2.addHandler(fh)  
logger2.addHandler(ch)  
  
#logger3.addFilter(filter)  
logger3.addHandler(fh)  
logger3.addHandler(ch)  
  
#logger4.addFilter(filter)  
logger4.addHandler(fh)  
logger4.addHandler(ch)  
  
logger5.addHandler(fh)  
logger5.addHandler(ch)  
  
# 记录一条日志    
logger.debug('logger debug message')  
logger.info('logger info message')  
logger.warning('logger warning message')  
logger.error('logger error message')  
logger.critical('logger critical message')  
  
logger1.debug('logger1 debug message')  
logger1.info('logger1 info message')  
logger1.warning('logger1 warning message')  
logger1.error('logger1 error message')  
logger1.critical('logger1 critical message')  
  
logger2.debug('logger2 debug message')  
logger2.info('logger2 info message')  
logger2.warning('logger2 warning message')  
logger2.error('logger2 error message')  
logger2.critical('logger2 critical message')  
  
logger3.debug('logger3 debug message')  
logger3.info('logger3 info message')  
logger3.warning('logger3 warning message')  
logger3.error('logger3 error message')  
logger3.critical('logger3 critical message')  
  
logger4.debug('logger4 debug message')  
logger4.info('logger4 info message')  
logger4.warning('logger4 warning message')  
logger4.error('logger4 error message')  
logger4.critical('logger4 critical message')  
  
logger5.debug('logger5 debug message')  
logger5.info('logger5 info message')  
logger5.warning('logger5 warning message')  
logger5.error('logger5 error message')  
logger5.critical('logger5 critical message')  
```

输出：
```
2014-05-06 12:54:43,222 - root - WARNING - logger warning message
2014-05-06 12:54:43,223 - root - ERROR - logger error message
2014-05-06 12:54:43,224 - root - CRITICAL - logger critical message
2014-05-06 12:54:43,224 - mylogger - INFO - logger1 info message
2014-05-06 12:54:43,224 - mylogger - INFO - logger1 info message
2014-05-06 12:54:43,225 - mylogger - WARNING - logger1 warning message
2014-05-06 12:54:43,225 - mylogger - WARNING - logger1 warning message
2014-05-06 12:54:43,226 - mylogger - ERROR - logger1 error message
2014-05-06 12:54:43,226 - mylogger - ERROR - logger1 error message
2014-05-06 12:54:43,227 - mylogger - CRITICAL - logger1 critical message
2014-05-06 12:54:43,227 - mylogger - CRITICAL - logger1 critical message
2014-05-06 12:54:43,228 - mylogger - INFO - logger2 info message
2014-05-06 12:54:43,228 - mylogger - INFO - logger2 info message
2014-05-06 12:54:43,229 - mylogger - WARNING - logger2 warning message
2014-05-06 12:54:43,229 - mylogger - WARNING - logger2 warning message
2014-05-06 12:54:43,230 - mylogger - ERROR - logger2 error message
2014-05-06 12:54:43,230 - mylogger - ERROR - logger2 error message
2014-05-06 12:54:43,231 - mylogger - CRITICAL - logger2 critical message
2014-05-06 12:54:43,231 - mylogger - CRITICAL - logger2 critical message
2014-05-06 12:54:43,232 - mylogger.child1 - WARNING - logger3 warning message
2014-05-06 12:54:43,232 - mylogger.child1 - WARNING - logger3 warning message
2014-05-06 12:54:43,232 - mylogger.child1 - WARNING - logger3 warning message
2014-05-06 12:54:43,234 - mylogger.child1 - ERROR - logger3 error message
2014-05-06 12:54:43,234 - mylogger.child1 - ERROR - logger3 error message
2014-05-06 12:54:43,234 - mylogger.child1 - ERROR - logger3 error message
2014-05-06 12:54:43,235 - mylogger.child1 - CRITICAL - logger3 critical message
2014-05-06 12:54:43,235 - mylogger.child1 - CRITICAL - logger3 critical message
2014-05-06 12:54:43,235 - mylogger.child1 - CRITICAL - logger3 critical message
2014-05-06 12:54:43,237 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 12:54:43,237 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 12:54:43,237 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 12:54:43,237 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 12:54:43,239 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 12:54:43,239 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 12:54:43,239 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 12:54:43,239 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 12:54:43,240 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 12:54:43,240 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 12:54:43,240 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 12:54:43,240 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 12:54:43,242 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 12:54:43,242 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 12:54:43,242 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 12:54:43,242 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 12:54:43,243 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 12:54:43,243 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 12:54:43,243 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 12:54:43,243 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 12:54:43,244 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 12:54:43,244 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 12:54:43,244 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 12:54:43,244 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 12:54:43,244 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 12:54:43,246 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 12:54:43,246 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 12:54:43,246 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 12:54:43,246 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 12:54:43,246 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 12:54:43,247 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 12:54:43,247 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 12:54:43,247 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 12:54:43,247 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 12:54:43,247 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 12:54:43,249 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 12:54:43,249 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 12:54:43,249 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 12:54:43,249 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 12:54:43,249 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 12:54:43,250 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 12:54:43,250 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 12:54:43,250 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 12:54:43,250 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 12:54:43,250 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
```

先简单介绍一下，logging库提供了多个组件：Logger、Handler、Filter、Formatter。Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。

1） Logger

Logger是一个树形层级结构，输出信息之前都要获得一个Logger（如果没有显示的获取则自动创建并使用root Logger，如第一个例子所示）。
logger = logging.getLogger()返回一个默认的Logger也即root Logger，并应用默认的日志级别、Handler和Formatter设置。
当然也可以通过Logger.setLevel(lel)指定最低的日志级别，可用的日志级别有logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL。
Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()输出不同级别的日志，只有日志等级大于或等于设置的日志级别的日志才会被输出。

我们看到程序中：
```
logger.debug('logger debug message')  
logger.info('logger info message')  
logger.warning('logger warning message')  
logger.error('logger error message')  
logger.critical('logger critical message')  
```

输出：
```
2014-05-06 12:54:43,222 - root - WARNING - logger warning message
2014-05-06 12:54:43,223 - root - ERROR - logger error message
2014-05-06 12:54:43,224 - root - CRITICAL - logger critical message
```
从这个输出可以看出logger = logging.getLogger()返回的Logger名为root。这里没有用logger.setLevel()显示的为logger设置日志级别，所以使用默认的日志级别WARNIING，故结果只输出了大于等于WARNIING级别的信息。

另外，我们明明通过logger1.setLevel(logging.DEBUG)将logger1的日志级别设置为了DEBUG，为何显示的时候没有显示出DEBUG级别的日志信息，而是从INFO级别的日志开始显示呢？原来logger1和logger2对应的是同一个Logger实例，只要logging.getLogger（name）中名称参数name相同则返回的Logger实例就是同一个，且仅有一个，也即name与Logger实例一一对应。在logger2实例中通过logger2.setLevel(logging.INFO)设置mylogger的日志级别为logging.INFO，所以最后logger1的输出遵从了后来设置的日志级别。
```
logger1 = logging.getLogger('mylogger')  
logger1.setLevel(logging.DEBUG)  
logger2 = logging.getLogger('mylogger')  
logger2.setLevel(logging.INFO) 
```

为什么logger1、logger2对应的每个输出分别显示两次，logger3对应的输出显示3次，logger4对应的输出显示4次......呢？

这是因为我们通过logger = logging.getLogger()显示的创建了root Logger，而logger1 = logging.getLogger('mylogger')创建了root Logger的孩子(root.)mylogger,logger2同样。
logger3 = logging.getLogger('mylogger.child1')创建了(root.)mylogger.child1
logger4 = logging.getLogger('mylogger.child1.child2')创建了(root.)mylogger.child1.child2
logger5 = logging.getLogger('mylogger.child1.child2.child3')创建了(root.)mylogger.child1.child2.child3
而孩子,孙子，重孙……既会将消息分发给他的handler进行处理也会传递给所有的祖先Logger处理。

试着注释掉如下一行程序，观察程序输出：
```
#logger.addHandler(fh)    
```
发现标准输出中每条记录对应两行（因为root Logger默认使用StreamHandler）：
```
2014-05-06 15:10:10,980 - mylogger - INFO - logger1 info message
2014-05-06 15:10:10,980 - mylogger - INFO - logger1 info message
2014-05-06 15:10:10,981 - mylogger - WARNING - logger1 warning message
2014-05-06 15:10:10,981 - mylogger - WARNING - logger1 warning message
2014-05-06 15:10:10,982 - mylogger - ERROR - logger1 error message
2014-05-06 15:10:10,982 - mylogger - ERROR - logger1 error message
2014-05-06 15:10:10,984 - mylogger - CRITICAL - logger1 critical message
2014-05-06 15:10:10,984 - mylogger - CRITICAL - logger1 critical message
```

而在文件输出中每条记录对应一行（因为我们注释掉了logger.addHandler(fh)，没有对root Logger启用FileHandler）
```
2014-05-06 15:10:10,980 - mylogger - INFO - logger1 info message
2014-05-06 15:10:10,981 - mylogger - WARNING - logger1 warning message
2014-05-06 15:10:10,982 - mylogger - ERROR - logger1 error message
2014-05-06 15:10:10,984 - mylogger - CRITICAL - logger1 critical message
```
孩子,孙子，重孙……可逐层继承来自祖先的日志级别、Handler、Filter设置，也可以通过Logger.setLevel(lel)、Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)、Logger.addFilter(filt)、Logger.removeFilter(filt)。设置自己特别的日志级别、Handler、Filter。若不设置则使用继承来的值。

2） Handler

上述例子的输出在标准输出和指定的日志文件中均可以看到，这是因为我们定义并使用了两种Handler。
```
fh = logging.FileHandler('/tmp/test.log')   
ch = logging.StreamHandler()  
```
Handler对象负责发送相关的信息到指定目的地，有几个常用的Handler方法：
Handler.setLevel(lel):指定日志级别，低于lel级别的日志将被忽略
Handler.setFormatter()：给这个handler选择一个Formatter
Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象

可以通过addHandler()方法为Logger添加多个Handler：
```
logger.addHandler(fh)  
logger.addHandler(ch)  
```
有多中可用的Handler：
logging.StreamHandler   可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
logging.FileHandler     用于向一个文件输出日志信息
logging.handlers.RotatingFileHandler 类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出
logging.handlers.TimedRotatingFileHandler 和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就自动创建新的日志文件
logging.handlers.SocketHandler 使用TCP协议，将日志信息发送到网络。
logging.handlers.DatagramHandler 使用UDP协议，将日志信息发送到网络。
logging.handlers.SysLogHandler 日志输出到syslog
logging.handlers.NTEventLogHandler 远程输出日志到Windows NT/2000/XP的事件日志 
logging.handlers.SMTPHandler 远程输出日志到邮件地址
logging.handlers.MemoryHandler 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler 通过"GET"或"POST"远程输出到HTTP服务器
各个Handler的具体用法可查看参考书册：
https://docs.python.org/2/library/logging.handlers.html#module-logging.handlers


3） Formatter

Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S。
```
#定义Formatter  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
#为Handler添加Formatter  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
```
Formatter参数中可能用到的格式化串参见上文（logging.basicConfig()函数format参数中可能用到的格式化串：）


4）Filter

限制只有满足过滤规则的日志才会输出。
比如我们定义了filter = logging.Filter('a.b.c'),并将这个Filter添加到了一个Handler上，则使用该Handler的Logger中只有名字带a.b.c前缀的Logger才能输出其日志。

取消下列两行程序的注释：
```
#filter = logging.Filter('mylogger.child1.child2')  
#fh.addFilter(filter)    
```

标准输出中输出结果并没有发生变化，但日志文件输出中只显示了如下内容：
```
2014-05-06 15:27:36,227 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:27:36,227 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:27:36,227 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:27:36,227 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:27:36,228 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:27:36,228 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:27:36,228 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:27:36,228 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:27:36,230 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:27:36,230 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:27:36,230 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:27:36,230 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:27:36,232 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:27:36,232 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:27:36,232 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:27:36,232 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:27:36,233 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:27:36,233 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:27:36,233 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:27:36,233 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:27:36,235 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:27:36,235 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:27:36,235 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:27:36,235 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:27:36,235 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:27:36,236 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:27:36,236 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:27:36,236 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:27:36,236 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:27:36,236 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:27:36,238 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:27:36,238 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:27:36,238 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:27:36,238 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:27:36,238 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:27:36,240 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:27:36,240 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:27:36,240 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:27:36,240 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:27:36,240 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:27:36,242 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:27:36,242 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:27:36,242 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:27:36,242 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:27:36,242 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
```
当然也可以直接给Logger加Filter。若为Handler加Filter则所有使用了该Handler的Logger都会受到影响。而为Logger添加Filter只会影响到自身。
注释掉：
```
#fh.addFilter(filter)
```

并取消如下几行的注释：
```
#logger.addFilter(filter)  
#logger1.addFilter(filter)  
#logger3.addFilter(filter)  
#logger4.addFilter(filter)  
```

输出结果
```
2014-05-06 15:32:10,746 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:32:10,746 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:32:10,746 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:32:10,746 - mylogger.child1.child2 - DEBUG - logger4 debug message
2014-05-06 15:32:10,748 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:32:10,748 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:32:10,748 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:32:10,748 - mylogger.child1.child2 - INFO - logger4 info message
2014-05-06 15:32:10,751 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:32:10,751 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:32:10,751 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:32:10,751 - mylogger.child1.child2 - WARNING - logger4 warning message
2014-05-06 15:32:10,753 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:32:10,753 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:32:10,753 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:32:10,753 - mylogger.child1.child2 - ERROR - logger4 error message
2014-05-06 15:32:10,754 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:32:10,754 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:32:10,754 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:32:10,754 - mylogger.child1.child2 - CRITICAL - logger4 critical message
2014-05-06 15:32:10,755 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:32:10,755 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:32:10,755 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:32:10,755 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:32:10,755 - mylogger.child1.child2.child3 - DEBUG - logger5 debug message
2014-05-06 15:32:10,757 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:32:10,757 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:32:10,757 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:32:10,757 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:32:10,757 - mylogger.child1.child2.child3 - INFO - logger5 info message
2014-05-06 15:32:10,759 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:32:10,759 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:32:10,759 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:32:10,759 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:32:10,759 - mylogger.child1.child2.child3 - WARNING - logger5 warning message
2014-05-06 15:32:10,761 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:32:10,761 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:32:10,761 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:32:10,761 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:32:10,761 - mylogger.child1.child2.child3 - ERROR - logger5 error message
2014-05-06 15:32:10,762 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:32:10,762 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:32:10,762 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:32:10,762 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
2014-05-06 15:32:10,762 - mylogger.child1.child2.child3 - CRITICAL - logger5 critical message
```
发现root、mylogger、mylogger.child1的输出全部被过滤掉了。


5） 除了直接在程序中设置Logger，Handler,Filter,Formatter外还可以将这些信息写进配置文件中。

例如典型的logging.conf
```
[loggers]  
keys=root,simpleExample  
  
[handlers]  
keys=consoleHandler  
  
[formatters]  
keys=simpleFormatter  
  
[logger_root]  
level=DEBUG  
handlers=consoleHandler  
  
[logger_simpleExample]  
level=DEBUG  
handlers=consoleHandler  
qualname=simpleExample  
propagate=0  
  
[handler_consoleHandler]  
class=StreamHandler  
level=DEBUG  
formatter=simpleFormatter  
args=(sys.stdout,)  
  
[formatter_simpleFormatter]  
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s  
datefmt=  
```
程序可以这么写：
```
import logging    
import logging.config    
    
logging.config.fileConfig("logging.conf")    # 采用配置文件     
    
# create logger     
logger = logging.getLogger("simpleExample")    
    
# "application" code     
logger.debug("debug message")    
logger.info("info message")    
logger.warn("warn message")    
logger.error("error message")    
logger.critical("critical message")  
```

6）多模块使用logging

logging模块保证在同一个python解释器内，多次调用logging.getLogger('log_name')都会返回同一个logger实例，即使是在多个模块的情况下。所以典型的多模块场景下使用logging的方式是在main模块中配置logging，这个配置会作用于多个的子模块，然后在其他模块中直接通过getLogger获取Logger对象即可。

main.py：
```
import logging    
import logging.config    
    
logging.config.fileConfig('logging.conf')    
root_logger = logging.getLogger('root')    
root_logger.debug('test root logger...')    
    
logger = logging.getLogger('main')    
logger.info('test main logger')    
logger.info('start import module \'mod\'...')    
import mod    
    
logger.debug('let\'s test mod.testLogger()')    
mod.testLogger()    
    
root_logger.info('finish test...')  
```

子模块mod.py：
```
import logging    
import submod    
    
logger = logging.getLogger('main.mod')    
logger.info('logger of mod say something...')    
    
def testLogger():    
    logger.debug('this is mod.testLogger...')    
    submod.tst()   
```

子子模块submod.py：
```
import logging    
    
logger = logging.getLogger('main.mod.submod')    
logger.info('logger of submod say something...')    
    
def tst():    
    logger.info('this is submod.tst()...')    
```


### 48. 使用threading模块编写多线程程序

1） threading模块简介

在Python多线程中可以使用2个模块，一个是我们现在讲解的threading，还有一个是thread模块，但是后者比较底层，后者算是它的一个升级版，现在来说Python对于线程的操作还不如其它编程语言有优势，不能够利用好多核心CPU的资源，但是不妨碍我们使用。

2） threading模块方法讲

2.1、 模块的Thread函数的可以实例化一个对象，每个Thread对象对应一个线程，可以通过start()方法，运行线程。
2.2、 threading.activeCount()方法返回当前”进程”里面”线程”的个数，注：返回的个数中包含主线程。类似python统计列表中[元素个数](http://www.iplaypython.com/jinjie/jj170.html)。
2.3、 threading.enumerate()的方法，返回当前运行中的Thread对象列表。
2.4、 threading.setDaemon()方法，参数设置为True的话会将线程声明为守护线程，必须在start() 方法之前设置，不设置为守护线程程序会被无限挂起。


3) threading模块源码演示

使用threading模块多线程操作有两种模式，我们先来看第一种创建线程要执行的函数，把这个函数传递进Thread对象里，让它来执行，代码如下：
```
import threading
import time

def thread_main(a):
   global count, mutex
   threadname = threading.currentThread().getName() # 获取线程名

   for x in xrange(0, int(a)):
       mutex.acquire() # 加锁
       count = count + 1
       mutex.release() # 释放锁
       print threadname, x, count
       time.sleep(1)

def main(num):
    global count, mutex
    threads = [] 
    count = 1
    mutex = threading.Lock() # 创建一个锁

    for x in xrange(0, num):
        threads.append(threading.Thread(target=thread_main, args=(10,)))

    for t in threads: # 启动所有线程
        t.start()

    for t in threads:
        t.join()  # 主线程中等待所有子线程退出

if __name__ == "__mian__":
    num = 4 # 创建4个线程
    main(4)
```

第二种是通过继承threading.Thread的方法，新建一个类(class)，把执行线程的代码放到这个类里面。
```
import threading
import time

class Test(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self._run_num = num

    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()

        for x in xrange(0, int(self._run_num)):
            mutex.acquire()
            count = count + 1
            mutex.release()
            print threadname, x, count
            time.sleep(1)

if __name__ == "__main__":
    global count, mutex
    threads = []
    num = 4
    count = 1

    mutex = threading.LOCK() # 创建锁

    for x in xrange(0, num):
        threads.append(Test(10)) # 添加线程对象

    for t in threads：
        t.start() # 启动线程

    for t in threads:
        t.join() # 等待子进程结束
```


### 49. 使用Queue使多线程编程更安全

Queue模块提供了一个适用于多线程编程的先进先出数据结构，可以用来安全的传递多线程信息。

创建一个Queue模块的队列对象：
```
>>> import Queue 
>>> q = Queue.Queue(maxsize=10)
>>>
```
上面的代码中，先导入了Queue模块，之后创建了一个叫做变量Q的队列对象，Queue.Queue是一个类，相当于创建了一个队列，这个队列有一个可参数masize，可以设置队列有长度，设置为“-1”，就可以让队列达到无限。

将一个数值放入队列中去：
```
>>> q.put(10)
>>>
```
put()方法可以在队列的尾部插入一个项目，它有2个参数，一个是需要插入的项，第二个默认参数值为1，方法让线程暂停，直到空出一个数据单元项，如果参数为0，会出发Full Python的异常。

有进有出，将刚才插入的值，再用get()方法取出来：
```
>>> q.get()
>>>
```

q这个对象的get()方法可以从队列头部删除而且返回一个项目，有一个可选参数，默认值是真，也就是True。get()就使调用线程暂停，直至有项目可用,如果队列为空且block为False，队列将引发Empty的Python异常。
举一个Queue的先进先出(FIFO)队列源码案例：

```
>>> import Queue
>>> q = Queue.Queue() #创建队列对象
>>>
>>> for i in range(8):
>>>    q.put(i)
>>>
>>> while not q.empty():
>>>    print q.get()
>>> print # 代码只使用了一个线程
>>>
````
结果：0 1 2 3 4 5 6 7