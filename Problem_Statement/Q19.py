# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:22:11 2017

@author: Girish Patil
"""

#19. Please write a program which count and print the numbers of each character in a string input by console.
#
#Example:
#If the following string is given as input to the program:
#
#abcdefgabc
#
#Then, the output of the program should be:
#
#a,2
#c,2
#b,2
#e,1
#d,1
#g,1
#f,1



def charecter_occurance_in_string(s):
    # take blank dictionary to store chrecter occurance in string
    d = {}
    
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    print d
    
    
s = raw_input("Enter String to get number of occurance :-")

charecter_occurance_in_string(s)