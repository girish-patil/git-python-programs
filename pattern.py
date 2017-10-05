# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:23:10 2017

@author: Girish Patil
"""


n = 5
for i in range(0,n):
    for j in range(0,n):
        print "* ",
    print '\n'
    
    

#n=4
#for i in range(0,n):
#    for j in range(0,i+1):
#        print "* ",
#    print '\n'
    
#def char_frequency(str1):
#    dict = {}
#    for n in str1:
#        keys = dict.keys()
#        print keys
#        if n in keys:
#            dict[n] += 1
#        else:
#            dict[n] = 1
#    return dict
#print(char_frequency('google.com'))
    


#
#def string_2_first_last_char(str):
#    l = len(str)
#    if l < 2:
#        return ''
#    else:
#        return str[0:2]+str[-2:]
#
#print (string_2_first_last_char('girish'))


#def change_char(str1):
#  char = str1[0]
#  length = len(str1)
#  str1 = str1.replace(char, '$')
#  str1 = char + str1[1:]
#
#  return str1
#
#print(change_char('restart'))
        

#
#string = "+ is an operator."
#
#new_string = string.capitalize()
#
#print('Old String:', string)
#print('New String:', new_string)

#
#def find_longest_word(words_list):
#    word_len = []
#    for n in words_list:
#        word_len.append((len(n), n))
#    print word_len
#    word_len.sort()
#    print word_len
#    return word_len[-1][1]
#
#print(find_longest_word(["PHP", "Exercises", "Backend"]))

#
#def remove_char(str, n):
#      first_part = str[:n] 
#      last_pasrt = str[n+1:]
#      return first_part + last_pasrt
#print(remove_char('Python', 0))
#print(remove_char('Python', 3))
#print(remove_char('Python', 5))

#
print [i for i in range(10,3,-2)]