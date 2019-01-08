#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:55:40 2019

@author: yang
"""

import turtle

x1, y1 = eval(input("Enter the coordinate of point1:"))
x2, y2 = eval(input("Enter the coordinate of point2:"))
x3, y3 = eval(input("Enter the coordinate of point3:"))

area = 1 / 2 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)

turtle.penup()
turtle.goto(x1, y1)
s1 = "p1(" + str(x1) + "," + str(y1) + ")"
turtle.write(s1)
turtle.pendown()
turtle.goto(x2, y2)
s2 = "p2(" + str(x2) + "," + str(y2) + ")"
turtle.write(s2)
turtle.goto(x3, y3)
s2 = "p3(" + str(x3) + "," + str(y3) + ")"
turtle.goto(x1, y1)

x = min(x1, x2, x3)
y = min(y1, y2, y3)

turtle.penup()
turtle.goto(x - 50, y - 50)
s = "The area of the triangle is " + str(area)
turtle.write(s)

turtle.hideturtle()
turtle.done()