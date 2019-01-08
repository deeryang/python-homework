#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:07:28 2019

@author: yang
"""

import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = eval(input("What's " + str(num1) + " + " + str(num2) + "? "))

print(num1, "+", num2, "=", answer, "is", num1 + num2 == answer)