#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:21:55 2019

@author: yang
"""

from math import sqrt

class QuadraticEquation:
    
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getDescriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def getRoot1(self):
        d = self.getDescriminant()
        if d >= 0:
            return (-self.__b + sqrt(d)) / (2 * self.__a)
        else:
            return 0
        
    def getRoot2(self):
        d = self.getDescriminant()
        if d >= 0:
            return (-self.__b - sqrt(d)) / (2 * self.__a)
        else:
            return 0
        
def main():
    a, b, c = eval(input("Enter the value of a, b, and c: "))
    q = QuadraticEquation(a, b, c)
    if q.getDescriminant() < 0:
        print("The equation has no root")
    elif q.getDescriminant() == 0:
        print("The equation has two same roots, and root =", q.getRoot1())
    else:
        print("Root1 =", q.getRoot1(), ", Root2 =", q.getRoot2())
        
main()
    