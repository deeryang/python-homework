#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:59:05 2019

@author: yang
"""

import turtle

turtle.speed(8)
for i in range(10):
    x = 0
    y = -100 - 10 * i
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(abs(y))
    
turtle.hideturtle()
turtle.done()