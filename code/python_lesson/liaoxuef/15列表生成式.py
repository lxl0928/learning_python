#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用
list(range(1, 11))：

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
[x * x for x in range(1, 11)]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]

#还可以使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

#列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
for k, v in d.items()

#列表生成式也可以使用两个变量来生成list
[k + '=' + v for k, v in d.items()]

#使用内建的isinstance函数可以判断一个变量是不是字符串
isinstance(x, str)


