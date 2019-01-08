#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:51:08 2019

@author: yang
"""

import random

number = random.randint(0, 1)
answer = eval(input("Guess 0 or 1:"))

print("The number is", number, "\nYour answer is", answer == number)