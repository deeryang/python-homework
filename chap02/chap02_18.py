#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:10:56 2019

@author: yang
"""

import time

offset = eval(input("Enter the time zone offset to GMT:"))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
totalHours = totalMinutes // 60
currentMinute = totalMinutes - totalHours * 60
currentHour = (totalHours + offset) % 24

print("Current time is", currentHour, ":", currentMinute, ":", currentSecond)

