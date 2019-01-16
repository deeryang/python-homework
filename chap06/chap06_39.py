#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:14:48 2019

@author: yang
"""

import turtle
import math

def drawLine(x1, y1, x2, y2, color = "black", size = 1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    
def drawStar():
    side = 200
    sita = math.radians(18)
    x1 = y1 = 0
    x2 = side * math.sin(sita)
    y2 = -side * math.cos(sita)
    drawLine(x1, y1, x2, y2)
    x3 = x2 - side * math.cos(2 * sita)
    y3 = y2 + side * math.sin(2 * sita)
    drawLine(x2, y2, x3, y3)
    x4 = x3 + side
    y4 = y3
    drawLine(x3, y3, x4, y4)
    x5 = x4 - side * math.cos(2 * sita)
    y5 = y4 - side * math.sin(2 * sita)
    drawLine(x4, y4, x5, y5)
    drawLine(x5, y5, x1, y1)
    
    turtle.hideturtle()
    turtle.done()
    
drawStar()