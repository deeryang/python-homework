#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:48:07 2019

@author: yang
"""

amount = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))

print(format("Interest Rate", "20s"), format("Monthly Payment", "20s"), format("Total Payment", "20s"))
rate = 0.05
totalPayment = 0
while rate - 0.08 < 0.00001:
    monthlyRate = rate / 12
    monthlyPayment = amount * monthlyRate / (1 - 1 / (1 + monthlyRate) ** (years * 12))
    totalPayment = monthlyPayment * years * 12
    print(format(rate, ".3%"), format(monthlyPayment, "20.2f"), format(totalPayment, "20.2f"))
    rate += 1 / 800