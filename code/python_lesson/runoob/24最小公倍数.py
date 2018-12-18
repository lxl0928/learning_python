#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 24.py
# Author: Timilong

# 定义最小公倍数函数
def lcm(x, y):
    # 判断两个数的大小
    if x > y:
        greater = x
    else:
        greater = y

    # 循环中判断最小公倍数
    while(True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

# 获取用户输入
x = int(input("请输入一个数x: "))
y = int(input("请输入一个数y: "))

# 获取最小公倍数
lcm = lcm(x, y)

# 打印
print(x, y, "的最小公倍数为: ", lcm)
