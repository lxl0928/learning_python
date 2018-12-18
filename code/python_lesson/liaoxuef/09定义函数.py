#定义函数
#在python中，定义一个函数要使用def语句，依次写出函数名字， 括号， 括号中的参数和冒号：， 然后， 在缩进块中编写函数体， 函数的返回值用return语句返回

#我们自定义一个求绝对值的my_abs函数为例子
def my_abs(x):
    if x > 0:
        return x;
    else:
        return -x;

print("\n")

#如果已经把my_abs()的函数定义保存为abstest.py文件了， 那么， 可以在该文件的当期那目录下启动python解释器， 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名字）

#空函数
#如果向定义一个什么也不做的空函数， 可以用pass语句
def nop():
    pass
#实际上pass可以用来作占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass， 让代码能运行起来

#参数检查

#数据类型检查可以用内置函数isinstance()实现

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


#返回多个值

#函数可以返回多个值，比如在函数中需要从一个点移动到另外一个点，给出坐标、位移、和角度， 就可以计算出新的坐标

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


#其中， import math就是导入math包，并允许后序代码引用math包里的sin, cos等函数
#然后，我们就可以同时获得返回值:

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

#但其实这是一种假象， python返回值仍然是单一值：

r = move(100, 100, 60, math.pi/60)
print(r)

#结果是: (151.96..., 70.0)
#原来返回值是一个tuple, 但是，在语法上面， 返回一个tuple可以省略括号， 而多个变量可以同时接收一个tuple，按位置赋值给对应的值，所以Python的函数返回多值实际上就是返回一个tuple，但是写起来很方便



