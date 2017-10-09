# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:32:37 2017

@author: Girish Patil
"""

# 21.With a given list [12,24,35,24,88,120,155,88,120,155], 
#write a program to print this list after removing all duplicate values with original  
#order reserved.


li = [12,24,35,24,88,120,155,88,120,155]


def remove_duplicate_in_same_list(li):
    
    length = len(li)
    
    for i in range(length):

        for j in range(i+1,length-1):
            #To check whether elements are same or not if same then del it
            if li[i] == li[j]:
                del li[j]
                length = len(li)
            else:
                continue
            
    #to check whether last two elements are same or not
    if li[-2] == li[-1]:
        del li[-1]
    
    
    return li



print remove_duplicate_in_same_list(li)