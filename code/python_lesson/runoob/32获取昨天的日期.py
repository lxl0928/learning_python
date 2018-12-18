#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.07
# Filename: 32.py
# Author: Timilong

# 引入datetime模块
import datetime

# 定义函数
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
print(getYesterday())
