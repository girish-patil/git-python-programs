# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:35:20 2017

@author: Girish Patil
"""

#20. Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class 
# and "Female" for Female class.


# Parent class
class Person:
    def getGender(self):
        pass
        
#Child class of Person Class
class Male(Person):
    def getGender(self):
        print "Male"
        
#Child class of Person class
class Female(Person):
    def getGender(self):
        print "Female"
        
        
def main():    
    Male().getGender()
    Female().getGender()
    
    
if __name__ == "__main__":
    main()