#如果给定一个list或者tuple，我们可以通过for循环来遍历这个list或者tuple， 这种遍历我们称为迭代(Iteration)

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

#isinstance('abc', Iterable) # str是否可迭代true

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
