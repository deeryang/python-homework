#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:04:00 2019

@author: yang
"""

import turtle
import math

turtle.speed(10)
turtle.penup()
x = -175
turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    
turtle.penup()
turtle.goto(-100, -15)
turtle.write("-2\u03c0")
turtle.goto(100, -15)
turtle.write("2\u03c0")

turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.goto(190, -6)
turtle.goto(200, 0)
turtle.goto(190, 6)

turtle.penup()
turtle.goto(0, -70)
turtle.pendown()
turtle.goto(0, 70)
turtle.goto(6, 60)
turtle.goto(0, 70)
turtle.goto(-6, 60)

turtle.hideturtle()
turtle.done()