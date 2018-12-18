#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 19.py
# Author: Timilong

# 初始化头两项
n1 = 0
n2 = 1
# 计数器置为2
count = 2
# 接受用户输入num
num = int(input("输入一个正整数: "))

# 条件判断num<=0
if num <= 0:
    print("请输入一个正整数num: ")
    num = int(input())

# num = 1
elif num == 1:
    print("1的前{0}项斐波拉切数列是".format(num))

# num >= 2
else:
    print("斐波拉切数列: ")
    print(n1, ',', n2, end=" , ")
    while count < num:
        nth = n1 + n2;
        if count < num - 1:
            print(nth, end=" , ")
        else:
            print(nth, end=".")
        n1 = n2
        n2 = nth
        count += 1

# 更新n1, n2
print()
