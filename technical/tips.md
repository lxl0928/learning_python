## python中的tips

1. 类型判断推荐isinstance
```
isinstance(object, classinfo)
isinstance(2, int) # True
isinstance('a', (str, unicode)) # True
isinstance(True, bool) # True 
isinstance((1,2), (str, list, tuple)) # True
```

2. 使用enumerate()获取序列迭代的索引和值
```
li = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(li):
    print("index: ", i, "element: ", e)
```

3. 善用延迟计算(lazy evalation)
```
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
from itertools import islice
print list(islice(fib(), 5))
# [0, 1, 1, 2, 3]
```

4. 区别对待可变对象和不可变对象
```
python中一切皆对象，每一个对象都有一个唯一的标识符(id()),类型(type())以及值。
不可变对象: 数字、字符串、元组
可变对象: 字典、列表、字节数组、集合等。

默认参数在函数被调用的时候仅仅被评估一次，以后都会使用第一次评估的结果。
我们将可变参数设置为函数默认参数时候特别警惕这一点，可变参数是可变的，默认参数只被评估一次。
解决方法:
    传入默认参数时设置值为None, 而不是具体某一可变参数类型如[]
```

5. 函数传参既不是传值，也不是传引用
```
正确的叫法是传对象。

函数参数在传递的过程中将整个对象传入，
可变对象： 对可变对象的修改在函数内部外部都可建，调用者和被调用者共享这个对象。
不可变对象：由于不能真正被修改，因此，修改往往是通过生成一个新对象后赋值来实现的。
```
