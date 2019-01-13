#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:51:31 2019

@author: yang
"""

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * (1 + monthlyInterestRate) ** (12 * years)

def main():
    investmentAmount = eval(input("The amount invested: "))
    annualInterestRate = eval(input("Annual interest rate: "))
    monthlyInterestRate = annualInterestRate / 1200
    years = 30
    print(format("Years", "5s"), format("Future Value", ">12s"))
    for i in range(years):
        futureValue = futureInvestmentValue(investmentAmount, monthlyInterestRate, i + 1)
        print(format(i + 1, "<5d"), format(futureValue, ">10.2f"))
        
main()