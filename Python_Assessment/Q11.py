# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:57:39 2017

@author: Girish Patil
"""


def check_additive(s):
    i = 1
    a = int(s[0])
    b = int(s[i])
    additive = True
    string_length = len(s)
    while True:
        
        c = a + b
        length = len(c)
        a = b
        b = int(s[i+1:i+length+1])
        i = i+length
        if b != c:
            additive = False
            break
        
        if i == string_length:        
            break
        
    return additive
    
    


s = raw_input("Enter String of numbers to check additive or not :-")

print check_additive(s)