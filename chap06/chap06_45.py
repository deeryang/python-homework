#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:22:45 2019

@author: yang
"""

import turtle

def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    turtle.penup()
    turtle.goto(x + radius, y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(radius, steps = numberOfSides)
    
def main():
    for i in range(6):
        x = -250 + i * 100
        y = 0
        radius = 40
        drawPolygon(x, y, radius, i + 3)
    turtle.hideturtle()
    turtle.done()
    
main()