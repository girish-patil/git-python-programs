# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:22:26 2017

@author: Girish Patil
"""

#9.Write a PYTHON program to check the validity of a password chosen by a user.
#
#To be considered valid, a password
#
#a) contains at least 1 letter between [A-Z],
#
#b) contains at least 1 letter between [a-z],
#
#c) contains at least 1 number between [0-9],
#
#d) contains at least 1 special character from [$#@],
#
#e) has a minimum length of 6 characters, and
#
#f) has a maximum length of 12 characters.
#
#Your program will consist of two user-defined functions: validate(s) and main(). 
#The validate() function implements the validation procedure described above.
# The parameter (or input) to the function is a string s. 
# If s fits the above criteria, print valid. Otherwise, print not valid.


import re

def validate(s):
    
    length = len(s) 
    x = True

    #Python offers two different primitive operations based on regular expressions:
    #re.match() checks for a match only at the beginning of the string,
    #while re.search() checks for a match anywhere in the string
    
    while x:
        
        if(length < 6 or length > 12):
            break
        elif not re.search("[a-z]",s):
            break
        elif not re.search("[0-9]",s):
            break
        elif not re.search("[A-Z]",s):
            break
        elif not re.search("[$#@]",s):
            break
        else:
            print("Valid Password")
            x = False
            break
        
    if x:
        print "Please enter valid Password"
    


def main():
    p = raw_input('Enter password to validate :=')
    validate(p)

    
#if it is not imported then call main function
if __name__ == "__main__":
    main()