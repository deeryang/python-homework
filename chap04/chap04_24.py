#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:35:35 2019

@author: yang
"""

import random

number = random.randint(1, 52)

print("The card you picked is", end = " ")

if number % 13 == 1:
    print("Ace of", end = " ")
elif number % 13 == 11:
    print("Jack of", end = " ")
elif number % 13 == 12:
    print("Queen of", end = " ")
elif number % 13 == 13:
    print("King of", end = " ")
else:
    print(number % 13, "of", end = " ")
    
if number // 13 == 0:
    print("Clubs")
elif number // 13 == 1:
    print("Diamonds")
elif number // 13 == 2:
    print("Hearts")
else:
    print("Spades")