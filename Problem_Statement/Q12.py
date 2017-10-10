# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:08:45 2017

@author: Girish Patil
"""

human_age = int(input("dog age in human years :-"))

if human_age < 0:
	print("Invalid Age")
	exit()
elif human_age <= 2:
	dog_age = human_age * 10.5
else:
	dog_age = 21 + (human_age - 2)*4

print("dog age in dog years is %d"%(dog_age))