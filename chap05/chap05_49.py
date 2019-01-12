#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:46:36 2019

@author: yang
"""

import turtle

turtle.penup()
turtle.goto(-100, 150)
turtle.write("Multiplication Table")

for i in range(9):
    x = -100 + 20 * i
    y = 130
    turtle.goto(x, y)
    turtle.write(i + 1)

turtle.goto(-140, 120)
turtle.write("-" * 60)

for i in range(9):
    turtle.goto(-140, 100 - 20 * i)
    turtle.write(str(i + 1) +  "     |   ")
    for j in range(9):
        x = -100 + 20 * j
        y = 100 - 20 * i
        turtle.goto(x, y)
        turtle.write((i + 1) * (j + 1))

turtle.hideturtle()
turtle.done()