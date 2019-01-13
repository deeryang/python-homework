#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:29:19 2019

@author: yang
"""

# converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

# converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def main():
    print(format("Celsius", "<10s"), format("Fahrenheit", "<10s"), format("Fahrenheit", "<10s"), format("Celsius", "<10s"))
    for i in range(10):
        celsius = 40.0 - i
        fahrenheit = 120.0 - 10 * i
        print(format(celsius, "<10.1f"), format(celsiusToFahrenheit(celsius), "<10.1f"), 
              format(fahrenheit, "<10.1f"), format(fahrenheitToCelsius(fahrenheit), "<10.2f"))
        
main()