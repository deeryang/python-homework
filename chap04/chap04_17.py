#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:00:55 2019

@author: yang
"""

import random

master = eval(input("scissor (0), rock (1), paper (2):"))
computer = random.randint(0, 2)

if computer == 0:
    print("The computer is scissor. ", end = "")
    if master == 0:
        print("You are scissor too. It is a draw.")
    elif master == 1:
        print("You are rock. You won")
    else:
        print("You are paper. You lost.")
elif computer == 1:
    print("The computer is rock. ", end = "")
    if master == 0:
        print("You are scissor. You lost.")
    elif master == 1:
        print("You are rock too. It is a draw.")
    else:
        print("You are paper. You won.")
else:
    print("The computer is paper. ", end = "")
    if master == 0:
        print("You are scissor. You won.")
    elif master == 1:
        print("You are rock. You lost")
    else:
        print("You are paper too. It is a draw.")