#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# filename: with_example01.py

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

def get_sample():
    return Sample()

with get_sample() as sample:
    print("my_sample", sample)
