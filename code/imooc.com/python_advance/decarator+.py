#! /usr/bin/python
#-*- coding: utf-8 -*-

def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()

