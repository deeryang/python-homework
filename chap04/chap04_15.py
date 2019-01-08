#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:27:52 2019

@author: yang
"""

import random

lottery = random.randint(0, 999)
guess = eval(input("Enter your lottery pick (three digits):"))

lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery // 10 % 10
lotteryDigit3 = lottery % 10

guessDigit1 = guess // 100
guessDigit2 = guess // 10 % 10
guessDigit3 = guess % 10

print("The lottery number is:", lottery)

lotterySorted = sorted([lotteryDigit1, lotteryDigit2, lotteryDigit3])
guessSorted = sorted([guessDigit1, guessDigit2, guessDigit3])

if guess == lottery:
    print("Exact match: you win $10,000")
elif lotterySorted == guessSorted:
    print("Match all digits: you win $3,000")
elif lotterySorted[0] == guessSorted[0] or lotterySorted[1] == guessSorted[1] or lotterySorted[2] == guessSorted[2]:
    print("Match at least one digit: you win $1,000")
else:
    print("Sorry, no match")
