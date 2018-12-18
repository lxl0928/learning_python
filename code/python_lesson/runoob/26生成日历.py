#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.06
# Filename: 26.py
# Author: Timilong

# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))
