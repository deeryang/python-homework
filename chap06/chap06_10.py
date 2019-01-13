#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:44:03 2019

@author: yang
"""

# check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    
    return True

def main():
    counter = 0
    for i in range(2, 10000):
        if isPrime(i):
            counter += 1
    print("The counters of prime number between 1 ~ 10000 is", counter)
    
main()