#! /usr/bin/python3 
# -*- conding: utf-8 -*-

# Date: 2016.08.07
# Filename:  25.py
# Author: Timilong

# 定义函数: 加减乘除
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# 控制台
print("*****简单计算器*****")
print("*     1. 加法      *")
print("*     2. 减法      *")
print("*     3. 乘法      *")
print("*     4. 除法      *")
print("********************")

print()

print("请输入您的选择1/2/3/4: ")
choice = int(input())
num1 = int(input("请输入第一个数num1: "))
num2 = int(input("请输入第二个数num2: "))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))

if choice == 2: 
    print(num1, '-', num2, '=', substract(num1, num2))

if choice == 3:
    print(num1, '*', num2, '=', multiply(num1, num2))

if choice == 4:
    print(num1, '/', num2, '=', divide(num1, num2))


