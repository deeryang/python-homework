#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:05:24 2019

@author: yang
"""

from tkinter import * # Import all definitions from tkinter

def processOK():
    print("OK button is clicked")
    
def processCancel():
    print("Cancel button is clicked")
    
window = Tk()   # Create a window
btOK = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)
btOK.pack()
btCancel.pack()

window.mainloop()