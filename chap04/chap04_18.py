#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:09:02 2019

@author: yang
"""

rate = eval(input("Enter the exchange rate from dollars to RMB:"))
flag = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa:"))

if flag == 0:
    amount = eval(input("Enter the dollar amount:"))
    res = amount * rate
    print("$" + str(amount) + " is " + str(res) + " yuan")
elif flag == 1:
    amount = eval(input("Enter the RMB amount:"))
    res = amount / rate
    print(str(amount) + " yuan is $" + format(res, ".2f"))
else:
    print("Incorrect input")