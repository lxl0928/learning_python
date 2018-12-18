#! /usr/bin/env python
# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function will bre3ak up words for us."""
    words = stuff.split(' ') #按照空格将句子划分成单词组成的列表
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) #将单词排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)#返回第一个单词
    print word

def print_last_word(words):
    word = words.pop(-1)#返回最后一个单词
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted woeds."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


