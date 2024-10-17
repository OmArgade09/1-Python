# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:50:21 2024

@author: argade om 
"""

import matplotlib.pyplot as plt 
X = range(1,50)
Y = [value*3 for value in X]
print("Values of X:")
print(*range(1,50))
'''
This is equivalent to i in range (1,50):
    print(i,end =' ')\
        
'''

print("Values of Y (thrice off X)") 
print(Y)
#Plot lines and/or markers to the Axes
plt.plot(X,Y)
#Set the x axis label of the current axis
plt.xlabel('X-axis')
#Set the y axis label of the current axes
plt.ylabel('Y-axis')
plt.title('draw a line ')
plt.show()
####################################################################3
import matplotlib.pyplot as plt
#x axis values 
x=[1,2,3]
#y axis
y=[2,4,1]
#Plot lines and/or markers to the Axes
plt.plot(x,y)
#Set the x axis label of the current axis
plt.xlabel('x-axis')
#Set the y axis label of the current axes
plt.ylabel('y-axis')
plt.title('draw a line')
plt.show()
##################################################################3
import matplotlib.pyplot as plt
#line 1 point
x1 = [10,20,30]
y1 = [20,30,40]


#line 2 point 
x2 =[10,20,30]
y2 =[40,10,30]

#ploting the line 1 points 
plt.plot(x1,y1,label="line1")
#
plt.plot(x2,y2,label='line2')
plt.xlabel('x-axis')
#set the y axis label of the current axis 
plt.ylabel('y-axis') 
#set the title 
plt.title("two or more ")

plt.legend()

plt.show()
######################################################################

import matplotlib.pyplot as plt
#line 1 point
x1 = [10,20,30]
y1 = [20,30,40]


#line 2 point 
x2 =[10,20,30]
y2 =[40,10,30]

plt.xlabel('x-axis')

plt.ylabel('y-axis')
#set a title 
plt.title("two or more ")
plt.legend()
plt.show()

################################################################3
import matplotlib.pyplot as plt 

# line 1 point
x1 = [10,20,30]
y1 = [20,30,10]

# line 2 point
x2 = [10,20,30]
y2 = [40,10,30]

# plotting the title 
plt.title("Plotting the two or more lines with different color and width ")
# plotting the line1 points 
plt.plot(x1,y1,color='blue',linewidth=3,label='line 1')
plt.xlabel('x - axis')
# plotting the line2 points
plt.plot(x2,y2,color='red',linewidth=5,label='line 2')
plt.ylabel('y - axis')

# Show the legend on the line
plt.legend()
##########################################################################3
#EdA is exploratory data analysis 
#Write a python program 
import matplotlib.pyplot as plt

x=[1,4,5,6,7]
y=[2,6,3,6,3]

plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)

#set the y-limits of the current axes
plt.ylim(1,8)
#set the x limits of the current axes
plt.xlim(1,8)
#naming the x axis 
plt.xlabel('x-axis')
#naming the y axis 
plt.ylabel('y-axis')

#giving title of my graph 
plt.title('display marker')
#function to show plot
plt.show()

################################################################################
"QUCICK REFERNCE CODE"

#write a python program to display 
#a bar grph
import matplotlib.pyplot as plt 
x=['java','python','c','c++','PHP','javascript']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming Language \n "+" worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################3#########################3

import matplotlib.pyplot as plt 
x=['java','python','c','c++','PHP','javascript']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='green')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming Language \n "+" worldwide, oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
#Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

################################################################################33
#Write a python programming to display
#default colors 

import matplotlib.pyplot as plt 
x=['java','python','c','c++','PHP','javascript']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming Language \n "+" worldwide, oct 2017 compared to a year ago")
plt.yticks(x_pos,x)
#Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##############################################3##############\
    
import matplotlib.pyplot as plt 
x=['java','python','c','c++','PHP','javascript']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['red','yellow','blue','purple','black','orange'])
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("popularity of programming Language \n "+" worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#########################################################################
#histogram 
#it is imp to undestand 
#whether ur data is concemtarted to mean or distributed 
import matplotlib.pyplot as plt 
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8)
plt.hist(blood_sugar, rwidth=0.5,bins=4)


'''HIStogram showing normal,pre-diabetic patiensts distribution
'80-100 Normal'
'100-125 Prediabetic'
'125 onwards Diabetics'
'''
plt.xlabel("Sugar level")
plt.ylabel("Number of patients")
plt.title("Blood sugar chart")
plt.hist(blood_sugar,bins=[80,100,125,150], rwidth=0.95,color='blue')

###################plt#########################################################
#BOX PLOT

import matplotlib.pyplot as plt
import numpy as np
#Creatingh= dataset 

np.random.seed(10)
data = np.random.normal(100,20,200)

fig=plt.figure(figsize =(10, 7))
#Creating plot
plt.boxplot(data)
#show plot
plt.show()

#######################################################################
#hoe to plot multiple box plot
import matplotlib.pyplot as plt 
import numpy as np
#Creating  dataset
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(100,10,200)
data_3=np.random.normal(100,10,200)
data_4=np.random.normal(100,10,200)

fig = plt.figure(figsize =(10,7))

#Creating axes instancee
ax= fig.add_axes([0,0,1,1])
#Creating plot
bp= ax.boxplot(data)
#show plot
plt.show()


###############################################
import seaborn as sns 
import pandas as pd 
cars=pd.read_csv("C:/1-python/Cars.csv.xls")
cars.head()
cars.columns

sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')

#####################################################
sns.catplot(x='HP',y='MPG',data=cars,kind='box')

#Histogram 
sns.distplot(cars.HP)
##########################################################
#multiple correlation regression anaylsis
import pandas as pd 
import numpy as np
import seaborn as sns
cars=pd.read_csv("C:/1-python/Cars.csv.xls")
#Exploartory data anaylsis
#1Measure the central analysis
#2 Measure the central tendency 
# 4 Fourth moment business decision 
#5 probability  distribution 
#6 Graphical represntation 
cars.describe()
#Graphical representation
import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)












