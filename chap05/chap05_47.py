#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:03:27 2019

@author: yang
"""

import turtle
import random

turtle.penup()
turtle.goto(-60, -50)
turtle.pendown()
turtle.goto(60, -50)
turtle.goto(60, 50)
turtle.goto(-60, 50)
turtle.goto(-60, -50)

turtle.penup()

for _ in range(10):
    x = random.randint(-55, 55)
    y = random.randint(-45, 45)
    turtle.goto(x, y)
    turtle.dot(5, "red")

turtle.hideturtle()
turtle.done()