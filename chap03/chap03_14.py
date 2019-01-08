#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:29:06 2019

@author: yang
"""

import turtle

r = eval(input("Enter the radius of the circle:"))

turtle.pensize(3)
turtle.speed(5)

turtle.penup()
turtle.goto(-2.2 * r, -r)
turtle.pendown()
turtle.color("blue")
turtle.circle(r)

turtle.penup()
turtle.goto(0, -r)
turtle.pendown()
turtle.color("black")
turtle.circle(r)

turtle.penup()
turtle.goto(2.2 * r, -r)
turtle.pendown()
turtle.color("red")
turtle.circle(r)

turtle.penup()
turtle.goto(-1.1 * r, -2.3 * r)
turtle.pendown()
turtle.color("yellow")
turtle.circle(r)

turtle.penup()
turtle.goto(1.1 * r, -2.3 * r)
turtle.pendown()
turtle.color("green")
turtle.circle(r)

turtle.hideturtle()

turtle.done()