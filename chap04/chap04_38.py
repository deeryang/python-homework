#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:08:19 2019

@author: yang
"""

import turtle

x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: \n"))
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: \n"))

#judge the relations
if abs(x1 - x2) <= (w1 - w2) / 2 and abs(y1 - y2) <= (h1 - h2) / 2:
    s = "r2 is inside r1"
elif abs(x1 - x2) <= w1 / 2 or abs(y1 - y2) <= h1 / 2:
    s = "r2 overlaps r1"
else:
    s = "r2 does not overlap r1"

#draw the two rectangles
turtle.penup()
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)
turtle.pendown()
turtle.goto(x1 + w1 / 2, y1 - h1 / 2)
turtle.goto(x1 + w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)

turtle.penup()
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)
turtle.pendown()
turtle.goto(x2 + w2 / 2, y2 - h2 / 2)
turtle.goto(x2 + w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)

turtle.penup()
turtle.goto(x2 -w2 / 2 - 100, y2 + h2 / 2 + 50)
turtle.write(s)

turtle.hideturtle()
turtle.done()