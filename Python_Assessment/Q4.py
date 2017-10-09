# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:19:14 2017

@author: Girish Patil
"""

# 4.Write a program to Find the Sum of Digits in a Number






def sum_of_the_digits(num):
    sum = 0
    while(num > 0):
        digit = num%10
        sum += digit
        num = num / 10
        
    return sum


num = 12345
sum = sum_of_the_digits(num)
print ("number = %d \n Sum of the digit of number is := %d"%(num,sum))