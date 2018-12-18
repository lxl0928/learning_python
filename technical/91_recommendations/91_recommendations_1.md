## 编写高质量代码(改善Python程序的91个建议)_1

[TOC]

### 1.理解pythonic概念
(1) 定义: 充分体现Python自身特色的代码风格
例子: 快速排序
```
def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less)+[pivot]+quicksort(greater)
```

(2) 代码风格
灵活使用迭代器是一种Python风格.
例子: 遍历一个容器
```
for instance in alist:
    do_sth_with(instance)
```

例子: 安全关闭文件的描述符
```
with open(path, 'r') as f:
    do_sth_with(f)
```

例子: 逆置list及string
```
a = [1, 2, 3, 4]
c = 'abcdef'

print(a[::-1])
print(c[::-1])

# 等同于python库的reversed()函数
print(reversed(a))
print(reversed(c))

"""
结果: 
[4, 3, 2, 1]
fedcba
[4, 3, 2, 1]
['f', 'e', 'd', 'c', 'b', 'a']

"""
```

(3)标准库
充分理解内值函数和内置数据类型
例子: 字符串格式化
```
# 一般情况
print("Hello %s!" % ('Tom'))

# 更改情况
print("Hello %{name}s!", % {'name': 'Tom'})

# 更好的情况
print("{greet} from {language}".format(greet="Hello world", language="Python"))
```

str.format是Python最为推荐的字符串格式化方法

(4)Pythonnic的库或者方法
例子: Flask框架是公认为比较Pythonic的
```
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run()
```

例子: Python的包和模块结构日益规范化
```
1. 包和模块的命名采用小写, 单数形式, 而且短小
2. 包通常仅作为命名空间, 如只包含空的__init__.py文件
```


### 2. 编写Pythonic代码
(1) 要避免劣化代码
  1) 避免只用大小写区分不同的对象
  2) 避免使用容易引起混淆的名称
  3) 不要害怕过长的变量名

(2) 深入认识Python有助于编写Pythonic代码
例子: 
```
pip install -U pep8
```
通过PEP检测代码是否Pythonic


### 3. 理解Python与C的不同之处
(1) "缩进" 与 "{}"
python代码通过四个空格缩进,代表{}

(2) ' 与 "
```
>>> string1 = "He said, \"Hello\""    # 使用双引号时, 内部的双引号需要转义
>>> string1
'He said, "Hello"'

>>> string2 = 'He said, "Hello"'      # 使用单引号时, 内部双引号不需要转义
>>> string2
'He said, "Hello"'
```

(3) 三元操作符" ?: "
python中通过: X if C else Y
```
>>> x = 0
>>> y = 2
>>> x if x<=y else y
0
```

(4)switch...case
python中没有switch...case, 通过:
方法1:
```
n = 3
if n == 0:
    print("n==0")
elif n == 1:
    print("n==1")
elif n == 2:
    print("n==2")
elif n == 3:
    print("n==3")
else
    print("n==?")
```

方法2:
```
def f(x):
    return {
        0: "n==0",
        1: "n==1",
        2: "n==2",
        3: "n==3"
    }.get(n, "Only single-digit numbers are allowed\n")
```

### 4. 在代码中适当添加注释

(1)使用块或者行注释仅仅注释那些复杂的操作, 算法, 还有可能别人难以理解的的技巧或者不够
一目了然的代码.

(2) 注释和代码隔开一段距离

(3)给外部可访问的函数和方法(无论是否简单)添加文档注释, 注释要清楚描述方法的功能, 并对参数, 返回值以及可能发生的异常进行说明, 使得外部的调用它的人员仅仅看docstring就能正确使用.
较为复杂的内部方法也需要进行注释, 推荐的注释如下:
```
def FuncName(parameter1, parameter2):
    """Describe what the function does.
       # such as "Find whether the special string is in the queue or not"
       Args:
           parameter1: parameter type, what is this parameter used for.
                       # such as strqueue: string, string queue list for search.
           parameter2: patameter type, what is this parameter used for.
                       # such as str: string, string to find
       Returns:
           return type, return value.
           # such as boolen, sepcial string found return True, else return False
    """

    function body
    ...
    ...

```

