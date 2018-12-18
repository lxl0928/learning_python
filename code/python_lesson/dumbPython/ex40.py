#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print "the length of lurics is %d " % len(self.lyrics)
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Python看到了Song(), 知道它是我定义的一个类
# Python创建了一个空对象，里边包含了在该类中用def创建的所有函数。
# 然后Python回去检查是不是在类中创建了一个__init__函数，如果又创建，它就会调用这个函数，从而对新创建的空对象进行了初始化。
# 在Song的__init__函数里，有一个多余的函数叫做self，这就是Python创建的空对象。我们可以对它进行类似模块，字典等的操作，为它设置一次额变量进去。
# 在这里我们把self.lyrics = lyrics设置成了一段外部传入的实例化对象设定的值。
# 然后Python讲这个新创建的对象复制给一个叫做happy_bday和bulls-on_parade的变量.
