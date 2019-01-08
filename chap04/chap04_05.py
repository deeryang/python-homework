#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:10:41 2019

@author: yang
"""

nowDay = eval(input("Enter today's day:"))
elapsedDay = eval(input("Enter the number of days elapsed since today:"))

print("Today is ", end = "")
if nowDay == 0:
    print("Sunday", end = "")
elif nowDay == 1:
    print("Monday", end = "")
elif nowDay == 2:
    print("Tuesday", end = "")
elif nowDay == 3:
    print("Wednesday", end = "")
elif nowDay == 4:
    print("Thursday", end = "")
elif nowDay == 5:
    print("Friday", end = "")
elif nowDay == 6:
    print("Saturday", end = "")
else:
    print("error")
    
futureDay = (nowDay + elapsedDay) % 7
print(" and the future day is ",  end = "")
if futureDay == 0:
    print("Sunday", end = "")
elif futureDay == 1:
    print("Monday", end = "")
elif futureDay == 2:
    print("Tuesday", end = "")
elif futureDay == 3:
    print("Wednesday", end = "")
elif futureDay == 4:
    print("Thursday", end = "")
elif futureDay == 5:
    print("Friday", end = "")
elif futureDay == 6:
    print("Saturday", end = "")
else:
    print("error")