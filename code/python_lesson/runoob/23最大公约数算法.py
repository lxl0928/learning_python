#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 23.py
# Author: Timilong

# 求两个数的最大公约数
def hcf(a, b):
# 判断两个数的大小
    if a>b:
        smaller = b
    else:
        smaller = a

    # 在较小的数内进行循环求余，判断余数是否为0
    for num in range(1, smaller+1):
        # 满足条件返回最大公约数
        if (a % num == 0) and (b % num == 0):
            hcf = num
    return hcf

# 获取用户输入
x = int(input("请输入一个数x:"))
y = int(input("请输入一个数y:"))

# 调用函数
ans = hcf(x, y)

# 打印结果
print(x, y, "的最大公约数为: ", ans)    

