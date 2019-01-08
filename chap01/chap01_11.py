#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:51:04 2019

@author: yang
"""

amount = 312032486
year1 = 365 * 24 * 3600
amount1 = amount + year1 // 7 - year1 // 13 + year1 // 45
year2 = year1 * 2
amount2 = amount + year2 // 7 - year2 // 13 + year2 // 45
year3 = year1 * 3
amount3 = amount + year3 // 7 - year3 // 13 + year3 // 45
year4 = year1 * 4
amount4 = amount + year4 // 7 - year4 // 13 + year4 // 45
year5 = year1 * 5
amount5 = amount + year5 // 7 - year5 // 13 + year5 // 45

print("The first year : ", amount1)
print("The second year : ", amount2)
print("The third year : ", amount3)
print("The fourth year : ", amount4)
print("The fifth year : ", amount5)