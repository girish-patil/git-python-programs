# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:29:22 2017

@author: Girish Patil
"""

#2. Write a Python program to convert temperatures to and from celsius, fahrenheit.


i = raw_input("Enter temprature to convert eg. C or F :-")

degree = int(i[:-1])         # to get the degree only without "F" or "C"

if i[-1].upper() == 'C':
    r = int(round((9 * degree) / 5 + 32))
    print("the temprature in celsius is %dC Conversion to fahrenheit is %dF"%(degree,r))
elif i[-1].upper() == 'F':
    r = int(round((degree - 32) * 5 / 9))
    print("the temprature in fahrenheit is %dF Conversion to celsius is %dC"%(degree,r))
else:
    print "Enter valid Input ending with C or F"
    


