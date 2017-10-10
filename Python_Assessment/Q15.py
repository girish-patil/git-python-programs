# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:17:53 2017

@author: Girish Patil
"""

#15.Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
#Example
#Case 1:
#Enter a list of tuples:[(2,5),(1,2),(4,4),(2,3)]
#Sorted:
#[(1, 2), (2, 3), (4, 4), (2, 5)]
# 
#Case 2:
#Enter a list of tuples:[(23,45),(25,44),(89,40)]
#Sorted:
#[(89, 40), (25, 44), (23, 45)]




# below function is written to return last element of each tuple in list
def on_last_sort_element(li):
    return li[-1]               


def sort_list(li):
    return sorted(li , key = on_last_sort_element)      # sorted function return a sorted list of elements in specific order

    

li = [(2,3),(1,1),(3,2),(5,4),(6,2),(1,5)]              # List of Tuples
print("sorted list of tuples by the last element in each tuple is:  ", sort_list(li))