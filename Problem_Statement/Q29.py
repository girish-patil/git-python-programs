# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:51:40 2017

@author: Girish Patil
"""

#29.Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
#D 100
#W 200
#
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500



        
    

def bank_operation(s):
    balance = 0
    while True:
        
        if s[0].upper() == 'D':
            balance += int(s[1:])
    
        elif s[0].upper() == 'W':
            if int(s[1:]) > balance:
                print("you have not sufficient amount Please Enter valid amount")
            else:
                balance -= int(s[1:])

        elif s[0].upper() == 'Q':
            print ("Your Current Balance is = %d"%(balance))
            break
        else:
            print ("Enter valid operation")
            break
        
        s = raw_input("Enter amout to be deposit eg.D350 or withdraw eg.W250 and enter Q for exit :-")



s = raw_input("Enter amout to be deposit eg.D350 or withdraw eg.W250 and enter Q for exit :-")

bank_operation(s)        