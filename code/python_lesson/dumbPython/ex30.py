#! /usr/bin/env python
# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15
if cars > people:
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars."

else:
    print "We can't decide"

if buses > cars:
    print "We should take the buses."

elif buses < cars:
    print "We should take the cars"

else:
    print "We still can't decide."

if people > buses:
    print "We should take buses"

else:
    print "Fine, let's stay home then..."

