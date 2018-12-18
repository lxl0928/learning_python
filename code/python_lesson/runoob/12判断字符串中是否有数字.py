#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.02
# Filename: 12.py
# Author: Timilong

# 判断函数
def is_number(s):
    try:
        float(s) # 将字符串转化为数字
        return True;
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s) # 针对unicode对象判断字符串是否由数字组成
        return True
    except ValueError:
        pass

    return False


while True:
    in_str = input("请输入一个字符串: ")
    if is_number(in_str):
        print("字符串{str1}由数字组成".format(str1=in_str))
    else:
        print("您输入的字符串不是数字")




