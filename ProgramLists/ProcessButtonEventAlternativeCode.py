#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:44:12 2019

@author: yang
"""

from tkinter import *  # Import all definitions from tkinter

class ProcessButtonEvent:
    
    def __init__(self):
        window = Tk()   # Create a window
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "Cancel", bg = "yellow", command = self.processCancel)
        btOK.pack()
        btCancel.pack()
        
        window.mainloop()
        
    def processOK(self):
        print("OK button is clicked")
        
    def processCancel(self):
        print("Cancel button is clicked")
        
ProcessButtonEvent()