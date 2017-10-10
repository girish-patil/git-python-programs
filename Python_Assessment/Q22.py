# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:00:13 2017

@author: Girish Patil
"""

#22.Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3




s = raw_input("Enter sentense :-")

alphabet = 0
digit = 0
for i in s:
    if i.isalpha():
        alphabet += 1
    elif i.isdigit():
        digit += 1
        
print ("Alphabet = %d & Digits = %d"%(alphabet,digit))










    