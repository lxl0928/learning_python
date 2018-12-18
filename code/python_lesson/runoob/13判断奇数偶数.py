#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 13.py
# Author: Timilong

# 输入一个数
num = float(input("请输入一个数num: "))

# 判断这个数是奇数还是偶数
if num %2 == 0:
    print("{num}是偶数".format(num=num))
else:
    print("{num}是奇数".format(num=num))


# 打印