(4) 推荐在文件头中包含copyright申明, 模块描述等等, 如有必要, 可以加入作者信息和变更记录
```
"""
    Licensed Materials - Property of CorpA
    (C) Copyright A Corp. 1999 2011 All Rights Reserved
    CopyRight statement and purpose...
    --------------------------------------------------------------
    File Name : comments.py
    Description : description what the main funciton of this file

    Author : Timilong
    Change Activity:
        list the change activity and time adn author information.
    --------------------------------------------------------------
"""
```

(5) 错误的例子
  1) 代码即注释(不写注释)
  2) 注释与代码重复
  3) 利用注释快速删除代码


### 5. 通过适当添加空行使代码布局更为优雅, 合理

(1) 在一组代码表达完成一个完整的思路后, 应该用空白航进行间隔
(2) 尽量保持上下文语义的易理解性
(3) 尽量避免过长的代码行, 每行最好不要超过80个字符
(4) 不要为了保持水平对齐儿使用多余的空格, 其实使阅读者尽可能容易的理解代码索要表达的意义更加重要.
(5) 空格的使用要能够在需要的时候警示读者.
  1) 二元运算符, 布尔运算左右两边加上空格
  2) 逗号和分号前不要使用空格
  3) 函数名和左括号, 序列索引操作时序列名和[]之间不需要空格, 函数默认参数两侧不需要空格
  4) 强调前面的操作要使用空格


### 6. 编写函数的4个原则

函数能够带来最大化的代码重用和最小化的代码冗余.
精心设计的函数不仅可以提高程序的健壮性, 还可以增强可读性, 减少维护成本.
(1) 函数设计要尽量短小, 嵌套层次不宜过深
(2) 函数申明应该做到合理, 简单, 易于使用
(3) 函数参数设计英国去爱考虑到向下兼容
(4) 一个函数只做一件事, 尽量保证函数语句的一致性
例子: 抓取网页中固定的内容, 然后发送给用户

```
def GetContent(ServerAdr, PagePath):
    http = httplib.HTTP(ServerAdr)

    http.putrequest('GET', PagePath)
    http.putheader('Accept', 'text/html')
    http.putheader('Accept', 'text/plain')
    http.endheaders()

    httpcode, httpmsg, headers = http.getreply()

    if httpcode != 200:
        raise "Could not get document: Check URL and Path"

    doc = http.getfile()
    data = doc.read()         # read file: with doc as : doc.read()
    doc.close()

    return data

def ExtractData(inputstring, start_line, end_line):
    lstr = inputstring.splitlines()          # split
    j = 0
    for i in lstr:                           # set counter to zero
        j = j+1
        if i.strip() == start_line:          # find slice start
            slice_start = j
        elif i.strip() == end_line:          # find slice end
            slice_end = j

    return lstr[slice_start : slice_end]      # return slice result

def SendEmail(sender, receiver, smtpserver, username, password, content):
    subject = "Contented get from the web"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()

    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

```
Python中函数设计的好习惯还包括: 不要在函数中定义可变对象作为默认值, 使用异常替换返回错误, 保证通过单元测试等.


### 7. 将常量集中到一个文件

python一般有以下两种方式使用常量:
(1)通过命名风格来提醒使用<F12>者该变量代表意义是常量, 如常量名所有字母大写, 用下划线链接单词. 然而这种方式并没有实现真正意义上的常量, 其值仍然可变.

(2)通过自定义的类实现常量功能.
例子: const.py

```
class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const.%{name}s".format(name = name)
        if not name.isupper():
            raise self.ConstCaseError, "const name %{name}s is not all uppercase"\
            .format(name = name)

        self.__dict__[name] = value

import sys 
sys.modules[__name__] = _const()

```


当其它模块要引用这些常量时, 按照如下方式进行即可:

```
import const
const.MY_CONSTANT = 1
const.MY_SECOND_CONSTANT = 2
const.MY_THIRD_CONSTANT = 'a'
const.MY_FORTH_CONSTANT = 'b'

print(const.MY_SECOND_CONSTANT)
print(const.MY_THIRD_CONSTANT*2)
print(const.MY_FORTH_CONSTANT+'5'
```

