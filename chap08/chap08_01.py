#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:03:25 2019

@author: yang
"""

def isValid(s):
    s = s.strip().split()
    s = list(s)
    if len(s) == 3:
        if (len(s[0]) == 3 and len(s[1]) == 2 and len(s[2]) == 4 and s[0].isdigit() 
        and s[1].isdigit() and s[1].isdigit()):
            return True
        else:
            return False
    else:
        return False
    
def main():
    s = input("Enter SSN: ").strip()
    if isValid(s):
        print("Valid SSN")
    else:
        print("Invalid SSN")
        
main()