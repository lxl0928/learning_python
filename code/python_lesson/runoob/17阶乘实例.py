#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 17.py
# Author: Timilong

# 接受用户输入一个数num
num = int(input("请输入一个数num: "))

# 小于0
if num < 0:
    print("对不起, 负数没有阶乘.")

# 等于0
elif num == 0:
    print("0的阶乘是0.")

# 大于0
else:
    factorial = 1;
    for i in range(1, num+1):
        factorial *= i
    print("{0}的阶乘为{1}".format(num, factorial))
