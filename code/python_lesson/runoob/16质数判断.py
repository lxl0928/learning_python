#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 16.py
# Author: Timilong

# 用户输入一个数
num = int(input("请输入一个数num: "))

# 小于等于1，不是质数,质数又叫素数
if num <= 1:
    print("{0}不是素数".format(num))


# 质数智能被1和本身整除
for i in range(2, num):
    if num%i == 0:# 判断是否是质数
        print("{num}不是质数".format(num=num))# 不是，给出一个例子
        print("例如: ")
        print("{0} * {1} = {2}".format(i, num//i, num))
        break;
    if i>= num/2:
        print("{0}是素数".format(num))# 是，直接打印


