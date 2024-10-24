# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:24:06 2024

@author:  omargade
"""

#interview 
import pandas as pd
f1=pd.read_csv("C:/1-python/buzzers.csv")
print(f1)

################################################
#checking for working directory
import os
with open("C:/1-python/buzzers.csv") as raw_data:
    print(raw_data.read())

################################################
#reading CSV Data As lists
import csv
with open('C:/1-python/buzzers.csv') as raw_data:    
   for line in csv.reader(raw_data):
       print(line)
################################################
#Reading csv file as dictionary
import csv
with open("buzzers.csv") as raw_data:    
   for line in csv.DictReader(raw_data):
       print(line)
       

################################################
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)

################################################
#defining function inside another function

def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    result = add_one(number)
    return result
plus_one(4)

################################################
#passing function as argument to other function

def plus_one(number):
    result1 = number +1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

################################################
#functions returning other function

def hello_function():
    def say_hi():
        return "hi"
    return say_hi
hello=hello_function()
hello()     #object of function

################################################

#interview need for decorators
#decorators are like function for they are used for another mechanism

import time
def calc_square(numbers):
    start=time.time() #starting time
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time() #ending of time
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time required for execution cube is{total_time}")
    return result

array =range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

################################################

def say_hi():
    return "hello there"

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()

################################################

# we simply write @ symbol before we had  like to decorate.

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return "hello there"
say_hi()

################################################

#applying multiple decorators
#to a single function
#however the decorator are applied in order to we've called them
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
    
@split_string
@uppercase_decorator
def say_hi():
    return "hello there"
say_hi()

################################################
#key word arguments
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took{total_time}mil sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)
