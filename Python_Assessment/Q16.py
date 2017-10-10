# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:23:35 2017

@author: Girish Patil
"""

#16.Write a Program to Count the Number of Lines in a Text File



def get_number_of_lines():
    try:
        fo = open("temp.txt","rb")
        length = len(fo.readlines())
        print("number of lines in file is %d"%(length))
        
    except IOError:
        print "cant find file"
        
    finally:
        fo.close()
    
    
get_number_of_lines()