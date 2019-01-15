#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:23:35 2019

@author: yang
"""

def convertMillis(millis):
    totalSeconds = millis // 1000
    leftSecond = totalSeconds % 60
    totalMinutes = totalSeconds // 60
    leftMinute = totalMinutes % 60
    totalHours = totalMinutes // 60
    
    print(totalHours, ":", leftMinute, ":", leftSecond)

def main():
    millis = eval(input("Enter the millis: "))
    convertMillis(millis)
    
main()