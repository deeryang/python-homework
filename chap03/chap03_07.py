#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:31:33 2019

@author: yang
"""

import time

currentTime = time.time()
currentTime = int(currentTime) % 26
print("Get the random char:", chr(currentTime + 65))