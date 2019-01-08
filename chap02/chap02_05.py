#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:06:32 2019

@author: yang
"""

subTotal, rate = eval(input("Enter the subtotal and a gratuity rate:"))
gratuity = subTotal * rate / 100
total = subTotal + gratuity
print("The gratuity is", gratuity, "and the total is", total)