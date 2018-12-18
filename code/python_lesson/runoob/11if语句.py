#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 11.py
# Author: Timilong

# 用户输入数字，程序判断这个数的正负属性，并打印结果

# 用户输入
num = float(input("请输入一个数字num: "))

# 程序判断
if num > 0:
    print("{num}是正数.".format(num=num))
elif num == 0:
    print("{num}是零.".format(num=num))
else:
    print("{num}是负数.".format(num=num))

# 方法二:内嵌if
print()
print("*****方法二：内嵌的if语句*****")
num1 = float(input("请输入一个数字num1: "))

# 判断程序
if num1 >= 0:
    if num1 > 0:
        print("{num}是正数.".format(num=num1))
    else:
        print("{num}是零.".format(num=num1))
else:
    print("{num}是负数.".format(num=num1))



