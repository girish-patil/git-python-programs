# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:30:10 2017

@author: Girish Patil
"""

class list_operation:
    def __init__(self,li):
        self.li =li

    def append_list(self,value):
        self.li.append(value)
        return self.li

    def delete_from_list(self,value):
        self.li.remove(value)
        return self.li

    def display_list(self):
        print (self.li)


li = [1,2,3,4]
lio = list_operation(li)
lio.append_list(5)
lio.display_list()