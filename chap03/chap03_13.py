#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:20:06 2019

@author: yang
"""

import turtle

turtle.right(30)
turtle.pensize(3)
turtle.begin_fill()
turtle.color("red")
turtle.circle(100, steps = 6)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 60)
turtle.color("white")
turtle.write("STOP", font = ("宋体", 40, "bold"))
turtle.hideturtle()

turtle.done()