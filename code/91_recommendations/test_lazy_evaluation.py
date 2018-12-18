#! /usr/bin/env python2
# -*- coding: utf-8 -*-

from time import time
t = time()
abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']
for i in xrange(100000):
    for w in ('Mr.', 'is', 'Hat', 'chasing', 'the', 'black', 'cat', '.'):
        if w in abbreviations:
        #if w[-1] == '.' and w in abbreviations:
            pass

print "total run time: "
print time()-t


print("---------------------")

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
from itertools import islice
print list(islice(fib(), 5))
