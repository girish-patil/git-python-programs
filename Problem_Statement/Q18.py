# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:10:11 2017

@author: Girish Patil
"""

#18.Please write a program which accepts a string from console and print it in reverse order.
#
#Example:
#If the following string is given as input to the program:
#
#rise to vote sir
#
#Then, the output of the program should be:
#
#ris etov ot esir


def string_reverse(s):
    print s[::-1]           # String Slicing from the End [start:end:step]

s = raw_input("Enter String to be reversed :-")

string_reverse(s)