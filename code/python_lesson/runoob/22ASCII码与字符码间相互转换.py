#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 22.py
# Author: Timilong

# 获取用户输入的字符
character = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转化为整型
number = int(input("请输入一个ASCII码: "))

# 打印转换结果
print(character, "转化为ASCII码: ", ord(character))

print(number, "转为为char为: ", chr(number))
