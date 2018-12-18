#python内置类字典: dict的支持，dict全称dictionary， 在其它语言总和功能也称为map， 使用键-值(key-value)存储，具有极快的查找速度.
#如果要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['A', 'B', 'C']
scores = [99, 98, 97]

#如果用dict实现，只需要一个名字-成绩的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
d = ['A': 99, 'B': 98, 'C': 97]
print('A的成绩： ', d[A])

print("\n")

#要避免key不存在的错误， 有两种办法，一是通过in判断key是否存在：

#二是通过dict提供的get方法，如果key不存在，可以返回None, 或者自己指定的value

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除

print("\n")

#set

#set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以，在set中，没有重复的key

#通过add(key)方法可以添加元素到set中， 可以重复添加但是不会有任何效果

#通过remove(key)方法可以删除元素:

#set可以看成数学意义上面的无序和无重复元素的集合，  因此，两个set可以做数学意义上的交集并集等操作


