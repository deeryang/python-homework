#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:49:38 2019

@author: yang
"""

import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)

answer = eval(input("What is " + str(a) + " + " + str(b) + " + " + str(c) + "? "))

print(a, "+", b, "+", c, "=", answer, "is", a + b + c == answer)