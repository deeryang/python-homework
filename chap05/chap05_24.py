#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:44:47 2019

@author: yang
"""

loanAmount = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))
annualRate = eval(input("Annual Interest Rate: "))

monthlyRate = annualRate / 1200
balance = loanAmount
monthlyPayment = loanAmount * monthlyRate / (1 - 1 / (1 + monthlyRate) ** (years * 12))
totalPayment = monthlyPayment * 12

print("Monthly Payment: " +  format(monthlyPayment, ".2f"))
print("Total Payment: " + format(totalPayment, ".2f"))
print()
print(format("Payment#", "10s"), format("Interest", "10s"), format("Principal", "10s"), format("Balance", "10s"))
for i in range(1, years * 12 + 1):
    interest = monthlyRate * balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(format(i, "<10d"), format(interest, "<10.2f"), format(principal, "<10.2f"), format(balance, "<10.2f"))
    