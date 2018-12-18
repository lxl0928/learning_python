#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 09.py
# Author: Timilong

# 用户输入摄氏温度
celsius = float(input("请输入摄氏温度: "))


# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32

# 打印华氏温度
print("%0.1f摄氏温度转化为华氏温度为%0.1f" % (celsius, fahrenheit))



