# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:31:22 2024

@author: Argade Om
"""
"#Expection handeling using try and "
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("DIVISION DONE SUCCESSFULLY")
except ZeroDivisionError:
   print("oh this is divide by zero error..")
print("outside try and catch block")

#######################################################
#below code here we are giving float value so it should give
# an only interger value allowed 
#sometimes A single piece of code might be suspected to have more than
#one type of error.for handling such stituations ,we can have multiple except
#blocks for a single try block
    
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("DIVISION DONE SUCCESSFULLY")
except ZeroDivisionError:
   print(" denom zero not allowed")
except ValueError:
    print("only intergers are allowed")  
    
  
##########################################################333
#Handling exception without knowing them 

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("DIVISION DONE SUCCESFULLY")
except ValueError:
    print("only int should be entered")
except:
    print("oopss something went wrong")
    
########################################################
#Handling exception using try , except , else 
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("DIVISION DONE SUCCESFULLY")
except ZeroDivisionError:
   print(" denom zero not allowed")
except ValueError:
    print("only int should be entered")
else:
    print("the result of operation is ",quotient)
    
###############################################################

try:
    numerator=50
    denom=int(input("enter the denomninator"))
    quotient=(numerator/denom)
    print("division performed successfully")
except ZeroDivisionError:
    print ("Denominator should be not zero")
except ValueError:
    print("only integers sholud be entered")
else:
    print("the result of division op is",quotient)
finally:
    print("over and out")
    
###############################################################
