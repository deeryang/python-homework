#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:25:28 2019

@author: yang
"""

import turtle
#import math

# fill a rectangle
def drawRectangle(color = "black", x = 0, y = 0, width = 30, height = 30):
    turtle.penup()
    turtle.begin_fill()
    turtle.color(color)
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    turtle.goto(x + width / 2, y - height / 2)
    turtle.goto(x + width / 2, y + height / 2)
    turtle.goto(x - width / 2, y + height / 2)
    turtle.goto(x - width / 2, y - height / 2)
    turtle.end_fill()
    
# fill a circle
def drawCircle(color = "black", x = 0, y = 0, radius = 50):
    turtle.penup()
    turtle.begin_fill()
    turtle.color(color)
    turtle.goto(x, y - radius)
    turtle.circle(radius)
    turtle.end_fill()
    
def main():
    drawRectangle("blue", -200, 0, 200, 150)
    drawCircle("red", 100, 0, 75)
    turtle.hideturtle()
    turtle.done()
    
main()