# function of pi
"""
Created on Tue Nov  8 13:43:14 2022

@author: ADMIN
"""
#NO RETURN WITHOUT ARGUMENT FUNCTION
'''def add():
    a=int(input('Enter the values of A:'))
    b=int(input('Enter the values of B:'))
    c=a+b
    print('Total',c)
add()
#NO RETURN WITH ARGUMENT FUNCTION
def sub(a,b):
    c=a-b
    print('Difference:',c)
sub(25,2)

#RETURN TYPE WITHOUT ARGUMENT FUNCTION
def mul():
    a=int(input('Enter the values of A:'))
    b=int(input('Enter the values of B:'))
    c=a*b
    return c
x=mul()
print('mul:',x)
'''
#RETURN TYPE WITH ARGUMENT FUNCTION
def div(a,b):
    c=a/b
    return c
x=div(25,2)
print('Division:',x)
# Arbitary argument function
def class_10(*students):
    print(students)
    for user in students:
        print(user)
class_10('ram','dev','ramya')
#keyword argument function
def message(name,age):
    print(name,"age is",age)
message(age=27,name='nava')
# Arbitary keyword argument function
def biodata(**data):
    print(data)
biodata(name="nava",age=27,gender="female")
# Default parameter function
def user(name,city="salem"):
    print(name,"is from",city)
user('ram','theni')
user('ram')
#passing a list as an argument in fun
def total(marks):
    return sum(marks)
print('Total:',total([75,85,68,95,82]))
#recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print('Factorial:',factorial(5))
#Lambda function
c=lambda a:a+50
print(c(5))
c=lambda a,b:a*b
print(c(10,20))
#date time fun 
import datetime as dt
current_date=dt.date.today()
print('current date:',current_date)
new=dt.date(2022,12,8)
print(new)
print('year:',new.year)
print('month:',new.month)
print('day:',new.day)
print('-------------------------------------------')
a=dt.time(10,45,5,55505)
print(a)
print('hour:',a.hour)
print('minute:',a.minute)
print('second:',a.second)
print('microsecond:',a.microsecond)
print('_________________________________________')
current_time=dt.datetime.now()
print('current time:',current_time)
print('--------------------------------')
new=dt.datetime(2022,11,21,9,46,58)
print(new)
print(new.date())
print(new.time())
print('--------------------------------')
current=dt.datetime.now()
new_year=dt.datetime(2023,1,1)
difference=new_year-current
print(difference)
print('--------------------------------')
current=dt.datetime.now()
print(current)
s=current.strftime('%A %B %d %Y')
print(s)
#math function
import math
print(math.sqrt(4))
print(math.ceil(1.555))
print(math.floor(1.555))
print(math.factorial(5))
print(math.fabs(-5))
print(math.pow(2,3))
print(math.log2(2))
print(math.log10(2))
print(math.cos(30))
print(math.pi)
print(math.e)
r=5
print(2*math.pi*r)



















