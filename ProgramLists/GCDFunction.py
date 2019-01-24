#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:32:42 2019

@author: yang
"""

# List 6-5
# Return the gcd of two integers
def gcd(n1, n2):
    gcd = 1     # Initial gcd is 1
    k = 2       # Possible gcd
    
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k     # Update gcd
        k += 1
            
    return gcd  # Return gcd