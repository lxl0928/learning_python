title: Python简明教程
date: 2016-04-24 22:00:03

---

### 版本
python2和python3是目前两个主要的版本。
如下两种情况下，建议使用Python2.7:
* 无法控制即将部署的环境时候。
* 需要使用一些特定的第三方包或者扩展的时候。

<!--more-->

Python是官方推荐且是未来全力支持的版本，目前很多功能提升仅在python3版本上进行。

### hello world
* 创建hello.py
* 编写程序:
```
if __name__ == '__mian__':
print "hello world"
```
* 运行程序
```
python ./hello.py
```

### 注释
* 无论是行注释韩式段注释，均以‘#‘加一个空格来注释。
* 如果需要在代码中使用中文注释，必须在python文件的最前面加上如下注释说明:
```
# -* - conding: UTF-8 -* -
```
* 如下注释用于指定解释器
```
#! /usr/bin/python
```

### 文件类型
* python的文件类型分为3种: 源代码、字节代码、优化代码。这些都是可以直接运行，不需要进行编译或者连接。
* 源代码以.py为扩展名，由python来负责解释；
* 源文件经过编译后生成扩展名为.pyc的文件，即编译过的字节文件。这种文件不能使用文本编辑器修改。pyc文件是和平台无关的，可以在大部分操作系统上运行。
如下pyc文件:
```
import py_compile
py_compile.compile('hello.py')
```
* 经过优化的源文件会以.pyo为后缀，即优化代码。它也不能直接用文本编辑器修改。
如下命令可以用来生成pyo文件:
```
python -o -m py_compile hello.py
```

### 变量
* python中的变量不需要声明，变量的赋值操作及时变量声明和定义的过程。
* python中一次新的赋值，将创建一个新的变量。及时变量的名称相同，变量的标识并不相同。
用id()函数可以获取变量的标识:
```
x = 1
print id(x)
x = 2
print id(x)
```
* 如果变量没有赋值，则python认为该变量不存在。
* 在函数之外定义的变量都可以称为全局变量。全局变量可以被文件内部的任何函数和外部文件访问。
* 全局变量建议在文件的开头定义。
* 也可以把全局变量放到一个专门的文件当中，然后通过import来引用。
gl.py文件中的内容如下:
```
_a = 1
_b = 2
```
use_global.py中引用全局变量:
```
import gl
def fun():
    print gl._a
    print gl._b
fun()
```

### 常量
python中没有提供定义常量的保留字。可以自己定义一个常量类来实习那常量的功能。
```
class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const.%s" % name
        if not name.isupper():
            raise self.ConstCaseError, \
                'const name "%s" is not all uppercase' %  name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()
```
如果上面的代码对应的模块名为const, 使用的时候只需要import const，便可以直接定义常量了。
如以下代码:
```
import const
const.COMPANY = "IBM"
```
上面的代码中的常量一旦赋值便不可再修改。
* python的数字分为整型、长整型、浮点型、布尔型、复数型。
* python没有字符型
* python内部没有普通类型
* 如果需要查看变量的类型，可以使用type类，　该类可以返回变量的类型或创建一个新的类型。
* python有三种表示字符串类型的方式，　即单引号、双引号、三引号。单引号和双引号的作用是相同的。
python程序员员更喜欢单引号，C/Java程序员则习惯使用双引号表示字符串。三引号中可以输入单引号、双引号或者换行等字符。

### 运算符和表达式
* python不支持自增运算符和自减运算符。i++/i--是错误的，但是i += 1是允许的。
* 1/2在python2.5之前会等于0.5，在pytho2.5后会等于０．
* 不等于是" != "或者"<>"
* 等于用" == "
* 逻辑表达式中: and(与)、or(或)、not(非)

### 控制语句
* 


