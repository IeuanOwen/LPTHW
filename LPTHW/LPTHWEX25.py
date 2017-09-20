#Learn Python the hard way EX25
# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """prints the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a  full sentance and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """" prints the first and last word"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """"Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


    

# Study Drills
# 1 ~ Go through each line of output when running in the shell and work out what is happening
# Done

# 2 ~ Try doing this: help(ex25) and also help(ex25.break_words). Notice how you get help for your module and how the help is those odd '"""' strings you put after each function in ex25?
# ~ Those special strings are called documentation comments and we’ll be seeing more of them.
# Skipped

# 3 ~ you can use from ex25 import * to instead of typing LPTHWEX25.print_first_word. all of your functions will have been imported.
# Done

# 4 ~ break the file an look at results
# Skipped