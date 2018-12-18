## python中itertools模块用法详解

[TOC]

```
这篇文章主要介绍了Python中itertools模块用法,详细的讲述了itertools模块中常见函数的用法及相关示例,有助于深入掌握Python程序设计.
```

一般来说，itertools模块包含创建有效迭代器的函数，可以用各种方式对数据进行循环操作，此模块中的所有函数返回的迭代器都可以与for循环语句以及其他包含迭代器（如生成器和生成器表达式）的函数联合使用。



### (1) chain(iter1, iter2, ..., iterN):

给出一组迭代器(iter1, iter2, ..., iterN)，此函数创建一个新迭代器来将所有的迭代器链接起来，返回的迭代器从iter1开始生成项，直到iter1被用完，然后从iter2生成项，这一过程会持续到iterN中所有的项都被用完。

```
from itertools import chain
test = chain('AB', 'CDE', 'F')
for el in test:
print el

"""结果如下: 
A
B
C
D
E
F
"""
```

### (2) chain.from_iterable(iterables):
一个备用链构造函数，其中的iterables是一个迭代变量，生成迭代序列，此操作的结果与以下生成器代码片段生成的结果相同：
```
>>> def f(iterables):
    for x in iterables:
        for y in x:
            yield y

>>> test = f('ABCDEF')
>>> test.next()
'A'


>>> from itertools import chain
>>> test = chain.from_iterable('ABCDEF')
>>> test.next()
'A'

```

### (3) combinations(iterable, r):
创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序:
```
>>> from itertools import combinations
>>> test = combinations([1,2,3,4], 2)
>>> for el in test:
    print el

    
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```

### (4) count([n]):
创建一个迭代器，生成从n开始的连续整数，如果忽略n，则从0开始计算（注意：此迭代器不支持长整数），如果超出了sys.maxint，计数器将溢出并继续从-sys.maxint-1开始计算。

### (5) cycle(iterable):
创建一个迭代器，对iterable中的元素反复执行循环操作，内部会生成iterable中的元素的一个副本，此副本用于返回循环中的重复项。

### (6) dropwhile(predicate, iterable):
创建一个迭代器，只要函数predicate(item)为True，就丢弃iterable中的项，如果predicate返回False，就会生成iterable中的项和所有后续项。
```
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

### (7) groupby(iterable [,key]):
创建一个迭代器，对iterable生成的连续项进行分组，在分组过程中会查找重复项。

如果iterable在多次连续迭代中生成了同一项，则会定义一个组，如果将此函数应用一个分类列表，那么分组将定义该列表中的所有唯一项，key（如果已提供）是一个函数，应用于每一项，如果此函数存在返回值，该值将用于后续项而不是该项本身进行比较，此函数返回的迭代器生成元素(key, group)，其中key是分组的键值，group是迭代器，生成组成该组的所有项。

### (8) ifilter(predicate, iterable):
创建一个迭代器，仅生成iterable中predicate(item)为True的项，如果predicate为None，将返回iterable中所有计算为True的项。
```
>>> ifilter(lambda x: x%2, range(10)) 
1 3 5 7 9
```

### (9) ifilterfalse(predicate, iterable):
创建一个迭代器，仅生成iterable中predicate(item)为False的项，如果predicate为None，则返回iterable中所有计算为False的项。
```
>>> ifilterfalse(lambda x: x%2, range(10)) 
0 2 4 6 8
```

### (10) imap(function, iter1, iter2, iter3, ..., iterN)
创建一个迭代器，生成项function(i1, i2, ..., iN)，其中i1，i2...iN分别来自迭代器iter1，iter2 ... iterN，如果function为None，则返回(i1, i2, ..., iN)形式的元组，只要提供的一个迭代器不再生成值，迭代就会停止。
```
>>> from itertools import *
  >>> d = imap(pow, (2,3,10), (5,2,3))
  >>> for i in d: print i
  
  32
  9
  1000
  
 ####
 >>> d = imap(pow, (2,3,10), (5,2))
 >>> for i in d: print i
 
 32
 9

 ####
 >>> d = imap(None, (2,3,10), (5,2))
 >>> for i in d : print i
 
 (2, 5)
 (3, 2)
```

### (11) islice(iterable, [start, ] stop [, step]):
创建一个迭代器，生成项的方式类似于切片返回值： iterable[start : stop : step]，将跳过前start个项，迭代在stop所指定的位置停止，step指定用于跳过项的步幅。与切片不同，负值不会用于任何start，stop和step，如果省略了start，迭代将从0开始，如果省略了step，步幅将采用1.
```
def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(xrange(s.start or 0, s.stop or sys.maxint, s.step or 1))
    nexti = next(it)
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)
 
#If start is None, then iteration starts at zero. If step is None, then the step defaults to one.
#Changed in version 2.5: accept None values for default start and step.
```

### (12) izip(iter1, iter2, ... iterN):
创建一个迭代器，生成元组(i1, i2, ... iN)，其中i1，i2 ... iN 分别来自迭代器iter1，iter2 ... iterN，只要提供的某个迭代器不再生成值，迭代就会停止，此函数生成的值与内置的zip()函数相同。
```
def izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterables = map(iter, iterables)
    while iterables:
        yield tuple(map(next, iterables))
```

### (13) izip_longest(iter1, iter2, ... iterN, [fillvalue=None]):
与izip()相同，但是迭代过程会持续到所有输入迭代变量iter1,iter2等都耗尽为止，如果没有使用fillvalue关键字参数指定不同的值，则使用None来填充已经使用的迭代变量的值。
```
def izip_longest(*args, **kwds):
    # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    def sentinel(counter = ([fillvalue]*(len(args)-1)).pop):
        yield counter()         # yields the fillvalue, or raises IndexError
    fillers = repeat(fillvalue)
    iters = [chain(it, sentinel(), fillers) for it in args]
    try:
        for tup in izip(*iters):
            yield tup
    except IndexError:
        pass
```

### (14) permutations(iterable [,r]):
创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同：
```
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

### (15) product(iter1, iter2, ... iterN, [repeat=1]):
创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数。
```
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```

### (16) repeat(object [,times]):
创建一个迭代器，重复生成object，times（如果已提供）指定重复计数，如果未提供times，将无止尽返回该对象。
```
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in xrange(times):
            yield object
```

### (17) starmap(func [, iterable]):
创建一个迭代器，生成值func(*item),其中item来自iterable，只有当iterable生成的项适用于这种调用函数的方式时，此函数才有效。
```
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
```
### (18) takewhile(predicate [, iterable]):
创建一个迭代器，生成iterable中predicate(item)为True的项，只要predicate计算为False，迭代就会立即停止。
```
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```

### (19) tee(iterable [, n]):
从iterable创建n个独立的迭代器，创建的迭代器以n元组的形式返回，n的默认值为2，此函数适用于任何可迭代的对象，但是，为了克隆原始迭代器，生成的项会被缓存，并在所有新创建的迭代器中使用，一定要注意，不要在调用tee()之后使用原始迭代器iterable，否则缓存机制可能无法正确工作。
```
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                newval = next(it)       # fetch a new value and
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)

#Once tee() has made a split, the original iterable should not be used anywhere else; otherwise, 
the iterable could get advanced without the tee objects being informed.
#This itertool may require significant auxiliary storage (depending on how much temporary data needs to be stored). 
In general, if one iterator uses most or all of the data before another iterator starts, it is faster to use list() instead of tee().
```
