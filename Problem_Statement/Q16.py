# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:43:39 2017

@author: Girish Patil
"""

#16. Please write a program which prints all permutations of [1,2,3]


#the itertool module is standard library that contains several functions that are useful in functional programing
# one of them function in itertool is permutation , which is used when you want to accomplish a
# Task with all combination


from itertools import permutations

li = [1,2,3]
print list(permutations(li))