#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:57:37 2019

@author: yang
"""

import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = eval(input("What is " + str(num1) + " * " + str(num2) + "? "))

if num1 * num2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", num1, "*", num2, "is", num1 * num2)