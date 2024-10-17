# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:08:33 2024

@author: argade om
"""

lst=[]
for num in range (0,20):
    lst.append(num)
print(lst)
    
    
    #list comprehension
    
lst=[num for num in range (0,20)]
print(lst)
    
    
    ####CAPTALISATION ##################
names=['dada','mama','kaka'] 
lst=[name.capitalize() for name in names]
print(lst)


#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

###########################################
#we need to write bussiness logic on left side and for loop on right side
lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)
####################################
#DICTIONORY COMPREHENSION

#IN DICTIO-- COMPRE WE WILL USE {} BRACKETS

dict={x:x*x for x in range(3)}
print(dict)

#################################################3
#Generator
#it is another way of creating iterators
#in a simple way where
#it uses the keyword "yeild"
#instead of returning it in a defined function
#generators are implemented using a function

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
    
    
    ###################
    
gen=(x 
     for x in range(3)
     )
next(gen)
next(gen)
#########################################

#function which return multipal values 
def range_even(end):
    for num in range(0,end,2):
        yield num
        #function  will return multiple values like list
for num  in range_even(6):
    print(num)
        
##############################################
#now instead of using for loop we will write our own code 
# the gen function is assigned above if we dont want to  use loops 
gen=range_even(6)   
next(gen)
next(gen)
    
#chaining generators
def lengths(itr):
  for ele in itr:
    yield len(ele)
    
def hide(itr):
  for ele in itr:
    yield ele*'*' 
  
    '''
    "ele*" appears to be a placeholder for an element
    from an iterable.the asterick(*) is likely
    just a character used to represent  a placeholder
    or a wildcard
    for instance,if youre iterating
    over a list of element,"ele*"
    could symbolize any element in that list
    its a generic representation
    that doesnt correspond to specific syntax in python or itertools
    
  '''
  
password=["om-123","om34556","okkk1123"]
for pas in hide(lengths(password)):
    print(pas)
  

# to take input from user,noun , objecctive , password 
def hide(pass1):
    yield pass1*'*'
noun=input("enter your name")
adj=input("enter the adjective")
special_character=input("enter any special character")
number=input("enter any number you want")
password=noun+adj+special_character+number
print(password)
for passw in hide(len(password)):
    print(passw)

###########################################################3
"after noon session data science    25-03-2024"
"------itertools ---------------------"

#Emnuerates in python
lst=["milk","egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
################################################################
#enmurate without using len
lst=["milk","egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
###################################################################### 
#USE of ZIP function

name=['dada','mama','kaka']
info=[9850,6032,9999]
for nm,inf in zip(name,info):
    print(nm,inf)
    #################################################
    
#USE of ZIP function WITH MIS MATCH LIST
name=['dada','mama','kaka','baba']
info=[9850,6032,9999]
for nm,inf in zip(name,info):
    print(nm,inf)
    
    #it will not display excess mismatch item in name
    #i.e baba
#########################

from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9999]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
    #####################################
    #use of fill value instead none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9999]
for nm,inf in zip_longest(name,info,fillvalue=0):
        print(nm,inf)

######################################
#use of all(),if all the values are 
#sture then it will produce output
#value must be non zero, positive or negavative 
lst=[2,3,-6,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')
############################################

lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')
    
#############################################################
#USE OF ANY IF ANY ONE ZERO VALUES
lst=[0,0,0,0,8,0]
if any(lst):
    print('its has some non zero value')
else:
    print('useless')

#use of any
lst=[0,0,0,0,0,0]
if any(lst):
    print('its has some non zero value')
else:
    print('all value are zero')
#########################################################

#count
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#it gives the count 

###################################################################
#NOW we want the COUNT from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

################################################
#cycle 
#suppose you have repeated tasks to be done ,then you
import itertools
instructions=("eat","code","sleep")
for instructions in itertools.cycle(instructions):
    print(instructions)

##############################################################

#repeat()
from itertools import repeat
for msg in repeat ("keep patience",times=3):
    print(msg)
#############################################################

#combinations()---------means selection
from itertools import combinations
players=['jhon','roman','brock','cody','finn']
for i in combinations(players,2):
    print(i)

##################################################################
#PERMUTATIONS-------arranging
from itertools import permutations
players=['jhon','roman','brock','cody','finn']
for seat in permutations(players,2):
    print(seat)

##################################################################

#product()

from itertools import product
team_a=['Rohit','pandya','Bumrah']
team_b=['virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)
 ###################################################################   
"interview fav shallow copy deep copy"
"In Python,assignment statements (obj_b =obj_a)"
#shallow copy and deep copy
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0] = -10
print(list_a)
print(list_b)

"SHALLOW COPY  ----- "
#SHALLOW COPY IS ONLY AFFLICABLE FOR 1 LEVEL DEEP
#import copy
#list_a =[1,2,3,4,5]
#list_b =list_a
#list_a[0]=-10
#
#print(list_a)
#print(list_b)


"we will use copy.copy(),ot object-specific function"
import copy
list_a =[1,2,3,4,5]
list_b=copy.copy(list_a)

list_b[0]=-10
print(list_a)
print(list_b)
#####################################################

#BUt with nested objects, modifying on level 2 or deep 
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affects the other 

list_a[0][0]=-10
print(list_a)
print(list_b)

#output 
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
###################################################################################

#DEEP COPIES  
#full INDEPENDENT CLONES .USE TO COPY.DEEPCOPY().
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#not affect the other 
list_a[0][0]=-10
print(list_a)
print(list_b)

#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

##############################################################

