#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:29:24 2019

@author: yang
"""

amount = eval(input("Enter the amount of water in kilograms:"))
initialTem = eval(input("Enter the initial temperature:"))
finalTem = eval(input("Enter the final temperature:"))
energy = amount * (finalTem - initialTem) * 4184

print("The energy needed is", energy)