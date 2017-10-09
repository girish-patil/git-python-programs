# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:00:58 2017

@author: Girish Patil
"""

#3.Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple




# below function is written to return last element of each tuple in list
def on_last_sort_element(li):
    return li[-1]               


def sort_list(li):
    return sorted(li , key = on_last_sort_element)      # sorted function return a sorted list of elements in specific order

    

li = [(2,3),(1,1),(3,2),(5,4),(6,2),(1,5)]              # List of Tuples
print("sorted list of tuples by the last element in each tuple is: ", sort_list(li))