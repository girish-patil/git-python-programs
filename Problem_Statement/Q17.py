# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:54:22 2017

@author: Girish Patil
"""

#17.Please write a program which accepts a string from console and print the characters 
#that have even indexes.

#Example:
#If the following string is given as input to the program:
#
#H1e2l3l4o5w6o7r8l9d
#
#Then, the output of the program should be:
#
#Helloworld




def print_even_char(s):
    length = len(s)
    s1 = ""
    for i in range(0,length,2):
        s1 += s[i]
    print s1
s = raw_input("Enter String to print even index only :-")
print_even_char(s)



# without using new string

#
#def print_even_char(s):
#    length = len(s)
#    for i in range(0,length,2):
#        print ("%s"%(s[i])),
#s = raw_input("Enter String to print even index only :-")
#print_even_char(s)
