#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:25:51 2019

@author: yang
"""

def find(s1, s2):
    if len(s1) > len(s2):
        return False
    else:
        start = 0
        while start < len(s2) - len(s1):
            if s2[start:start + len(s1)] == s1:
                return True
            start += 1
            
        return False
    
def main():
    s1 = input("Enter string 1: ").strip()
    s2 = input("Enter string 2: ").strip()
    if find(s1, s2):
        print("String 1 is a substring of string 2")
    else:
        print("String 1 is not a substring of string 2")
        
main()