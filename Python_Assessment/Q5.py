# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:15:01 2017

@author: Girish Patil
"""

#5.Write a Python program to find a missing number from a list
#Input : [1,2,3,4,6,7,8]
#Output : 5





def get_missing_Number(li):
    
    # i is start from 1 to 8
    for i in range(li[0],li[-1]+1):        

        # Check whether i value is present in list or not (if not then return it)
        if i not in li:                    
            return i
    

li = [1,2,3,4,6,7,8]
print("Missing number is := ",get_missing_Number(li))

