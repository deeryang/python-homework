#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:46:28 2019

@author: yang
"""

import turtle
import math

# draw a line from point (x1, y1) to point (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    
# draw a hexagon
def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    angle = 2 * math.pi / numberOfSides

    # Connect points for the polygon
    for i in range(numberOfSides + 1):  
        for j in range(numberOfSides + 1):  
             drawLine(x + radius * math.cos(i * angle),
                y - radius * math.sin(i * angle),     
                x + radius * math.cos(j * angle),
                y - radius * math.sin(j * angle))     

def main():
    turtle.speed(10) # Fastest   

    drawPolygon(0, 0, 50, 6)

    turtle.hideturtle()

    turtle.done()
    
main()