# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:59:16 2017

@author: Girish Patil
"""

#4. Write a Python program to get the Fibonacci series between 0 to 50

def print_fibonacci_series(n):
    
    a = 0
    b = 1
    print ("%d,%d"%(a,b)),
    while True:
        c = a + b
        if c > 50 :
            break
        print(",%d"%(c)),
        a = b
        b = c
    
    
    
    
print_fibonacci_series(50)