# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:46:39 2017

@author: Girish Patil
"""

#13.Write a Python program where you take any positive integer n, if n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process until you reach 1.
#Example :
#For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
#n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.



def print_untill_one_puzzle(n):
    
    if n > 0 :
        print ("%d"%(n)),
        while n != 1:
            if n %2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
            print (",%d"%(n)),
    
    
    
    
n = int(input("Enter positive number :- "))
print_untill_one_puzzle(n)