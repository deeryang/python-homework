#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:45:13 2019

@author: yang
"""

from random import randint

# generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# count the 'A' times in 10000 uppercase letter
def main():
    counter = 0
    for i in range(10000):
        ch = getRandomUpperCaseLetter()
        if ch == 'A':
            counter += 1
    print("The times of 'A' is", counter)
    
main()