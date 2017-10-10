# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:54:46 2017

@author: Girish Patil
"""

# 14.Write a Python program to check if a given positive integer is a power of two


def check_number_is_pow_of_two(n):
    flag = True
    while n != 1:
        
        if n % 2 != 0:
            flag = False
            break
        
        n = n / 2
        
    return flag
    
    
    
    
    
    
    
n = int(input("Enter positive number :- "))

if check_number_is_pow_of_two(n):
    print "It is Power of 2"
else:
    print "It is not power of 2"