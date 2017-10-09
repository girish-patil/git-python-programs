# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 13:00:03 2017

@author: Girish Patil
"""

#7.Write a program to display an user-defined Exception


#below code is written to ask user to enter number to guess the number stored,
#to help, we give hint to them greater than that number or less than that number

#user defined python exception
class Error(Exception):
    pass

class valueissmall(Error):
    pass

class valueislarge(Error):
    pass


num = 15

while True:
    try:
    
        i = int(input("Enter number :- "))
    
        if i < num :
            raise valueissmall
        elif i > num :
            raise valueislarge
        else:
            break
        
    except valueissmall:
            print('value is small')
        
    except valueislarge:
            print('value is large')

print ('yes finally u got it 15')

