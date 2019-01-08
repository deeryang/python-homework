#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 23:05:41 2019

@author: yang
"""

import turtle
import math

x1, y1 = eval(input("Enter the coordinate of point1:"))
x2, y2 = eval(input("Enter the coordinate of point2:"))
x3, y3 = eval(input("Enter the coordinate of point3:"))

a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))

turtle.penup()
turtle.goto(x1, y1)
s1 = "p1(" + str(round(A, 2)) + ")"
turtle.write(s1)
turtle.pendown()
turtle.goto(x2, y2)
s2 = "p2(" + str(round(B, 2)) + ")"
turtle.write(s2)
turtle.goto(x3, y3)
s3 = "p3(" + str(round(C, 2)) + ")"
turtle.write(s3)
turtle.goto(x1, y1)

turtle.hideturtle()

turtle.done()