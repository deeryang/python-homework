#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:05:16 2019

@author: yang
"""

from Loan import Loan

def main():
    # Enter yearly interest rate
    annualInterestRate = eval(input("Enter yearly interest rate, for example, 7.25: "))

    # Enter number of years
    numberOfYears = eval(input("Enter number of years as an integer: "))

    # Enter loan amount
    loanAmount = eval(input("Enter loan amount, for example, 120000.95: "))

    # Enter a borrower
    borrower = input("Enter a borrower's name: ")

    # Create a Loan object
    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    # Display loan date, monthly payment, and total payment
    print("The load is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan.getTotalPayment(), ".2f"))

main()  # Call the main function