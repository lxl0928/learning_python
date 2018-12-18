#! /usr/bin/python3 
# -*- coding: utf-8 -*-

# 用户输入两个数字
num1 = input("请输入第1个数字: ") # input输入的是字符串
num2 = input("请输入第2个数字: ")

# num1 与 num2 求和
sum = float(num1) + float(num2) # 通过float方法将字符串转化为数字

# 格式化输出
print("{num1} + {num2} = {sum}".format(num1=num1, num2=num2, sum = sum))

print("*****另外一种方法如下*****")

print("两数之和为: {0}".format(float(input("请输入第一个数: ")) + float(input("请输入第二个数: "))))

