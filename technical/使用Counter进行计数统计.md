## 使用Counter进行计数统计

### 使用dict
```
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = dict()
for item in some_data:
    if item in count_frq:
        count_frq[item] += 1
    else:
        count_frq[item] = 1
print("result: ", count_frq)
```

### 使用defaultdict
```
from collections import defaultdict

some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = defaultdict(int)
for item in some_data:
    count_frq[item] += 1

print("result: ", count_frq)
```

### 使用set和list
```
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_set = set(some_data)
count_list = []
for item in count_set:
    count_list.append((item, some_data.count(item)))

print("result: ", count_frq)
```

### 使用collections.Counter
```
from collections import Counter

some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']

print("result: ", Counter(some_data))
```

