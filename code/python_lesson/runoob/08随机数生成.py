#! /usr/bin/python3 
# -*- coding: utf-8 -*-

import random

# 生成五个不同的随机数
i = 1
arr = []

while i<=5:
    a = random.randint(1, 33)
    arr.append(a)
    i += 1;


arr1 = tuple(arr)

print(arr1)
print(type(arr1))
