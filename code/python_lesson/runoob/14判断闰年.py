#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# 输入一个年份
year = int(input("请输入一个年份year: "))

# 按照闰年判断方法来判断

if year%400 == 0:
    print("{year}是闰年.".format(year=year))

elif year%4 == 0 and year%100 != 0:
    print("{year}是闰年".format(year=year))

else:
    print("{year}不是闰年.".format(year=year))


# 打印结果
