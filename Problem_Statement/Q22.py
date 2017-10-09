# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 14:52:11 2017

@author: Girish Patil
"""

#22.By using list comprehension,
# please write a program to print the list after removing the v0th, 2nd, 4th,6th numbers
# in [12,24,35,70,88,120,155].


li = [12,24,35,70,88,120,155]
length = len(li)

for i in range(0,length/2+1):
    del li[i]
        
print li