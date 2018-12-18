[TOC]

## 如何在列表，字典，集合中根据条件筛选数据?

![筛选数据](http://ogba4u3pk.bkt.clouddn.com/%E5%A6%82%E4%BD%95%E5%9C%A8%E5%88%97%E8%A1%A8,%20%E5%AD%97%E5%85%B8,%20%E9%9B%86%E5%90%88%E4%B8%AD%E6%A0%B9%E6%8D%AE%E6%9D%A1%E4%BB%B6%E7%AD%9B%E9%80%89%E6%95%B0%E6%8D%AE.png)

1) for循环迭代
```
data = [1, 5, -3, -2, 6, 8, 9]

res = []
for x in data:
    if x >= 0:
        res.append(x)

print(res)
```

![其它解决方案](http://ogba4u3pk.bkt.clouddn.com/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88.png)

2) 使用filter函数
```
# 运行环境: python 2.7

from random import randint

# 生成list: 生成10个-10到10的范围内的list
data = [randint(-10, 10) for _ in xrange(10)]

# 打印list
print "data: ", data

# 使用filter
res = filter(lambda x: x>= 0, data)

# 打印结果
print "res: ", res
```

输出结果: 
```

```
