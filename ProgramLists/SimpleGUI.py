#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:01:47 2019

@author: yang
"""

from tkinter import * # Import all definitions from tkinter

window = Tk()   # Create a window
label = Label(window, text = "Welcome to Python") # Create a label
button = Button(window, text = "Click Me")  # Create a button
label.pack()    # Place the label in the window
button.pack()   # Place the button in the window

window.mainloop()