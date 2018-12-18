# python字典操作高级技巧：http://www.jb51.net/Special/670.htm
# python字典操作方法：http://www.jb51.net/article/66995.htm
### dict 特性

dict用花括号｛｝表示，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。

#### dict的查找速度快
无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢

#### dict 通过key 来查找 value
因此key 不能重复，而value可重复

#### dict储存的"key:value"是无序的
即不可用索引号切片等。

Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。

### 用 dict 表示“名字”-“成绩”的查找表如下：
```
 d = {
 'Adam': 95, #key : value
 'Lisa': 85,
 'Bart': 59
 }
```
我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。

### 访问 dict

创建一个dict，用于表示名字和成绩的对应关系：
```
 d = {
 'Adam': 95,
 'Lisa': 85,
 'Bart': 59
 }
```
使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key返回对应的val。

注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。

### 要避免 KeyError 发生，有两个办法：

#### 先判断一下 key 是否存在，用 in 操作符：
```
 if 'Paul' in d:
	print d['Paul']
```
如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。

#### 使用dict本身提供的一个get方法dict.get(key, default=None)
在Key不存在的时候，返回默认值None：
```
 >>> print d.get('Bart')
 59
 >>> print d.get('Paul')
 None
```
 ### 更新 dict 
dict是可变的，可以随时往dict中添加新的 key-value。比如已有dict：
```
 d = {
 'Adam': 95,
 'Lisa': 85,
 'Bart': 59
 }
```
 要把新同学'Paul'的成绩 72 加进去，用赋值语句：
```
 >>> d['Paul'] = 72 
```
 再看看dict的内容：
```
 >>> print d
 {'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}
```
 如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value：
```
 >>> d['Bart'] = 60
 >>> print d

 {'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60｝
```
### 删除dict元素或清空dict
可使用pop方法: 
dict.pop(key[,default])，通过key值删除dict内元素，并返回被删除key对应的value。
若key不存在，且default值未设置，则返回KeyError异常。
```
>>> a
{1: 'abc', 2: 'efg', 3: 'hij'}
>>> a.pop(1)
'abc'
>>> a
{2: 'efg', 3: 'hij'}
>>> 
>>> a
{2: 'efg', 3: 'hij'}
>>> a.pop(1,False)
False
>>>
```
可使用clear方法dict.clear()清空dict

### 遍历/迭代 dict 

#### for循环遍历
由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。 
```
>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }4
>>> for key in d:
print key,'-',d[key]
Lisa - 85
Adam - 95
Bart - 59
```

#### values() / itervalues() 方法：返回dict 的value值 

values()方法：把 dict 转换成了包含 value 的list 
```
>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> print d.values()
[85, 95, 59]
>>> for v in d.values():
print v
85
95
59
```
 用 itervalues() 方法替代 values() 方法，迭代效果完全一样。
 而 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
 
#### items() / iteritems() 方法：返回dict 的key和value 
 
dict 对象的 items() 方法返回的值：
```
 >>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 } >>> print d.items() [('Lisa', 85), ('Adam', 95), ('Bart', 59)]
```
可以看到，items()方法把dict对象转换成了包含tuple的list，
对这个list进行迭代，可以同时获得key和value：
```
>>> for key, value in d.items(): ... print key, ':', value ... Lisa : 85 Adam : 95 Bart : 59
```
和 values() 有一个 itervalues() 类似， 
items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以，iteritems() 不占用额外的内存。