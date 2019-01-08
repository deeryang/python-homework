#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:00:15 2019

@author: yang
"""

import turtle

radius = eval(input("Enter the radius:"))

turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, - 2 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, - 2 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()