# !/usr/bin/python
# -*- coding: utf-8 -*-

def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)

    return fn

@log
def factorial(n):
    return reduce(lambda x, y : x*y, range(1, n+1))
print factorial(10)


