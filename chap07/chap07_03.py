#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:44:24 2019

@author: yang
"""

class Account:
    
    def __init__(self, ID = 0, balance = 100, annualInterestRate = 0):
        self.__ID = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getID(self):
        return self.__ID
    
    def setID(self, ID):
        self.__ID = ID
        
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance
        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12
    
    def getMonthlyInterest(self):
        return self.__balance * self.__annualInterestRate / 1200
    
    def withdraw(self, money):
        self.__balance -= money
        
    def deposit(self, money):
        self.__balance += money
        
def main():
    a = Account(1122, 20000, 4.5)
    a.withdraw(2500)
    a.deposit(3000)
    print("The id of the account is", a.getID())
    print("The balance is", a.getBalance())
    print("The monthly interest rate is", a.getMonthlyInterestRate(), "%")
    print("The monthly interest is", a.getMonthlyInterest())
    
main()