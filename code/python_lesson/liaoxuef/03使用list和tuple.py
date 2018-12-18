#python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
#列出班里所有同学电费名字， 就可以用一个list表示

classmates = ['tjy', 'bob', 'timilong']

print(classmates)
print("\n")

classmatesLen = len(classmates)

print("班级人数为: ", classmatesLen)
print("\n")

#往list的末尾追加元素:
classsmates.append('Adam')

#插入元素到指定位置
classmates.insert(1, 'Jack')
print("\n")

print(classmates)
print("\n")

#删除列表末尾元素
classmates.pop()

print(classmates)
print("\n")

#list里面的数据类型可以不同

L = ['Apple', 123, True]

print(L)
print("\n")

#list元素也可以是另外一个list

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(s);
print("s的长度：", len[s])

#list中的元素可以一个都没有, 就是一个空list， 它的长度为0

LL = []

print("LL的长度为:", len(LL))


#另一种有序列表叫做元组: tuple。 tuple和list非常类似。但是tuple一旦厨师换就不能修改，比如刚刚列出同班同学的名字

tupleclass = ('Michael', 'Bob', 'Tracy')

#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
#tuple陷阱: 当你定义个tuple时候， 在定义的时候，tuple的元素就必须被确定下来

print("\n")

print("请用索引取出下面list的指定元素:")
mylist = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
        ]
print("\n")
print("打印Apple:", mylist[0][0])
print("\n打印Python:", mylist[1][1])
print("\n打印Lisa:", mylist[2][2])




