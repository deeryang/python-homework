#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:09:23 2019

@author: yang
"""

# List 6-8
# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
    hex = " "
    
    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
        
    return hex

# Convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:   # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
    
def main():
    # Prompt the user to enter a decimal integer
    decimalValue = eval(input("Enter a decimal number: "))
    
    print("The hex number for decimal", decimalValue,
          "is", decimalToHex(decimalValue))
    
main()  # Call the main function