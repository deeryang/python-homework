#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:52:48 2019

@author: yang
"""

def count(s, ch):
    count = 0
    for i in range(len(s)):
        if ch == s[i]:
            count += 1
            
    return count
    
def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ").strip()
    n = count(s, ch)
    print("Character " + "'" + ch + "' appears", n, "time(s) in string '" + s + "'")
    
main()