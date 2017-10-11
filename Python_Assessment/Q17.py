# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:30:24 2017

@author: Girish Patil
"""


from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area_circle(self):
        return pi*(self.radius*self.radius)


print ("%f"%(Circle(12).area_circle()))