#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:33:34 2019

@author: yang
"""

import turtle
import random
import math

# draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    
# draw a circle centered at (x, y) with the specified radius
def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)
    
# draw a dot at specified location (x, y) with specified radius
def drawDot(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(radius)
    
def main():
    drawRectangle(-75, 0, 100, 100)
    for i in range(10):
        x = random.randint(-125, -25)
        y = random.randint(-50, 50)
        drawDot(x, y, 5)
        
    drawCircle(50, 0, 50)
    counter = 0
    while counter < 10:
        x = random.randint(0, 100)
        y = random.randint(-50, 50)
        if math.sqrt((x - 50) ** 2 + y ** 2) < 50:
            drawDot(x, y, 5)
            counter += 1
    

    turtle.hideturtle()
    turtle.done()

main()