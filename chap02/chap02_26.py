#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:13:55 2019

@author: yang
"""

import turtle
import math

x, y = eval(input("Enter the center of the circle:"))
r = eval(input("Enter the radius of the circle:"))

area = r * r * math.pi

turtle.penup()
turtle.goto(x, y - r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(x, y)
turtle.write(area)
turtle.hideturtle()

turtle.done()