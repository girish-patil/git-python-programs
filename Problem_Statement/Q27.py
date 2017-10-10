# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:49:48 2017

@author: Girish Patil
"""

# 27.Write a program to generate and print another tuple whose values are even numbers 
#    in the given tuple (1,2,3,4,5,6,7,8,9,10).






def get_even_numbers(t):
    # because list are immutable, we can update the list
    li = list(t)
    for i in li:
        #check whether the ele
        if i % 2 != 0:
            li.remove(i)
    
    # return list        
    return li


t1 = (1,2,3,4,5,6,7,8,9,10)
# function returns list we convert it into tuple
t = tuple(get_even_numbers(t1))
print t