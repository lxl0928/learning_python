#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
script, filename = argv

txt = open(filename)

print "The file name is %r" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
