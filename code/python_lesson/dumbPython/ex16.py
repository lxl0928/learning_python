#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r. " % filename
print "If you don't want that, please hit CTRL+C(^C)"
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

print "Truncating the file. GoodBye!"
target.truncate()
# target.truncate()是截断文件大小[size]参数size可选，表示截断文件的大小是多少
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
