#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:48:53 2019

@author: yang
"""

import turtle

r = 50

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.right(60)
turtle.circle(r, steps = 3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(0)
turtle.right(45)
turtle.circle(r, steps = 4)
turtle.end_fill()

turtle.penup()
turtle.goto(-0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(0)
turtle.right(36)
turtle.circle(r, steps = 5)
turtle.end_fill()

turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(0)
turtle.right(30)
turtle.circle(r, steps = 6)
turtle.end_fill()

turtle.penup()
turtle.goto(230, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(0)
turtle.right(22.5)
turtle.circle(r, steps = 8)
turtle.end_fill()

turtle.hideturtle()

turtle.done()