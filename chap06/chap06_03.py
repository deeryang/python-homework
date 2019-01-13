#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:33:07 2019

@author: yang
"""

# return the reversal of an integer
def reverse(number):
    res = number % 10
    number = number // 10
    while number:
        res = res * 10 + number % 10
        number = number // 10
        
    return res

# return true if number is a palindrome
def isPalindrome(number):
    return number == reverse(number)

def main():
    number = eval(input("Enter an integer: "))
    if isPalindrome(number):
        print(number, "is a palindrome")
    else:
        print(number, "is not a palindromne")
        
main()