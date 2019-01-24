#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:15:32 2019

@author: yang
"""

# List 6-12
import RandomCharacter

NUMBER_OF_CHARS = 175   # Number of characters to generate
CHARS_PER_LNIE = 25     # Number of characters to display per line

# Print random characters between 'a' and 'z', 25 chars per line
for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandomLowerCaseLetter(), end = " ")
    if (i + 1) % CHARS_PER_LNIE == 0:
        print() # Jump to the new line
        