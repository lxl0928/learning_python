#! /usr/bin/python3 
# -*- coding: utf-8 -*-

my_input = int(input('利润:'))

array_benjing = [1000000, 600000, 400000, 200000, 100000, 0]
array_lilv = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0

for i in range(0, 6):
    if my_input > array_benjing[i]:
        r += (my_input-array_benjing[i]) * array_lilv[i]
        print(i, (my_input-array_benjing[i]) * array_lilv[i])
        my_input = array_benjing[i]
print(r)
        
