#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 20.py
# Author: Timilong

# Python检测用户输入的数是否是阿姆斯特丹数

# 获取用户输入
num = int(input("请输入一个数num: "))

# 初始化sum
sum = 0

# n位数指数n
n = len(str(num))

# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

#  输出结果
if sum == num:
    print(num, "是阿姆斯特丹数")
else:
    print(num, "不是阿姆斯特丹数")


print("****获取指定区间的阿姆斯特丹数*****")

# 获取指定区间的阿姆斯特丹数
upper = int(input("请输入数值范围上限: "))
lower = int(input("请输入数值范围的下限: "))

for num in range(lower, upper+1):
    temp = num
    sum = 0
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    # 输出结果
    if sum == num:
        print(num, "是阿姆斯特丹数")

