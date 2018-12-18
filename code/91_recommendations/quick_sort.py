#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

# filename: quick_sort.py
# author: Timilong

def quicksort(array):
    less = []
    greater = []
    print("1: ", "array: ", array, "len(array): ", len(array))
    if len(array) <= 1:
        print("2: ", "array: ", array, "len(array): ", len(array))
        return array

    pivot = array.pop()
    print("3: ", "array: ", array, "len(array): ", len(array), "pivot: ", pivot)

    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    current_array = quicksort(less) + [pivot] + quicksort(grater)
    print("4: ", "array: ", array, "len(array): ", len(array), "pivot: ", pivot, "current_array:", current_array)
    return current_array

array = [1, 4, 3, 0]
print(quicksort(array))

