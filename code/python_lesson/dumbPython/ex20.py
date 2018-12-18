#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(myfile):
    print myfile.read();

#每次运行seek(0)回到文件的开始
def rewind(myfile):
    myfile.seek(0)

def print_a_line(line_count, myfile):
    print line_count, myfile.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

