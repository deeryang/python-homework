#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:20:39 2019

@author: yang
"""

import turtle
import math

x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: \n"))
x2, y2, r2 = eval(input("Enter circle1's center x-, y-coordinates, and radius: \n"))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d <= abs(r1 - r2):
    if r1 > r2:
        s = "circle2 is inside circle1"
    else:
        s = "circle1 is inside circle2"
elif d <= r1 + r2:
    s = "circle2 overlaps circle1"
else:
    s = "circle2 does not overlap circle1"

#draw circle1
turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)

#draw circle2
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)

turtle.penup()
turtle.goto(x1 - 60, y1 - 20)
turtle.write(s)

turtle.hideturtle()
turtle.done()