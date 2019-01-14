#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:31:12 2019

@author: yang
"""

import turtle

# draw one chessboard whose-upper-left corner is at
#  (startx, starty) and bottom-right corner is at (endx, endy)
def drawChessBoard(startx, endx, starty, endy):
    turtle.speed(10)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 != 0:
                turtle.begin_fill()
            turtle.penup()
            stepx = abs(endx - startx) / 8
            stepy = abs(endy - starty) / 8
            x = startx + stepx * i
            y = starty - stepy * j
            turtle.goto(x, y)
            turtle.pendown()
            turtle.setheading(0)
            turtle.forward(stepx)
            turtle.left(90)
            turtle.forward(stepy)
            turtle.left(90)
            turtle.forward(stepx)
            turtle.left(90)
            turtle.forward(stepy)
            if (i + j) % 2 != 0:
                turtle.end_fill()
                
def main():
    drawChessBoard(-250, -50, 100, -100)
    drawChessBoard(50, 250, 100, -100)
    
    turtle.hideturtle()
    turtle.done()
    
main()