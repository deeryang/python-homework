#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:51:16 2019

@author: yang
"""

from random import randint

# generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

def main():
    for i in range(100):
        ch = getRandomUpperCaseLetter()
        if (i + 1) % 10 != 0:
            print(ch, end = " ")
        else:
            print(ch)
            
main()