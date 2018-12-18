## python3中的字符串调用方法


### 搜索方法
1. S.find(sub [, start [, end]])
在start(默认为0)到end(默认len(S))中搜索子串sub第一次出现的偏移量，如果不存在，返回-1

2. S.rfind(sub [, start [, end]])
类似find，从末端扫描，从end到start，第一次出现sub的偏移量被返回

3. S.index(sub [, start [, end]])
类似find,但如果没有找到，不是返回-1,而是返回ValueError

4. S.rindex(sub [, start [, end]])
类似rfind。

5. S.count(sub [, start [, end]])
从偏移量start到end(默认0:lend(S中统计S中子串sub非重叠出现的次数。

6. S.startswith(sub [, start [, end]])
如果字符串S从某个子字符串开始，这个子字符串任意给定了与sub相匹配的开始点和结束点sub. start和end，则为真

7. S.endswith(sub, [, start [, end]])
如果字符串S从某个子字符串结束，这个子字符串任意给定了与sub相匹配的开始点和结束点sub.
start和end，则为真。


### 分解与连接方法
1. S.split([sep [, maxsplit]])
返回字符串S中的一个单词列表，列表以sep作为字符串的定界符。如果给定maxsplit,则最多完成maxsplit个分解。
如果不指定sep或为None，则用空白字符串作为分隔符。
'a*b'.split('*')得到['a', 'b']。
提示：使用list(S)讲字符串转换为 一个字符列表(如, ['a', '*', 'b'])

2. S.join(iterable)
将一个可迭代读取的字符串(如，列表或元组)连接成一个单一字符串项，在每个项间添加S.S可以是''，以便将可迭代字符转换成为字符串((a, b).join('*')->'a*b'

3. S.replace(old, new [, count])
返回一个字符串S的拷贝。S中子字符串old中的所有事件均被new锁替换。如果传递了count, 最初的count(计数)事件被替换。这项工作类似x = S.split(old)和new.join(x)的组合

4. S.splitlines([keepends])
在换行符处分解字符串S，返回行列表。结果中不保留换行符字符，除非keepends为真。


### 格式化方法
1. S.format(*args, **kwargs), S.format_map(mapping)


2. S.capitalize()


3. S.expandtabs([tabsize])


4. S.strip([chars])


5. S.lstrip([chars])


6. S.rstrip([chars])


7. S.swapcase()


8. S.upper()


9. S.lower()


10. S.casefold()


11. S.ljust()


12. S.rjust()


13. S.center(width [, fill])


14. S.zfill(width)


15. S.translate(table [, deletechars])


16. S.title()


### 内容检测方法

1. S.is*()


### 截取子串方法

ins = u"我是中国人"
print(ins[2:4])