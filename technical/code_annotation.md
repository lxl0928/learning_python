## python函数注释规范

```
def FuncName(parameter1, parameter2):
    """ Describe what this function does
        # "Find whether the special string is in the queue or not"
        Args: 
            parameter1: patameter type, what is this parameter used for.
                        # strqueue: string, string queue list for search.
            parameter2: patameter type, what is this parameter used for.
                        # str: String, string to find
        Returns:
            return type, return value.
            # boolean, sepcial string string found return True, else return False.
    """
    function body
    ...
    ...
```

## pep常用风格
```
1. 类与类、函数与函数间隔两个空行

2. 类中的函数与函数之间间隔一个空行

3. import相关包放入py文件上部, 如下:
#! /usr/bin/env python3 
# coding: utf-8

from collections import Counter, defaultdict


some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']


def test_counter():
    print("result: ", Counter(some_data))


def test_defaultdict():
    count_frq = defaultdict(int)
    for item in some_data:
        count_frq[item] += 1
    print("result: ", count_frq)


def test_set_list():
    count_set = set(some_data)
    count_list = []
    for item in count_set:
        count_list.append((item, some_data.count(item)))

    print("result: ", count_list)

4. 简单的函数不需要doc_string

#! /usr/bin/env python
# coding: utf-8

def num2str(num: int) -> str:
    return str(num)

5. 函数命名用小写字母，用'_'连接不同单词, 如 def show_pizza_info(self):

6. 类命名用大写字母开头，如 class CreateReport(object):
```


