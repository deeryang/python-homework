#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:14:45 2019

@author: yang
"""

import turtle

x1, y1 = eval(input("Enter the coordinate of point1:"))
x2, y2 = eval(input("Enter the coordinate of point2:"))

turtle.penup()
turtle.goto(x1, y1)
s1 = "(" + str(x1) + "," + str(y1) + ")"
turtle.write(s1)
turtle.pendown()
turtle.goto(x2, y2)
s2 = "(" + str(x2) + "," + str(y2) + ")"
turtle.write(s2)

turtle.hideturtle()

turtle.done()