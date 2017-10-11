# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:44:44 2017

@author: Girish Patil
"""

#15.  Write a program to solve a classic ancient Chinese puzzle: 
#     We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#     How many rabbits and how many chickens do we have?



def puzzle(h,l):

    for r in range(h + 1):
        c = h - r
        if 2 * c + 4 * r == l:
            print ("Number of chickens are %d and rabbits are %d."%(c,r))
            


h = 35
l = 94
puzzle(h,l)   
    

