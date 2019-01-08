#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:10:09 2019

@author: yang
"""

import turtle

x, y = eval(input("Enter the center of the rectangle:"))
width, height = eval(input("Enter the width and the height:"))

turtle.penup()
turtle.goto(width / 2, height / 2)
turtle.pendown()
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)

turtle.done()
