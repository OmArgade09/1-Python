# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:42:48 2024

@author: argad
"""

"Python for datascince "
#Numpy
#its a popular open source pythonlibrary
"Numpy is basically used for image proccessing "

'''
python list can contain differrnt datatypes within a single list,
all of the elements in a Numpy array should be homogeneous 
'''
#Array In Numpy
# create np array
import numpy as np
arr = np.array([10,20,30])
print(arr)
####################################################################
#[]- single dimensinal array
#[[]]- two dimensinal array
#[[[]]]--Multidimenal  / three

#Multidimensional array
arr = np.array([[10,20,30],[10,20,30]])
print(arr)
'''
print(arr)
[[10 20 30]
 [10 20 30]]
'''
######################################################################
arr = np.array([10,20,30,40],ndmin = 3)
print(arr)

#print(arr)
#[[[10 20 30 40]]]

######################################################################
#chnage the data type 
#dtype parameter 

arr = np.array([10,20,30],dtype =complex)
print(arr)

#[10.+0.j 20.+0.j 30.+0.j]

#Get dimension of the array 
arr= np.array([[1,2,3,4],[7,8,9,10],[11,12,13,14]])
print(arr.ndim)
print(arr)

#print(arr.ndim)
#2
#print(arr)
#[[ 1  2  3  4]
 #[ 7  8  9 10]
 #[11 12 13 14]]
 
 #finding the size of each item in the array 
arr =np.array([10,20,30])
print("Each item is of the type", arr.dtype)

#get the shapwe and size of the array 
arr = np.array([[10,20,30,40],[50,60,70,80],[11,12,13,14]])
print("Array size :-",arr.size)
print("Array shape :-",arr.shape)
#Creating array from list with type float
arr = np.array([[1,2,3],[4,5,6]],dtype=float)
print(arr)
#####################################################################
#create a sequence of interger using arrange()
#create a sequence of integer
# from 0 to 20 with steps of 3 
arr= np.arrange(0,20,3)
print("A sequential array with steps of 3:\n", arr)

###################################################################
#Access single element using index
arr =np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])
#2
print(arr[-2])
#9

###################################################################
#Multidimensional array indexing 
#Acess multi dimensional array element 
#using array indexing 
arr =np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
#[[10 20 30 40 50]
 #[20 30 50 10 30]]
 
print(arr.shape)
 #(2, 5)
 
print(arr[1,1])
#30

print(arr[0,4]) 
#50
print(arr[1,-1])
#30

################################################################
#Acess array element using slicing
arr =np.array([0,1,2,3,4,5,6,7,8,9])
x =arr[1:8:2]
print(x)
# [1 3 5 7]
###############################################################
#example 
x=arr[-2:3:-1]
print(x)

#output [8 7 6 5 4]

#
x=arr[-2:10]
print(x)

#[8 9]
#Indexing in numpy
multi_arr=np.array([[10,20,30,40],[40,50,60,70],[60,70,80,90],
                    [30,90,40,30]])
multi_arr

#Slicing array 
#for multi-dimensional Numpy arrays,
#you can access the element as below

multi_arr [1,2]
multi_arr [1,:]
multi_arr [:,1]
 #columns from 0 to 3 in and  every alternate column 
x=multi_arr[:3,::2]
print(x)
#print(x)
#[[10 30]
# [40 60]
# [60 80]]
#integer array indexing 
arr=np.arange(35).reshape(5,7)
print(arr)


#print(arr)
#[[ 0  1  2  3  4  5  6]
 #[ 7  8  9 10 11 12 13]
 #[14 15 16 17 18 19 20]
 #[21 22 23 24 25 26 27]
 #[28 29 30 31 32 33 34]]
 
#############################################################

import numpy as np
#Boolean array indexing 
arr =np.arange(12).reshape(3, 4)
print(arr)

rows= np.array([False,True,True])
rows
wanted_rows= arr[rows,:]
print(wanted_rows)

'''print(wanted_rows)
[[ 4  5  6  7]
 [ 8  9 10 11]]'''

#Convertinh np array to list
list=[20,30,40,50]
array=np.asarray(list)
print("Array:-",array)
print(type(array))

#################################################################
#Numpy array prperties'
#mdarray.shape
#ndarray.nidm
#ndarray.itemsize
#ndarray.size
#ndarray.dtype 

#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

#Resize the array 
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)

#[[10 20]
# [30 40]
# [50r
#Numpy aslo provide a numpy
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)

#Arithmatic 
arr1=np.arange(16).reshape(4, 4)
arr2=np.array([1,2,3,4])

#add
add_arr=np.add(arr1,arr2)
print(f"adding two arrays:\n {add_arr}")


#sunstract
sub_arr=np.subtract(arr1,arr2)
print(f"Substracting two arrays:\n {sub_arr}")

#multiple
mul_arr=np.multiply(arr1,arr2)
print(f"multiply of array is :\n{mul_arr}")
'''
multiply of array is :
[[ 0  2  6 12]
 [ 4 10 18 28]
 [ 8 18 30 44]
 [12 26 42 60]]
'''

#divide()
div_arr=np.divide(arr1,arr2)
print(f"division of two array:\n {div_arr}")

'''
print(f"division of two array:\n {div_arr}")
division of two array:
 [[ 0.          0.5         0.66666667  0.75      ]
 [ 4.          2.5         2.          1.75      ]
 [ 8.          4.5         3.33333333  2.75      ]
 [12.          6.5         4.66666667  3.75      ]]
'''
#To perform Reciprocal operation 
arr1 =np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"after applying reciprocal function to array:\n{rep_arr1}")

arr1 =np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"after applying power function to array:\n{pow_arr1}")
####################################################################33

arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"after applying power function to array:\n{pow_arr2}")

#this function returnms the remainder of the division 
#numpy.reminder() also produces the same

import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2]) 
#mod fun
mod_arr =np.mod(arr1,arr2)
print(f"After applying mod function to array:\n{mod_arr}")

##########################################################################
#Create an empty array 
from numpy import empty
a = empty([3,3])
print(a)
#create a zwero arrays 

from numpy import zeros
a= zeros([3,5])
print(a)

print(np.__version__)

#create one array 
from numpy import ones 
a =ones([5])
print(a)
"[1. 1. 1. 1. 1.]"
#######################################################
#create array with v stack

from numpy import array 
from numpy import vstack

a1=array([1,2,3])
print(a1)
#create swecond array
a2= array([4,5,6])
print(a2)
#vertical stack 
a3=vstack((a1,a2))
print(a3)
print(a3.shape)

#########################################################################3
#craete array with  h stack 
from numpy import array 
from numpy import hstack

a1=array([1,2,3])
print(a1)
#create swecond array
a2= array([4,5,6])
print(a2)
#vertical stack 
a3=hstack((a1,a2))
print(a3)
print(a3.shape)