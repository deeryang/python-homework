#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:48:15 2019

@author: yang
"""

import turtle

x, y = eval(input("Enter the x- and y-coordinates of the point:"))

turtle.penup()
turtle.goto(-50, -25)
turtle.pendown()
turtle.goto(50, -25)
turtle.goto(50, 25)
turtle.goto(-50, 25)
turtle.goto(-50, -25)

turtle.penup()
turtle.goto(x, y)
turtle.dot(5, "black")

turtle.goto(-70, -50)
if x >= -50 and x <= 50 and y > -25 and y < 25:
    s = "The point is inside the rectangle"
else:
    s = "The point is not in the ractangle"
turtle.write(s)

turtle.hideturtle()

turtle.done()