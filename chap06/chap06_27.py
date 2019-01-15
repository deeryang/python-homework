#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:25:53 2019

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

# return true if primeNumber2 - primeNumber1 = 2
def isDoublePrime(number):
    return isPrime(number) and isPrime(number + 2)

def main():
    for number in range(2, 999):
        if isDoublePrime(number):
            print("(%d, %d)" %(number, number + 2))
            
main()