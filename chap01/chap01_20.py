#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:32:24 2019

@author: yang
"""

import turtle

a = 100

turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)

turtle.penup()
turtle.goto(-a/2, -a/2)
turtle.pendown()

turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)

turtle.goto(0, 0)

turtle.penup()
turtle.goto(-a/2, a/2)
turtle.pendown()
turtle.goto(0, a)

turtle.penup()
turtle.goto(a/2, -a/2)
turtle.pendown()
turtle.goto(a, 0)

turtle.penup()
turtle.goto(a/2, a/2)
turtle.pendown()
turtle.goto(a, a)

turtle.hideturtle()
turtle.done()