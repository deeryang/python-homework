#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:09:46 2019

@author: yang
"""

from tkinter import *
from StillClock import StillClock

class DisplayClock:
    
    def __init__(self):
        window = Tk()
        window.title("Change Clock Time")
        
        self.clock = StillClock(window)     # Create a clock
        self.clock.pack()
        
        frame = Frame(window)
        frame.pack()
        
        Label(frame, text = "Hour: ").pack(side = LEFT)
        self.hour = IntVar()
        self.hour.set(self.clock.getHour())
        Entry(frame, textvariable = self.hour, width = 2).pack(side = LEFT)

        Label(frame, text = "Minute: ").pack(side = LEFT)        
        self.minute = IntVar()
        self.minute.set(self.clock.getMinute())
        Entry(frame, textvariable = self.minute, width = 2).pack(side = LEFT)
        
        Label(frame, text = "Second: ").pack(side = LEFT)
        self.second = IntVar()
        self.second.set(self.clock.getSecond())
        Entry(frame, textvariable = self.second, width = 2).pack(side = LEFT)
        
        Button(frame, text = "Set New Time", command = self.setNewTime).pack(side = LEFT)
        
        window.mainloop()
        
    def setNewTime(self):
        self.clock.setHour(self.hour.get())
        self.clock.setMinute(self.minute.get())
        self.clock.setSecond(self.second.get())
        
DisplayClock()