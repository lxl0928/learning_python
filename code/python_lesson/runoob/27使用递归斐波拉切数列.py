#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 27.py
# Author: Timilong

# 递归函数
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


# 获取用户输入
nterms = int(input("要输出几项: "))

# 检查输入的数字是否正确
if nterms <= 0:
    print("请输入正数!")
else:
    for i in range(nterms):
        print(recur_fibo(i))


