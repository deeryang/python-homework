#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:49:47 2019

@author: yang
"""

import turtle

turtle.speed(10)
turtle.color("black")

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            turtle.begin_fill()
        turtle.penup()
        x = 50 * i - 200
        y = 50 * j - 200
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        if (i % 50 + j % 50) % 2 == 0:
            turtle.end_fill()

turtle.hideturtle()
turtle.done()