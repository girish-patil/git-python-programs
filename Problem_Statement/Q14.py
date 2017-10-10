# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:13:35 2017

@author: Girish Patil
"""

#14. Write a Python program to get next day of a given date. 
#
#Expected Output:
#Input a year: 2016                                                      
#Input a month [1-12]: 08                                                
#Input a day [1-31]: 23                                                  
#The next date is [yyyy-mm-dd] 2016-8-24 


md = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}


y = input("Enter Year:-")
m = input("Enter Month:-")
d = input("Enter Day:-")

def get_next_day(y,m,d):
    if((y%400 == 0)or((y%4 == 0 )and(y%100 != 0))):
        md[2] = 29
        
    else:
        md[2] = 28
    
    if d == md[m]:
        d = 1
        if m == 12:
            m = 1
            y = y + 1
        else:
            m += 1
    else:
        d = d+1
        
    
    print ("The next date is [yyyy-mm-dd] %d-%d-%d"%(y,m,d))
    
get_next_day(y,m,d)