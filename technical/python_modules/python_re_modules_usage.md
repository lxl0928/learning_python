## python的re模块

[TOC]

### 什么是正则表达式
正则表达式(可以称为REs，regex，regex pattens)是一个小巧的，高度专业化的编程语言，
它内嵌于python开发语言中，可通过re模块使用。正则表达式的pattern可以被编译成一系列
的字节码，然后用C编写的引擎执行。

### 正则表达式包含的元字符的列表

(1) 正则表达式语法

![语法表1](http://7xorah.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE20161012155613.png)

![语法表2](http://7xorah.com1.z0.glb.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE20161012155739.png)

### re的主要功能元素

常用的功能函数包括: compile, search, match, split, findall(finditer), sub(subn)

(1) re.compile(pattern[, flags])

作用: 把正则表达式转化成正则表达式对象

flags定义包括:
```
  re.l: 忽略大小写
  re.L: 表示特殊字符集\w, \W, \b, \B, \s, \S依赖于当前环境
  re.M: 多行模式
  re.S: '.'并且包括换行符在内的任意字符(注意: '.'不包括换行符)
  re.U: 表示特殊字符集\w, \W, \b, \B, \d, \D, \s, \S依赖于Unicode字符属性数据库
  更多用法： http://www.devexception.com/sitemap_index.xml
```

(2) re.search(pattern, string[, flags])

作用: 在字符串中查找匹配正则表达式模式的位置，　返回MatchObject的实例，　如果没有找到匹配的位置，　则返回None.

(3) re.match(pattern, string[, flags])

作用: match() 函数只在字符串的开始位置尝试匹配正则表达式，也就是只报告从位置 0 开始的匹配情况，而 search() 函数是扫描整个字符串来查找匹配。如果想要搜索整个字符串来寻找匹配，应当用 search()。

例子: 最基本的用法-通过re.RegexObject对象调用
```
#！ /usr/bin/env python
import re

r1 = re.compile(r'world')

if r1.match('helloworld'):
    print("match succeeds")
else:
    print("match fails")

if r1.search("hello world"):
    print("search succeeds")
else:
    print("search fails")
```

例子: 设置flag
```
# r2 = re.compile(r'n$', re.S)
# r2 = re.compile(r'\n$', re.S)
r2 = re.compile('World$', re.l)
if r2.search('helloworld\n'):
    print("search succeeds")
else:
    print("search fails")

```

例子: 直接调用

```
if re.search(r'abc', 'helloaaabcdworldn'):
    print("search succeeds")
else:
    print("search fails")
```

(4) re.split(pattern, string[, maxsplit=0, flags=0])

作用: 可以将字符串匹配正则表达式的部分分割开并返回一个列表

例子: 简单分析ip
```
#! /usr/bin/env python
import re
r1 = re.compile('W+')

print(r1.split('192.168.1.1')

print(re.split('(W+)', '192.168.1.1'))

print(re.split('(W+)', '192.168.1.1', 1))

"""结果:
['192', '168', '1', '1']
['192', '.', '168', '.', '1', '.', '1']
['192', '.', '168.1.1']
"""
```

(5) re.findall(pattern, string[, flags])

作用: 在字符串中找到正则表达式所匹配的所有子串， 并组成一个列表返回

例子: 查找[]包括的内容(贪婪和非贪婪查找)
```
#! /usr/bin/env python
import re

r1 = re.compile('([.*])')
 
print(re.findall(r1, "hello[hi]heldfsdsf[iwonder]io"))

r2 = re.compile('(r2, "hello[hi]heldfsdsf[iwonder]io"))

print(re.findall('[0-9]{2}', "fdskfj1323jfkdj"))
print(re.findall('([0-9][a-z])', "fdskfj1323jfkdj"))
print re.findall('(?=www)',"afdsfwwwfkdjfsdfsdwww")
print re.findall('(?<=www)',"afdsfwwwfkdjfsdfsdwww")
```

说明: finditer和findall类似， 在字符串中找到正则表达式所匹配的所有子串， 并组成一个迭代器返回


(6) re.sub(pattern, repl, string[, count, flags])

说明：在字符串 string 中找到匹配正则表达式 pattern 的所有子串，用另一个字符串 repl 进行替换。如果没有找到匹配 pattern 的串，则返回未被修改的 string。Repl 既可以是字符串也可以是一个函数。

例子: 
```
#! /usr/bin/env python
import re

p = re.compile('('one|two|three)')
print(p.sub('num', 'one word two words three words apple', 2)
```

说明: re.subn(pattern, repl, string[, count, flags])
该函数功能和sub()相同, 但它还返回新的字符串以及替换的次数。



