#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:45:08 2019

@author: yang
"""

from tkinter import * # Import all definitions from tkinter
import random

class DeckOfCardsGUI:
    
    def __init__(self):
        window = Tk()
        window.title("Pick Four Cards Randomly")
        
        self.imageList = []     # Store images for cards
        for i in range(1, 55):
            self.imageList.append(PhotoImage(file = "image/card/" + str(i) + ".gif"))
            
        frame = Frame(window)   # Hold four labels for cards
        frame.pack()
        
        self.labelList = []     # A list of four label
        for i in range(4):
            self.labelList.append(Label(frame, image = self.imageList[i]))
            self.labelList[i].pack(side = LEFT)
            
        Button(window, text = "Shuffle", command = self.shuffle).pack()
        
        window.mainloop()
        
    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]
            
DeckOfCardsGUI()