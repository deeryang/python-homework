#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 18:52:27 2019

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

# return true if number is a mersenne prime number
def isMersennePrime(number):
    return isPrime(number) and isPrime(2 ** number - 1)

def main():
    print(format("p", ">3s"), format("2^p - 1", ">6s"))
    for number in range(2, 32):
        if isMersennePrime(number):
            print(format(number, "3d"), format(2 ** number - 1, "6d"))
            
main()

# =============================================================================
# result:
#     
#   p 2^p - 1
#   2      3
#   3      7
#   5     31
#   7    127
#  13   8191
#  17 131071
#  19 524287
#  31 2147483647
# =============================================================================
