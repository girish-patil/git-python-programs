# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

var = input('Enter Marks:')
if var<100:
    if var >= 40 and var < 50:
        print 'Grade D'
    elif var >=50 and var <60:
        print 'Grade C'
    elif var >=60 and var <70:
        print 'Grade B'
    elif var >=70 and var < 90:
        print 'Grade A'
    elif var >= 90:
        print 'Grade A+'
    else:
        print 'Fail'
else:
    print 'invalid marks'