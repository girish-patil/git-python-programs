# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:35:39 2017

@author: Girish Patil
"""
# Custom Exception class
class my_exception(Exception):
    
    def __init__(self,msg):
        self.msg = msg
        
        
raise my_exception("Exception is raised")