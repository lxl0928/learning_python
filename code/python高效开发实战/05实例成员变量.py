#! /usr/bin/env python3
# coding: utf-8

class MyClass(object):
    message = "Hello, Developer!"

    def show(self):
        print(self.message)
        print("Here is {0} in {1}".format(self.name, self.color))

    def __init__(self, name="unset", color="black"):
        print("Constructor && __init__ is called with params: {0}, {1}".format(name, color))
        self.name = name
        self.color = color

    def __del__(self):
        print("Destructor is called for {0}".format(self.name))

inst0 = MyClass("David")
inst0.show()
print("Color of inst0 is: {0}.".format(inst0.color))
print("\n--------------------\n")

inst1 = MyClass("Lisa", "Yellow")
inst1.show()
print("Name of inst1 is: {0}.".format(inst1.name))

print("\n--------------------\n")
del inst0, inst1



