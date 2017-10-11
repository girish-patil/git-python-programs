# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:57:39 2017

@author: Girish Patil
"""

#11.Write a Python program to find whether it contains an additive sequence or not.
#The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
#Sample additive sequence: 6, 6, 12, 18, 30
#In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
#Also, you can split a number into one or more digits to create an additive sequence.
#Sample additive sequence: 66121830
#In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
#Note : Numbers in the additive sequence cannot have leading zeros.







def check_additive(s):
    i = 1
    a = int(s[0])
    b = int(s[i])
    # take as flag whether it is additive or not
    additive = True
    string_length = len(s)-1

    while i < string_length:
        
        c = a + b        
        c = str(c)
        length = len(c)        
        d = int(c)
        
        #normal fibonacci logic ( follow up pointers)
        a = b
        b = int(s[i+1:i+length+1])

        
        
        if d == b:
            additive = True
        else:
            additive = False
            break
        
        i = i+length

    

    
    return additive
    
    


s = raw_input("Enter String of numbers to check additive or not :-")
if len(s) != 1:
    if check_additive(s):
        print "Given String is additive"
    else:
        print "Given String is not additive"
else:
    print "please enter more than 1 element"