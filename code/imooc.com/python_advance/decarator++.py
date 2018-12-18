#! /usr/bin/python
#-*- coding: utf-8 -*-

# 利用functool.wraps作用在返回的新函数上面，是的调用装饰器以后不该便原来的信息

import time, functools
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2-t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x, y : x*y, range(1, n+1))
print factorial.__name__
