#Python内建了map()和reduce()函数

#map()

#map()函数接收两个参数，一个是函数，一个是Iterable(序列：字符串、数据、列表)，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

#实现一个函数： f(x) = x*x
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print("\n", list(r), "\n")

#map传入的第一个参数是f， 即函数对象本身， 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x*x，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串:
list(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#reduce()

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#例子： 序列求和:
from functools import reduce
def add(x, y):
    return x+y;

reduce (add, [1, 3, 5, 7, 9])

#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
from functions import reduce
def add1(x, y):
    return x*10 + y
reduce(add1, [1, 3, 5, 7, 9])

#reduce+map函数实现字符串转整型

from functools import reduce
def str2int:
    def fn(x, y):
        return x*10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

#使用lambda进一步简化成:
from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


