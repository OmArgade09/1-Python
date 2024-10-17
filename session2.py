# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:15:12 2024

@author: Argade Om
"""


import pandas as pd
f1=pd.read_csv("C:/1-python/buzzers.csv")  #it is called as relative path
print(f1)

#################################################################
#checking for working directory
import os
with open("C:/1-python/buzzers.csv") as raw_data:      
    print(raw_data.read())
    
#####################################################################
#reading Csv data as lits 
#where we want the data in the from of list
import csv    
with  open('C:/1-python/buzzers.csv') as raw_data:  #its a absolute path
    for line in csv.reader(raw_data):
        print(line)
        
##################################################################
#when we want the data in the form of dictornory

import csv    
with  open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
    
    
    
############################################################
#wrongggg codeee
with open ('C:/1-python/buzzers.csv') as data:
  ignore=data.readline()
for line in data:
        flights=line.split.split()
print(flights)
    

##########################################################
#pre-requisite of decorators
def plus_one(number):
    number1=number +1
    return number1
plus_one(5)

"plus one value will be in the number "
"then the number +1 value will be stored in number1 and it will be printed"
###############################################################
#defining functions inside others functions'
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result = add_one(number)
    return result
plus_one(4)

####################################################
#passing function as argument
#to others functions
def plus_one(number):
    result1=number +1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

####################################################
#function returning other function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello=hello_function()
hello()

#####################################################

#Always remeber when u call hello_function() interview fav
import time
def calc_square(numbers):
    start=time.time()
    result= []
    for number in numbers:
        result.append(number*number)
        end=time.time()
        total_time=(end-start)*1000
        print(f"total time for execution square is { total_time }")
        return result
    
def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
        end=time.time()
        total_time=(end-start)*1000
        print(f"total time for execution cube is { total_time }")
        return result
        
    
array=range(1,10000)
out_square = calc_square(array) 
out_cube = calc_cube(array)  
     
###################################################################
#a python decorator is a function
#that takes in a function and returns it by adding some functionality
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper(): 
        func = function()
        make_uppercase= func.upper()
        return make_uppercase
    return wrapper 
decorator = uppercase_decorator(say_hi)
decorator()

#output HELLO THERE
###################################################################
'decorators are imp in interview perespective '
#for us to apply decorate
#we simply add the @symbol before the function we would like to dectorate 
def uppercase_decorator(function):
    def wrapper(): 
        func = function()
        make_uppercase= func.upper()
        return make_uppercase
    return wrapper 

@uppercase_decorator  
def say_hi():
    return 'hello boss'
say_hi()

##########################################################################

'applying multiple decorators'

#to a single function
#we can use multiple decorators to asingle function hpwever thr decorators will
#be apploied in the order 
#that we have called them


def split_string(function):                  #code to split string
    def wrapper():
        func = function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):              #code to make uppercase
    def wrapper(): 
        func = function()
        make_uppercase= func.upper()
        return make_uppercase
    return wrapper

    
@split_string                         #decorator  called  
@uppercase_decorator  
def say_hi():
    return 'hello boss'
say_hi()

#op  HELLO , BOSS

###################################################################
'interview **kwargs can ask what is it '
import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start =time.time()
        result =func(*args,**kwargs)
        end = time.time()
        total_time=(end-start)*1000
        print(func.__name__ +f"{total_time}mil sec")
        return result
    return wrapper

@time_it 
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
        return result
    
@time_it 
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
        return result
    
array = range(1,10000)
out_square = cal_square(array)
out_cube = cal_cube(array)


  
