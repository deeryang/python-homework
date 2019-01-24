#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:34:55 2019

@author: yang
"""

class Stock:
    
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
        
    def getName(self):
        return self.__name
    
    def getSymbol(self):
        return self.__symbol
    
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price
        
    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setCurrentPrice(self, price):
        self.__currentPrice = price
        
    def getChangePercent(self):
        change = (self.__previousClosingPrice - self.__currentPrice) / self.__previousClosingPrice
        return round(abs(change) * 100) / 100
    
def main():
    s = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print("The change percent is", s.getChangePercent())
    
main()