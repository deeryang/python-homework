#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:12:06 2019

@author: yang
"""

import turtle

radius = 100

turtle.penup()
turtle.goto(-radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()