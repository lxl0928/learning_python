#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Filename: 07计算三角形面积.py
# Author: Timilong

# 用户输入三角形三边
a = float(input("请输入边长a: "))
b = float(input("请输入边长b: "))
c = float(input("请输入边长c: "))

# 计算半周长
s = (a + b + c)/2

# 计算面积
area = (s * (s-a)*(s-b)*(s-c)) ** 0.5

print("边长为{a}, {b}, {c}的三角形面积为%.2f".format(a=a, b=b, c=c) % area.real)
