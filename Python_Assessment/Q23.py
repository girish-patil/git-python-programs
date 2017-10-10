# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:29:40 2017

@author: Girish Patil
"""

#23.Write a Program to Read a String from the User and Append it into a File



    
    
    
    
    
    
s = raw_input("Enter string to append in file :-")

with open("temp.txt",'a') as f:
    f.write(s)