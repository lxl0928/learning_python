#! /usr/bin/python3 
# -*- coding: utf-8 -*-

import datetime
import random

# 生成十个带有时间戳的字符串

for i in range(0, 10):
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S"); # 生成当前时间
    print("当前时间{0}".format(str(nowTime)))

    randomNum = random.randint(0, 1000) # 生成随机数0<=randomNum<=1000
    if randomNum < 10: 
        randomNum = str(00) + str(randomNum)
    if randomNum < 100 and randomNum >= 10:
        randomNum = str(0) + str(randomNum)

    uniqueNum = str(nowTime) + str('+') + str(randomNum)
    print(uniqueNum)
    print()
