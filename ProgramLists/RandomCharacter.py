#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:49:36 2019

@author: yang
"""

# List 6-11
from random import randint # import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# Generate a random lowercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

# Generate a random uppercase letter
def GetRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')

# Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# Generate a random character
def getRandomASCIICharacter():
    return chr(randint(0, 127))