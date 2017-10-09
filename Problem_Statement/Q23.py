# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:08:51 2017

@author: Girish Patil
"""

#23.Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.




def binary_search(li,element):
    length = len(li)
    left = 0
    right = length-1
    mid = (left+right)/2
    
    while not li[mid] == element:
        
        if element > li[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
        mid = (left+right)/2
        if li[mid] == element :
            print "element is found at %d position in list"%(mid+1)
    
    
li = [12,15,18,19,25,30,34,40]

element = input("Enter Element to be searched in list")

binary_search(li,element)