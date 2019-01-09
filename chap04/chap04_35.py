#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:41:11 2019

@author: yang
"""

import turtle

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2:\n"))

d = (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0)

turtle.penup()
turtle.goto(x0, y0)
turtle.write("p0(" + str(x0) + ", " + str(y0) + ")")
turtle.pendown()
turtle.goto(x1, y1)
turtle.write("p1(" + str(x1) + ", " + str(y1) + ")")

turtle.penup()
turtle.goto(x2, y2)
turtle.dot(10, "black")


if d > 0:
    s = "p2 is on the left side of the line from p0 to p1"
elif d == 0:
    s = "p2 is on the same line from p0 to p1"
else:
    s = "p2 is on the right side of the line from p0 to p1"
    
turtle.goto(x2 - 100, y2 - 30)
turtle.write(s)
turtle.hideturtle()

turtle.done()