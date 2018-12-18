#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 18.py
# Author: Timilong

# 双重循环格式化打印9*9乘法表
i = 1
while i<=9:
    j = 1
    while j<i+1:
        print("{0}*{1} = {2}    ".format(i, j, i*j), end='')
        j += 1;
    i += 1
    print()


