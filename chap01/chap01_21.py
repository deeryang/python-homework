#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:42:29 2019

@author: yang
"""

import turtle

turtle.speed(8)
turtle.pensize(3)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.left(172.5)
turtle.forward(70)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(80, 0)

turtle.penup()
turtle.goto(90, -10)
turtle.write("3")
turtle.goto(-5, 80)
turtle.write("12")
turtle.goto(-90, -10)
turtle.write("9")
turtle.goto(-5, -100)
turtle.write("6")

turtle.goto(-10, -130)
turtle.write("9:15:00")

turtle.hideturtle()

turtle.done()