#! /usr/bin/env python
# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "The count is %d" % number

for fruit in fruits:
    print "The fruit is %s" % fruit

for i in change:
    print "I got the change: %r" % i

elements = []

for i in range(0, 6):
    print "Adding %d to the list elements" % i
    elements.append(i)

for i in elements:
    print "Element was: %d" % i


