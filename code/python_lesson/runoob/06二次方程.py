#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Filename: 06二次方程.py
# author: Timilong

# 二次方程式: ax**2 + bx + c =  0
# a, b, c由用户提供

# 导入cmath模块
import cmath

a = float(input("请输入a: "))
b = float(input("请输入b: "))
c = float(input("请输入c: "))

# 计算

d = (b**2) - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("{a}, {b}, {c}为参数满足二次方程的两个解为{sol1}, {sol2}".format(a=a, b=b, c=c, sol1=sol1.real, sol2=sol2.real))
