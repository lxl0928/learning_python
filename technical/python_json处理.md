## python类型和json类型互换

### python对象-->json对象: dump && dumps
编码是将python对象转化为json对象的过程。

#### 1. dump介绍
通过json.dump()将python对象转换成为
json对象生成一个fp的文档流。
简明: dump处理的是文件对象，比如StringIO转化后的字符串

#### 2. dumps介绍
dumps处理的是字符串。
```
import json 

a = ['foo', {'bar': ('baz', None, 1.0, 2)}]  # python对象, list
b = json.dumps(a)  # json对象, str

# dumps(sort_keys, indent, separators, skipkeys)
# sort_keys: 控制是否排序(True or False)
# indent: 定义缩进大小(int类型)
# separators: 定义分隔符类型(tuple类型)
# skipkeys: 默认为False, 如果dict的keys内的数据类型不是python的基本类型(str, unicode, int, long, float, bool, None), 设置为False会报TypeError错误，此时设置为True，则会跳过此类key。
```

### json对象-->python对象: load, loads
解码是将json对象解码成python对象的过程

#### 1. load
和json.dump()相反过程。

#### 2. loads
和json.dumps()相反过程。

### python对象与json对象互换对比介绍

| python对象 | json对象 |
|:---|:---|
|dict|object|
|list, tuple|array|
|str, unicode|string|
|int, long, float|number|
|True|true|
|False|false|
|None|null|


