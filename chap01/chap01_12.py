#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:56:51 2019

@author: yang
"""

import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.goto(0, 0)
turtle.goto(0, -100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(0, 0)

turtle.done()