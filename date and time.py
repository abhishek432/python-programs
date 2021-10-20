import datetime

#for date---
"""
date_obj=datetime.date.today()
print(date_obj)
"""
#for both time and time--
"""
time_obj=datetime.datetime.now()
print(time_obj)

"""
#what inside date and time---
"""
print(dir(datetime))
"""
#todays year,month and day--
"""
from datetime import date
today=date.today()
print('current year: ',today.year)
print('current month: ',today.month)
print('current day: ',today.day)
"""

#Diffrence between two dates--
"""
from datetime import date
t1=date(year=2001,month=9,day=16)
t2=date(year=2021,month=9,day=17)
t3=t2-t1
print(t3)
"""
#Diffrence between two dates and time--
"""
from datetime import datetime,date
t4=datetime(year=2001,month=9,day=16,hour=8,minute=10,second=20)
t5=datetime(year=2021,month=9,day=17,hour=4,minute=20,second=20)
t6=t5-t4
print(t6)
"""
#print day name----
"""
import datetime
x=datetime.datetime.now()

print(x.strftime("%A"))#for full weekday name
print(x.strftime("%a"))#for short weekday name
print(x.strftime("%w"))#weekday no in month
print(x.strftime("%d"))#for date of month
print(x.strftime("%b"))#month name in short
print(x.strftime("%B"))#month name full
print(x.strftime("%y"))#year short version
print(x.strftime("%Y"))#year full version
print(x.strftime("%H"))#24 hour format
print(x.strftime("%M"))#print minutes
print(x.strftime("%S"))#print second
print(x.strftime("%p"))#print AM or PM
print(x.strftime("%j"))#print day no in year
print(x.strftime("%U"))#week no in year

"""















