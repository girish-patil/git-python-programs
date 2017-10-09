# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:35:36 2017

@author: Girish Patil
"""

#2.Write a program to demonstrate printing pattern of alphabets

#A 
#B C 
#D E F 
#G H I J 
#K L M N O 



def pattern(n):                     # n = 5 is to print number of lines

    ch = 65                     #ASCII value of 'A is 65'
    print("Pattern is : ")
    for i in range(n):          # i starts with 0 to 4
        for j in range(-1,i):   # j starts with -1 to i
            print chr(ch),      #to get character from the ASCII value we use the chr() function
            ch += 1             # increase the ASCII each time by 1 to get next charecter
            
            if(ch == 91):       # to get charecters in pattern only in the range of A to Z 
                ch = 65
        print                   # to get the cursor on next line(bydefault print function at the end goes on next line)

pattern(5)