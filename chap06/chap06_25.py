#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 18:46:20 2019

@author: yang
"""

# return true if number is a prime
def isPrime(number):
    division = 2
    while division <= number / 2:
        if number % division == 0:
            return False
        division += 1
    return True

# return the reversal of an integer
def reverse(number):
    res = number % 10
    number = number // 10
    while number:
        res = res * 10 + number % 10
        number = number // 10
        
    return res

# return true if number is not a palindrome
def isNotPalindrome(number):
    return number != reverse(number)

def main():
    counter = 0
    number = 2
    while counter < 100:
        if isNotPalindrome(number) and isPrime(number) and isPrime(reverse(number)):
            counter += 1
            if counter % 10 != 0:
                print(format(number, "5d"), end = " ")
            else:
                print(format(number, "5d"))
        number += 1

main()