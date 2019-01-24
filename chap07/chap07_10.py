#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:46:45 2019

@author: yang
"""

import time

class Time:
    
    def __init__(self):
        self.setTime(int(time.time()))
        
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setTime(self, elapseTime):
        self.__hour = elapseTime // 3600 % 24
        self.__minute = elapseTime // 60 % 60
        self.__second = elapseTime % 60
        
def main():
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))
    elapseTime = eval(input("Enter the elapse time: "))
    currentTime.setTime(elapseTime)
    print("The hour:minute:second for elapse time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + str(currentTime.getSecond()))
    
main()