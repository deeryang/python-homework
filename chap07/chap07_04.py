#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:56:20 2019

@author: yang
"""

SLOW = 1
MEDIUM = 2
FAST = 3
    
class Fan:
       
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        
    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, speed):
        self.__speed = speed
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
        
    def isOn(self):
        return self.__on
    
    def turnOn(self):
        self.__on = True
        
    def turnOff(self):
        self.__on = False
    
def displayProperties(fan):
    print("speed", fan.getSpeed(), "\n", "color", fan.getColor(), "\n", 
        "radius", fan.getRadius(), "\n", "fan is on" if fan.isOn() else "fan is off")
    
def main():
    f1 = Fan()
    f1.setSpeed(FAST)
    f1.setRadius(10)
    f1.setColor("yellow")
    f1.turnOn()
    displayProperties(f1)
    
    f2 = Fan()
    f2.setSpeed(MEDIUM)
    f2.setRadius(5)
    f2.setColor("blue")
    f2.turnOff()
    displayProperties(f2)
    
main()
    
    