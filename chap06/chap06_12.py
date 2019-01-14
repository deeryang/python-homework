#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:02:01 2019

@author: yang
"""

def printChars(ch1, ch2, numberPerLine):
    number = ord(ch2) - ord(ch1) + 1
    for i in range(number):
        if (i + 1) % numberPerLine != 0:
            print(chr(ord(ch1) + i), end = " ")
        else:
            print(chr(ord(ch1) + i))
            
def main():
    ch1 = input("Enter the first char: ")
    ch2 = input("Enter the second char: ")
    numberPerLine = eval(input("Enter the number per line: "))
    printChars(ch1, ch2, numberPerLine)
    
main()