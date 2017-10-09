# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:57:20 2017

@author: Girish Patil
"""

# 24.Write a program which accepts a sequence of words separated by whitespace as input 
#to print the words composed of digits only.
#
#Example:
#If the following words is given as input to the program:
#
#2 cats and 3 dogs.
#
#Then, the output of the program should be:
#
#['2', '3']
#
#In case of input data being supplied to the question, it should be assumed to be a console input.







def get_digits_from_string(s):
    li = []
    for i in s:
        if i.isdigit():
            li.append(i)
    return li




s = raw_input("Enter String :-")

print get_digits_from_string(s)