# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:27:44 2017

@author: Girish Patil
"""

#10.Write a program to accept Date & Time in IST format and convert it to US format(EST).


import pytz
import datetime






gmt = pytz.timezone('GMT')
eastern = pytz.timezone('US/Eastern')

time = "Wed, 12 Oct 2017 10:40:20 GMT"

date = datetime.datetime.strptime(time, '%a, %d %b %Y %H:%M:%S GMT')

dategmt = gmt.localize(date)

dateeastern = dategmt.astimezone(eastern)
dateindian = dategmt.astimezone(gmt)

print "IST format (GMT): ",dateindian
print "US format(EST): ",dateeastern