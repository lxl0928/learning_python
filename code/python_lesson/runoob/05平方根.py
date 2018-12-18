#! /usr/bin/python3 
# -*- coding: utf-8 -*-

num1 = float(input("请输入一个数: "))

root1 = num1 ** 0.5

print("{num1}的平方根是{root1}".format(num1=num1, root1=root1))

print("*****第二种方法:使用cmath库*****")

num2 = float(input("请输入一个数: "))

import cmath

root2 = cmath.sqrt(num2)

print("{num2}的平方根是{root2}".format(num2=num2, root2=root2))
