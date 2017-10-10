# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:15:57 2017

@author: Girish Patil
"""

#20.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#Then, the output should be:
#2:2
#3.:1
#3?:1
#New:1
#Python:5
#Read:1
#and:1
#between:1
#choosing:1
#or:2
#to:1


# sorting of key left

          



def charecter_occurance_in_string(s):
    # take blank dictionary to store chrecter occurance in string
    d = {}
    li = s.split()
    for c in li:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    
    li = d.keys()
    li.sort()
    for i in li:
        print("%s  %s"%(i,d.get(i)))
    
    
s = raw_input("Enter String to get number of occurance :-")

charecter_occurance_in_string(s)