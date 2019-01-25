#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:47:53 2019

@author: yang
"""

def isValid(passwd):
    length = len(passwd)
    alnum = passwd.isalnum()
    digitNum = 0
    for i in range(length):
        if passwd[i].isdigit():
            digitNum += 1
    
    if length >= 8 and alnum and digitNum >= 2:
        return True
    else:
        return False
    
def main():
    passwd = input("Enter the password: ").strip()
    if isValid(passwd):
        print("valid password")
    else:
        print("invalid password")
        
main()