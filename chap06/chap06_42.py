#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:02:29 2019

@author: yang
"""

import turtle
import math

# draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    
# write a string s at the specified location (x, y)
def writeText(s, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(s)
    
def drawSin():
    turtle.speed(10)
    turtle.penup()
    x = -175
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.pendown()
    for x in range(-175, 176):
        turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
        
    
    
def main():
    drawSin()
    
    writeText("-2\u03c0", -100, -15)
    writeText("2\u03c0", 100, -15)
    
    drawLine(-200, 0, 200, 0)
    turtle.goto(190, -6)
    turtle.goto(200, 0)
    turtle.goto(190, 6)
    
    drawLine(0, -70, 0, 70)
    turtle.goto(6, 60)
    turtle.goto(0, 70)
    turtle.goto(-6, 60)

    turtle.hideturtle()
    turtle.done()
    
main()
    