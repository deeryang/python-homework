#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:10:13 2019

@author: yang
"""

import turtle

turtle.penup()
for i in range(10):
    for j in range(10):
        if j <= i:
            x = -100 + 20 * j
            y = 100 - 20 * i
            turtle.goto(x, y)
            turtle.write(j + 1)
        
turtle.hideturtle()
turtle.done()