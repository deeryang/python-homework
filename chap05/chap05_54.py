#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:45:12 2019

@author: yang
"""

import turtle

turtle.penup()
turtle.goto(-150, (150 / 10) ** 2)
turtle.pendown()
for x in range(-150, 151):
    turtle.goto(x, (x / 10) ** 2)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.goto(190, -6)
turtle.goto(200, 0)
turtle.goto(190, 6)

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.goto(0, 150)
turtle.goto(6, 140)
turtle.goto(0, 150)
turtle.goto(-6, 140)

turtle.hideturtle()
turtle.done()