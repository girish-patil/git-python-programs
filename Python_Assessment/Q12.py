# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:51:37 2017

@author: Girish Patil
"""

#12.Take question 11 and implement logging on it and logging statement has to 
#be meaningful and should include entire details for easy tracking.



import logging

#Create and Configure Logger

LOG_FORMAT = "%(levelname)s  %(asctime)s - %(message)s"

logging.basicConfig(filename = "C:\\git-python-program\\Python_Assessment\\python_log.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

#to create logger object
logger = logging.getLogger()




def check_additive(s):
    logger.info("Function check_additive is called with parameter %s "%(s))
    
    i = 1
    a = int(s[0])
    b = int(s[i])
    logger.info("set first time value with a = %d & b = %d "%(a,b))
    
    # take as flag whether it is additive or not
    additive = True
    string_length = len(s)-1
    
    logger.info("start the loop untill the last index of string %d"%(string_length))
    while i < string_length:
        
        
        c = a + b        
        logger.info("we generated next value is c = %d"%(c))
        c = str(c)
        length = len(c)        
        d = int(c)
        logger.info("Now we set the values of a & b to next operation")
        #normal fibonacci logic ( follow up pointers)
        a = b
        b = int(s[i+1:i+length+1])
        
        logger.info("Now, value of a is %d & value of b is %d"%(a,b))
        

        
        if d == b:
            additive = True
        else:
            additive = False
            break
        
        logger.info("checking value of b and c are same or not")
        
        i = i+length
        logger.info("value of i is updated to get out of loop after complition with status of additive is %r"%(additive))
    

    
    return additive
    
    


s = raw_input("Enter String of numbers to check additive or not :-")
if len(s) != 1:
    if check_additive(s):
        print "Given String is additive"
    else:
        print "Given String is not additive"
else:
    print "please enter more than 1 element"