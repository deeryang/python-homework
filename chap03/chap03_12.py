#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:17:47 2019

@author: yang
"""

import turtle

side = eval(input("Enter the side:"))

turtle.right(72)
turtle.forward(side)
for i in range(4):
    turtle.right(144)
    turtle.forward(side)

turtle.hideturtle()
    
turtle.done()