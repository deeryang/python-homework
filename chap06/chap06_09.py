#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:37:23 2019

@author: yang
"""

# converts from feet to meters
def footToMeter(foot):
    return 0.305 * foot

# converts from meters to feet
def meterToFoot(meter):
    return meter / 0.305

def main():
    print(format("Feet", ">8s"), format("Meters", ">8s"), format("Meters", ">8s"), format("Feet", ">8s"))
    for i in range(10):
        feet = 1.0 + i
        meters = 20.0 + 5 * i
        print(format(feet, ">8.1f"), format(footToMeter(feet), ">8.3f"), 
              format(meters, ">8.1f"), format(meterToFoot(meters), ">8.3f"))
        
main()