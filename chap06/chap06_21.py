#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:03:52 2019

@author: yang
"""

# babylon function to get the sqrt
def sqrt(n):
    lastGuess = 1
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    while abs(lastGuess - nextGuess) > 0.00001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        
    return nextGuess

def main():
    num = eval(input("Enter a number: "))
    print("The sqrt of", num, "is", sqrt(num))
    
main()