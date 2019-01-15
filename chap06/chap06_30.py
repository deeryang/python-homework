#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:02:20 2019

@author: yang
"""


import random

# return the sum of two number
def rollNumber():
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
#    print("You rolled %d + %d = %d" %(number1, number2, number1 + number2))
    
    return number1 + number2

# return true if win
def win():
    total = rollNumber()
    if total == 2 or total == 3 or total == 12:
        return False
#        print("You lose")
    elif total == 7 or total == 11:
        return True
#        print("You win")
    else:
        point = total
#        print("Point is", point)
        total = rollNumber()
        while total != 7 and total != point:
            total = rollNumber()
        if total == 7:
            return False
#            print("You lose")
        else:
            return True
#            print("You win")
            
def main():
    counter = 0
    for i in range(10000):
        if win():
            counter += 1
    print("For 10000 times you win", counter)
   
main()