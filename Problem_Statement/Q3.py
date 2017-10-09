# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 16:52:27 2017

@author: Girish Patil
"""

## 3. Write a Python program to construct the following pattern, using a nested for loop.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*



#n is the how many maximum number of "*" to be print in pattern
def pattern(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print "*",
         
        print "\n"
    
    for i in range(n-1,0,-1):
        for j in range(0,i):
            print "*",
            
        print "\n"
    

pattern(5)