#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:10:39 2019

@author: yang
"""

import random

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

# Display result
print(number1, "+", number1, "=", answer, "is", number1 + number2 == answer)