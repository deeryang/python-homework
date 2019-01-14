#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:43:21 2019

@author: yang
"""

import time
import sys

# return the English name for the month
def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    elif month == 12:
        monthName = "December"
    else:
        sys.exit()
        
    return monthName

# return true if it is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# return the number of days in a month
def getNumberOfDaysInMonth(year, month):
    biggerList = [1, 3, 5, 7, 8, 10, 12]
    smallerList = [4, 6, 9, 11]
    if month in biggerList:
        return 31
    if month in smallerList:
        return 30
    if month == 2:
        return 29 if isLeapYear(year) else 28
    
# get the total number of days
def getTotalNumberDays()        :
    return

# return total number of days from Jan 1st, 1970 to the specified day
def getTotalDaysInYears(year):
    total = 0
    for i in range(1970, year + 1):
        if isLeapYear(i):
            total += 366
        else:
            total += 365
    
    return total

# return total number of days from Jan 1st to the month in the year
def getTotalDaysInMonths(year, month):
    total = 0
    for i in range(1, month + 1):
        total += getNumberOfDaysInMonth(year, i)
        
    return total
            
# return the current day and time
def getTime():
    currentTime = time.time()
    totalSeconds = int(currentTime)
    currentSecond = totalSeconds % 60
    totalMinutes = totalSeconds // 60
    currentMinute = totalMinutes % 60
    totalHours = totalMinutes // 60
    currentHour = totalHours % 60
    totalDays = totalHours // 24
    if currentHour > 0:
        totalDays += 1
    
    # obtain year
    currentYear = 1970
    while getTotalDaysInYears(currentYear) < totalDays:
        currentYear += 1
        
    # obtain month
    totalNumberDaysInTheYear = totalDays - getTotalDaysInYears(currentYear - 1)
    currentMonth = 1
    while getTotalDaysInMonths(currentYear, currentMonth) < totalNumberDaysInTheYear:
        currentMonth += 1
        
    # obtain day
    currentDay = totalNumberDaysInTheYear - getTotalDaysInMonths(currentYear, currentMonth - 1)
    
    
    # display result
# =============================================================================
#     print("Year", currentYear)
#     print("Month", getMonthName(currentMonth))
#     print("Day", currentDay)
#     print("Hour", currentHour)
#     print("Minute", currentMinute)
#     print("Second", currentSecond)
# =============================================================================
    
    print("Current date is", getMonthName(currentMonth), currentDay, ",", currentYear)
    print("Current time is", currentHour, ":", currentMinute, ":", currentSecond)


def main():
    getTime()
    
main()