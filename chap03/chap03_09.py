#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:57:32 2019

@author: yang
"""

name = input("Enter employee's name:")
hours = eval(input("Enter number of hours worked in a week:"))
rate = eval(input("Enter hourly pay rate:"))
federalTax = eval(input("Enter federal tax withholding rate:"))
stateTax = eval(input("Enter state tax withholding rate:"))

print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $" + str(rate))
print("Gross Pay: $" + str(hours * rate))
print("Deductions:")
print("  Federal Withholding (" + str(format(federalTax, '.1%')) + "): $" + str(hours * rate * federalTax))
print("  State Withholding (" + str(format(stateTax, '.1%')) + "): $" + str(hours * rate * stateTax))
print("  Total deduction: $" + str(hours * rate * (federalTax + stateTax)))
print("Net Pay: $" + str(hours * rate * (1 - federalTax - stateTax)))