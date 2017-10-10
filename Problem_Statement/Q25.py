# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:44:38 2017

@author: Girish Patil
"""

#25.Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address. 
# Both user names and company names are composed of letters only.

#Example:
#If the following email address is given as input to the program:
#
#john@google.com
#
#Then, the output of the program should be:
#
#google



def get_username(email_address,i):
    
    return email_address[:i]


def get_companyname(email_address,i,d):
    
    #slicing start with index of '@' +1 and end at index of '.'
    return email_address[i+1:d]



email_address = raw_input('Enter Email address to get user as well as Company name :-')
# first we find the index of '@' and '.' in email Address
i = email_address.find('@')
d = email_address.find('.',i)           # begin with index of @

user_name = get_username(email_address,i)
company_name = get_companyname(email_address,i,d)

print('user Name is %s &\ncompany Name is %s'%(user_name,company_name))