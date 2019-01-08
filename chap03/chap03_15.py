#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:36:49 2019

@author: yang
"""

import turtle

turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)

turtle.penup()
turtle.goto(-50, -45)
turtle.pendown()
turtle.goto(0, -70)
turtle.goto(50, -45)

turtle.penup()
turtle.goto(-42, 25)
turtle.dot(15, "black")
turtle.goto(42, 25)
turtle.dot(15, "black")

turtle.goto(0, -100)
turtle.setheading(0)
turtle.pensize(2)
turtle.pendown()
turtle.circle(90)

turtle.hideturtle()

turtle.done()
