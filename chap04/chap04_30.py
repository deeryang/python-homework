#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:02:53 2019

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

if currentHour <= 12:
    print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "AM")
else:
    print("Current time is", currentHour - 12, ":", currentMinute, ":", currentSecond, "PM")

