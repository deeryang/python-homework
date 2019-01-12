#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:02:44 2019

@author: yang
"""

import turtle

for i in range(19):
    turtle.penup()
    x = -180
    y = -180 + 20 * i
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(-x, y)
    
for i in range(19):
    turtle.penup()
    x = -180 + 20 * i
    y = -180
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, -y)
    
turtle.hideturtle()
turtle.done()