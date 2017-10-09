# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:03:09 2017

@author: Girish Patil
"""

#6.Write a Python program to print alphabet pattern 'A'.
#Expected Output:
#
#    
#      * * * 
#    *       *
#    *       *
#    * * * * *
#    *       *
#    *       *
#    *       *
#    



for i in range(1,8):

    if i == 1:
        print "  ",
    else:
        print "* ",

    for j in range(1,4):
        if i == 1 or i == 4:
            print "* ",
        else:
            print "  ",
    
    if i == 1:
        print
    else:
        print "*"
        
