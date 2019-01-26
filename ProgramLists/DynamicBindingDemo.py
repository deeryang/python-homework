#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:59:21 2019

@author: yang
"""

class Student:
    def __str__(self):
        return "Student"
    
    def printStudent(self):
        print(self.__str__())
        
class GraduateStudent(Student):
    def __str__(self):
        return "Graduate Student"
    
a = Student()
b = GraduateStudent()
a.printStudent()
b.printStudent()