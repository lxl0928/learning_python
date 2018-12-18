## 使用copy模块深拷贝对象

### 浅拷贝
shallow copy：构造一个新的复合对象并将从元对象发现的引用插入该对象中。
浅拷贝的实现方式有很多种：工厂函数、切片操作、copy模块中的copy

### 深拷贝
deep copy：构造一个新的复合对象，但是遇到引用会继续递归拷贝其所指向的具体内容。
也就是说它会针对应用所指向的对象继续执行拷贝，因此产生的对象不受其他引用对象操作的影响。
深拷贝的实现需要依赖copy模块的deepcopy()操作。

```
#! /usr/bin/env python3
# coding: utf-8

import copy

class Pizza(object):
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
    
    def get_pizza_info(self):
        return self.name, self.size, self.price

    def show_pizza_info(self):
        print("Pizza name: ", self.name)
        print("Pizza size: ", str(self.size))
        print("Pizza price: ", str(self.price))

    def change_size(self, size):
        self.size = size

    def change_price(self, price):
        self.price = price


class Order(object):
    def __init__(self, name):
        self.customername = name
        self.pizzaList = []
        self.pizzaList.append(Pizza("Mushroom", 12, 30))

    def order_more(self, pizza):
        self.pizzaList.append(pizza)

    def change_name(self, name):
        self.customername = name

    def get_order_detail(self):
        print("Customer name: ", self.customername)
        for i in self.pizzaList:
            i.show_pizza_info()

    def get_pizza(self, number):
        return self.pizzaList[number]


customer1 = Order("Timilong")
customer1.order_more(Pizza("seafood", 9, 40))
customer1.order_more(Pizza("fruit", 12, 35))
print("customer1 oreder infomation: ")
customer1.get_order_detail()
print("-----------------------------------")

customer2 = copy.copy(customer1)
print("order 2 customer name: ", customer2.customername)
customer2.change_name("Lixiaolong")
customer2.get_pizza(2).change_size(9)
customer2.get_pizza(2).change_price(30)
print("customer2 order informat: ")
customer2.get_order_detail()
print("---------------------------------")

print("customer1 oreder infomation: ")
customer1.get_order_detail()
```

### 输出结果
```
customer1 oreder infomation: 
Customer name:  Timilong
Pizza name:  Mushroom
Pizza size:  12
Pizza price:  30
Pizza name:  seafood
Pizza size:  9
Pizza price:  40
Pizza name:  fruit
Pizza size:  12
Pizza price:  35
-----------------------------------
order 2 customer name:  Timilong
customer2 order informat: 
Customer name:  Lixiaolong
Pizza name:  Mushroom
Pizza size:  12
Pizza price:  30
Pizza name:  seafood
Pizza size:  9
Pizza price:  40
Pizza name:  fruit
Pizza size:  9
Pizza price:  30
---------------------------------
customer1 oreder infomation: 
Customer name:  Timilong
Pizza name:  Mushroom
Pizza size:  12
Pizza price:  30
Pizza name:  seafood
Pizza size:  9
Pizza price:  40
Pizza name:  fruit
Pizza size:  9
Pizza price:  30

```

### 说明
```
customer2的订单通过copy.copy(customer1)获得，通过id函数查看customer2中的pizzaList的具体Pizza对象，
发现它们和customer1的输出是一样的。
这是由于通过copy.copy()得到的customer2是customer1的一个浅拷贝，它仅仅拷贝了pizzaList里面对象的地址
而不对对应地址所指向的具体内容(即具体的pizza)进行拷贝
因此，customer2中的pizzaList所指向的具体内容是和customer1中一样的。
所以，对customer2的fruit的修改直接影响了customer1的订单内容。
实际上在包含引用的数据结构中，浅拷贝并不能进行彻底的拷贝，当存在字典、列表等可变对象的时候，
它仅仅拷贝其引用地址。
```
要解决上述问题，就需要用到深拷贝，深拷贝不仅拷贝引用也拷贝引用所指向的对象，
因此深拷贝得到的对象和原对象是相互独立的。
所以，上述代码应该改为:
```
customer2 = copy.deepcopy(customer1)
```

