# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:52:11 2017

@author: Girish Patil
"""

#24.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')




n = input("Enter Numbers seperated by comma operator:-")
print list(n)
print tuple(n)