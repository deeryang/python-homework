#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:49:37 2019

@author: yang
"""

# return true if the card number is valid
def isValid(number):
    if getSize(number) >= 13 and getSize(number) <= 16:
        if (prefixMatched(number, 4) or prefixMatched(number, 5) 
        or prefixMatched(number, 6) or prefixMatched(number, 37)):
            if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
                return True
    return False

# get the result from step 2
def sumOfDoubleEvenPlace(number):
    total = 0
    s = str(number)
    for i in range(len(s)):
        data = int(s[i])
        total += getDigit(data)
        
    return total

# return this number if it is a single digit, otherwise,
#  return the sum of the two digits
def getDigit(number):
    if number // 10 == 0:
        return number
    else:
#        return int(str(number)[0]) + int(str(number)[1])
        return number - 9
    
# return sum of odd place digits in number
def sumOfOddPlace(number):
    s = str(number)
    total = 0
    for i in range(0, len(s), 2):
        total += int(s[i])
        
    return total

# return true if the digit d is a prefix for number
def prefixMatched(number, d):
    
    return getPrefix(number, getSize(d)) == d

# return the number of digits in d
def getSize(d):
    
    return len(str(d))

# return the first k number of digits from number. If the
#  number of digits in number is less than k, return number
def getPrefix(number, k):
    if len(str(number)) < k:
        return number
    else:
        for i in range(getSize(number) - k):
            number = number // 10
        return number
    
# test example
def main():
    number = eval(input("Enter the card number: "))
    if isValid(number):
        print("The card number is valid")
    else:
        print("The card number is not valid")
        
main()
    