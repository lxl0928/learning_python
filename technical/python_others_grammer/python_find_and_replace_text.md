[TOC]

## 在Python中查找和替换文本

### 最简单的查找替换

在Python中查找和替换非常简单，如果当前对象是一个字符串str时，你可以使用该类型提供的find()或者index()方法查找指定的字符，如果能找到则会返回字符第一次出现的索引，如果不存在则返回-1。
```
>>> s = 'Cat and Dog'
>>> s.find('Dog')
8
>>> s.index('Dog')
8
>>> s.find('Duck')
-1

```

如果要替换目标字符串，用replace()方法就好了。
```
>>> s = 'Cat and Dog'
>>> s.replace('Cat', 'Dog')
'Dog and Dog'
```

### 通配符查找匹配

当然，如果你觉得上面的功能还不能满足你，你想使用通配符来查找字符串？没问题！fnmatch这个库就能满足你的要求，看例子！
```
>>> s = 'Cat and Dog'
>>> import fnmatch
>>> fnmatch.fnmatch(s,'Cat*')
True
>>> fnmatch.fnmatch(s,'C*and*D?')
False
>>> fnmatch.fnmatch(s,'C*and*D*')
True
```

### 正则表达式查找替换

如果你需要查找比较复杂的字符规则，正则表达式是你不二的选择。下面是正则查找的简单示例。
```
>>> import re
>>> s = 'We will fly to Thailand on 2016/10/31'
>>> pattern = r'\d+'
>>> re.findall(pattern, s)
['2016', '10', '31']
>>> re.search(pattern, s)
<_sre.SRE_Match object at 0x03A8FD40>
>>> re.search(pattern, s).group()
'2016'
```

接下来你可能需要用正则表达式去替换某些字符，那么你需要了解re.sub()方法，看例子。
```
>>> s = "I like {color} car."
>>> re.sub(r'\{color\}','blue',s)
'I like blue car.'
>>> s = 'We will fly to Thailand on 10/31/2016'
>>> re.sub('(\d+)/(\d+)/(\d+)', r'\3-\1-\2', s)
'We will fly to Thailand on 2016-10-31'

```

其实re.sub()远比你相像的强大的多。在上面的例子里你可以替换类似于{color}这样的模板字符，也可以把正则匹配到的所有分组调换顺序，例如第二个例子一共匹配了3个分组，然后把第3个分组放到最前面 r'\3-\1-\2'，看明白了吗？

接下来看另外一个例子。
```
s = "Tom is talking to Jerry."
name1 = "Tom"
name2 = "Jerry"

pattern = r'(.*)({0})(.*)({1})(.*)'.format(name1, name2)
print re.sub(pattern, r'\1\4\3\2\5', s)
# Jerry is talking to Tom.
```

其实你还可以自定义替换函数，也就是re.sub()的第二个参数。
```
def change_date(m):
    from calendar import month_abbr
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

s = 'We will fly to Thailand on 10/31/2016'
pattern = r'(\d+)/(\d+)/(\d+)'
print re.sub(pattern, change_date, s)
# We will fly to Thailand on 31 Oct 2016
```

最后给大家一个终极版的例子，里面用到了函数的闭包，着酸爽，你懂的！
```
def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

s = "LOVE PYTHON, love python, Love Python"
print re.sub('python', match_case('money'), s, flags=re.IGNORECASE)
# LOVE MONEY, love money, Love Money
```

### 写在最后

其实正则表达式还有很多玩法，如果你想让正则和通配符混合着用，一点问题都没有，因为fnmatch还有一个translate()的方法，可以让你把通配符无痛转换成正则表达式.
```
>>> fnmatch.translate('C*and*D*')
'C.*and.*Ｄ.*'
```
