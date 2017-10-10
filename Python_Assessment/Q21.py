# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:25:21 2017

@author: Girish Patil
"""


#21.Write a Program to Read the Contents of a File in Reverse Order

for line in reversed(open("temp.txt").readlines()):
    print line.rstrip()