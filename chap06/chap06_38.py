#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:10:13 2019

@author: yang
"""

import turtle

def drawLine(x1, y1, x2, y2, color = "black", size = 1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    
def main():
    drawLine(1, 1, 100, 100, "red", 5)
    turtle.hideturtle()
    turtle.done()
    
main()