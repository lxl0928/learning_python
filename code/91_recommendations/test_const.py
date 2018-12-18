#! /usr/bin/env python2
# -*- coding: utf-8 -*-

"""测试自定义常量const.py模块
-----------------------
File name: test_const.py
Author: Timilong
Date: 2016.10.8 22:15
-----------------------
"""

import const
const.MY_CONSTANT = 1
const.MY_SECOND_CONSTANT = 2
const.MY_THIRD_CONSTANT = 'a'
const.MY_FORTH_CONSTANT = 'b'


print(const.MY_CONSTANT)
print(const.MY_SECOND_CONSTANT)
print(const.MY_THIRD_CONSTANT*2)
const.MY_CONSTANT = 22222
print(const.MY_CONSTANT)

