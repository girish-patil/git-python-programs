# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:32:18 2017

@author: Girish Patil
"""


#6. Assuming that we have some email addresses in the "username@companyname.com" format
#, please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.




def get_username(email_address,i):
    
    return email_address[:i]


def get_companyname(email_address,i,d):
    
    #slicing start with index of '@' +1 and end at index of '.'
    return email_address[i+1:d]



email_address = 'girishpatil@quantiphi.com'
# first we find the index of '@' and '.' in email Address
i = email_address.find('@')
d = email_address.find('.',i)           # begin with index of @

user_name = get_username(email_address,i)
company_name = get_companyname(email_address,i,d)

print('user Name is %s &\ncompany Name is %s'%(user_name,company_name))