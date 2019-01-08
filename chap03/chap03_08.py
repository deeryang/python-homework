#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:35:11 2019

@author: yang
"""

num = eval(input("Enter an amount:"))

numberOfYuan = num // 100
numberOfJiao = num % 100 // 10
numberOfFen = num % 10

print("The money is", numberOfYuan, "Yuan", numberOfJiao, "Jiao", numberOfFen, "Fen")