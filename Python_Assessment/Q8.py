# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 14:31:36 2017

@author: Girish Patil
"""

#8.Write a program to overload + operator.



class PlusOperatorOverloading:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
     #ist like toString in java whenever we try to print the objetct this method gets executed
    def __str__(self):
        return ("{0},{1}").format(self.x,self.y)
        
    #To overload the + operator, we implement __add__() 
    def __add__(self,next):
        x = self.x + next.x
        y = self.y + next.y
        return PlusOperatorOverloading(x,y)
    
    

p = PlusOperatorOverloading(2,3)
p1 = PlusOperatorOverloading(2,-5)

print(p+p1)