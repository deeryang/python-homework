#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:42:39 2019

@author: yang
"""

import time

class StopWatch:
    
    def __init__(self, startTime = time.time()):
        self.__startTime = startTime
        
    def getStartTime(self):
        return self.__startTime
    
    def getEndTime(self):
        return self.__endTime
    
    def start(self):
        self.__startTime = time.time()
        
    def stop(self):
        self.__endTime = time.time()
        
    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))
    
def main():
    startTime = time.time()
    s = StopWatch(startTime)
    s.start()
    count = 0
    while count < 1000000:
        count += 1
    s.stop()
    print("The cost time is", s.getElapsedTime(), "milliseconds")
    
main()