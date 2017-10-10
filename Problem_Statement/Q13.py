# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:31:41 2017

@author: Girish Patil
"""

#13. Write a Python program to check whether an alphabet is a vowel or consonant.
#Expected Output:
#
#Input a letter of the alphabet:                                        
#k is a consonant.



vowels = ['a','e','i','o','u','A','E','I','O','U']

def check_vowel_or_consonent(ch):
    
    if ch in vowels:
        return " is vowel"
    else:
        return "is consonant"
    
    
ch = raw_input("Enter alphabet to be check :-")
print ("%s %s"%(ch,check_vowel_or_consonent(ch)))