# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:30:00 2017

@author: Girish Patil
"""

n = input('Enter number to check prime or not')
flag = 0
if n > 1:
    for i in range(2,n-1):
        if n%i==0:
            #global flag
            flag = 1
            print n,'is not a prime Number'
            break
if flag == 0:
    print n,' is prime number'
    