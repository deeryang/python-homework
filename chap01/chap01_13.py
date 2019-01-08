#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:03:59 2019

@author: yang
"""

import turtle

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.goto(100, 0)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.goto(0, -100)
turtle.right(90)

turtle.done()