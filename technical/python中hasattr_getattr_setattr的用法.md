## Python的hasattr() getattr() setattr() 函数使用方法详解

### hasattr(object, name)
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
需要注意的是name要用括号括起来

```
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> hasattr(t, "name") #判断对象有name属性
 8 True
 9 >>> hasattr(t, "run")  #判断对象有run方法
10 True
11 >>>
```
### getattr(object, name[,default])
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号。

```
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> getattr(t, "name") #获取name属性，存在就打印出来。
 8 'xiaohua'
 9 >>> getattr(t, "run")  #获取run方法，存在就打印出方法的内存地址。
10 <bound method test.run of <__main__.test instance at 0x0269C878>>
11 >>> getattr(t, "run")()  #获取run方法，后面加括号可以将这个方法运行。
12 'HelloWord'
13 >>> getattr(t, "age")  #获取一个不存在的属性。
14 Traceback (most recent call last):
15   File "<stdin>", line 1, in <module>
16 AttributeError: test instance has no attribute 'age'
17 >>> getattr(t, "age","18")  #若属性不存在，返回一个默认值。
18 '18'
19 >>>
```
 

### setattr(object, name, values)
给对象的属性赋值，若属性不存在，先创建再赋值。

```
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> hasattr(t, "age")   #判断属性是否存在
 8 False
 9 >>> setattr(t, "age", "18")   #为属相赋值，并没有返回值
10 >>> hasattr(t, "age")    #属性存在了
11 True
12 >>>
```
 

### 一种综合的用法是：判断一个对象的属性是否存在，若不存在就添加该属性。

```
 1 >>> class test():
 2 ...     name="xiaohua"
 3 ...     def run(self):
 4 ...             return "HelloWord"
 5 ...
 6 >>> t=test()
 7 >>> getattr(t, "age")    #age属性不存在
 8 Traceback (most recent call last):
 9   File "<stdin>", line 1, in <module>
10 AttributeError: test instance has no attribute 'age'
11 >>> getattr(t, "age", setattr(t, "age", "18")) #age属性不存在时，设置该属性
12 '18'
13 >>> getattr(t, "age")  #可检测设置成功
14 '18'
15 >>>
```
