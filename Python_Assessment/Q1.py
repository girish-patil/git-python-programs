# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:02:25 2017

@author: Girish Patil
"""

# 1. Write a program to raise a RunTimeError Exception



#if user give 'girish' as argument to function it raise exceptin

def check_name(name):
    if name == "girish":
        raise Exception("bye Girish")
    print "Hi there {0}".format(name)
    
try:
    check_name("girish")
except Exception as e:
    print e