# 函数的参数

### 位置参数
###### 我们先写一个计算x平方的函数:

```
def power(x):
    return x*x
```

###### 对于power(x)函数，参数x就是一个位置参数, 当我们调用power函数时候，必须传入有且仅有的一个参数x:
###### 现在我们要计算x的三次方，我们可以把power(x)修改为power(x, n),用来计算x的n次方

```
def power(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
```

###### 对于这个修改的power(x, n)函数，可以计算任意的n次方
###### 修改后的power(x, n)函数有两个参数, x,n都是位置参数， 调用函数时候， 传入的两个值按照位置顺序依次赋值给参数x和n

### 默认参数
###### 新的power(x, n)函数定义没有问题， 但是, 旧的代码失败了，原因是我们增加了一个参数， 导致旧的代码因为缺少一个参数而无法正常使用

###### 由于我们经常调用x的平方，我们完全可以把n的默认值设置为2

```
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
```

###### 使用默认参数最大的好处是降低调用函数的难度

###### Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
###### 所以定义默认参数要牢记一点: 默认参数必须指向不变的对象！
###### 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

### 可变参数
###### 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
###### 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

###### 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

```
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

###### 但是调用的时候，需要先组装出一个list或tuple：

```
    >>> calc([1, 2, 3])
    14
    >>> calc((1, 3, 5, 7))
    84
```

###### 如果利用可变参数，调用函数的方式可以简化成这样：

```
    >>> calc(1, 2, 3)
    14
    >>> calc(1, 3, 5, 7)
    84
```

###### 所以，我们把函数的参数改为可变参数：

```
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
```

###### 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

```
    >>> calc(1, 2)
    5
    >>> calc()
    0
```

###### 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

```
    >>> nums = [1, 2, 3]
    >>> calc(nums[0], nums[1], nums[2])
    14
```

###### 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

```
    >>> nums = [1, 2, 3]
    >>> calc(*nums)
    14
```

###### *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

### 关键字参数
###### 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

###### 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：

```
>>> person('Michael', 30)
name: Michael age: 30 other: {}
```

###### 也可以传入任意个数的关键字参数：

```
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```




###### 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
###### 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

```
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

###### 当然，上面复杂的调用可以用简化的写法：

```
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

###### **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
###### 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
######仍以person()函数为例，我们希望检查是否有city和job参数：

```
def person(name, age, **kw):
    if 'city' in kw:
    # 有city参数
        pass
    if 'job' in kw:
    # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```

###### 但是调用者仍可以传入不受限制的关键字参数：

```
>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
```

###### 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

```
def person(name, age, *, city, job):
    print(name, age, city, job)
```

###### 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。调用方式如下：

```
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```

###### 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

```
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```

###### 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数.命名关键字参数可以有缺省值，从而简化调用：

```
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```

###### 由于命名关键字参数city具有默认值，调用时，可不传入city参数：

```
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
```

###### 使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

```
def person(name, age, city, job):
        # 缺少 *，city和job被视为位置参数
    pass
```

### 参数组合
###### 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。

###### 比如定义一个函数，包含上诉若干种参数:

```
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```

###### 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

```
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

###### 最神奇的是通过一个tuple和dict，你也可以调用上述函数：

```
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

###### 所以， 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


