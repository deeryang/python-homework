#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:53:16 2019

@author: yang
"""

import turtle
from random import randint

# generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# generate a random uppercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

def drawLetter():
    counter = 0
    turtle.penup()
    for y in range(60, -100, -20):
        for x in range(-150, 150, 20):
            turtle.goto(x, y)
            ch = getRandomLowerCaseLetter()
            turtle.write(ch)
            counter += 1
            if counter > 100:
                return
def main():
    drawLetter()
    turtle.hideturtle()
    turtle.done()
    
main()