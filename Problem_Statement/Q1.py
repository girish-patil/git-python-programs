# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:48:37 2017

@author: Girish Patil
"""

# 1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)




for i in range(1500,2701):
    if(i%7 == 0 and i%5 == 0):
        print i
        
        
# or
#7*5 = 35 then,
#find the first very multiple of 35 from 1500, then simply print number + 35 upto 2700
#        here 1505 is first multiple of 35
        
#for i in range(1505,2701,35):
#    print i