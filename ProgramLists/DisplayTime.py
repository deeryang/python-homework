#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:28:17 2019

@author: yang
"""

# Prompt the user for input
seconds = eval(input("Enter an integer for seconds: "))

# Get minutes and remaining seconds
minutes = seconds // 60     # Find minutes in seconds
remainingSeconds = seconds % 60     # Seconds remaining
print(seconds, "seconds is", minutes, "minutes and", remainingSeconds, "seconds")