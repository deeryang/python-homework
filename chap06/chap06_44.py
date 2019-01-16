#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:22:57 2019

@author: yang
"""

import turtle

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
    
def drawPowerLine():
    turtle.penup()
    turtle.goto(-150, (150 / 10) ** 2)
    turtle.pendown()
    for x in range(-150, 151):
        turtle.goto(x, (x / 10) ** 2)
        
        
def main():
    drawPowerLine()
    
    
    drawLine(-200, 0, 200, 0)
    turtle.goto(190, -6)
    turtle.goto(200, 0)
    turtle.goto(190, 6)
    
    drawLine(0, -150, 0, 150)
    turtle.goto(6, 140)
    turtle.goto(0, 150)
    turtle.goto(-6, 140)
    
    writeText("x", 220, 0)
    writeText("y", 0, 170)
    
    turtle.hideturtle()
    turtle.done()
    
main()