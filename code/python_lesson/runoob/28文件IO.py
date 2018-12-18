#！ /usr/bin/python3 
# -*- coding: utf-8 -*-

# Date: 2016.08.06
# Filename: 28.py
# Author: Timilong

with open("test.txt", 'wt') as out_file:
    out_file.write("该文本会写入到文本中\n")

# 读文件
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)
