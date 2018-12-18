#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 10.py
# Author: Timilong

# 用户输入待交换的两个数
a = input("请输入数a: ")
b = input("请输入数b: ")

# 打印交换前
print("a = ", a)
print("b = ", b)

# 执行交换
temp = a;
a = b;
b = temp;

# 打印交换后的结果
print("交换后")
print("a = {num1}".format(num1=a))
print("b = {num2}".format(num2=b))


# 第二种方法：不使用临时变量
print("*****第二种方法：不适用临时变量*****")
x = input("请输入x的值: ")
y = input("请输入y的值: ")

# 打印交换前
print("交换前")
print("x = ", x)
print("y = ", y)
# 直接交换
x, y = y, x

# 打印
print("交换后")
print("x = ", x)
print("y = ", y)


