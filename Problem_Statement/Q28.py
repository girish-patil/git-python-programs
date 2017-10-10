# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:05:02 2017

@author: Girish Patil
"""

#28. A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them 
#according to the above criteria. Passwords that match the criteria are to be printed, 
#each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1



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
            print("'%s' is Valid Password "%(s))
#            x = False
            break
        
#    if x:
#        print "Please enter valid Password"
    


def main():
    s = raw_input('Enter password to validate :=')
    li = s.split(",")
    for p in li:
        validate(p)

    
#if it is not imported then call main function
if __name__ == "__main__":
    main()