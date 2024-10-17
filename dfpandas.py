# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:48:35 2024

@author: argade om 
"""

###############################################
import pandas as pd
technologies ={
    "courses":["python","java","Hadoop","C++","C"],
    "fee":[200,300,400,500,600],
    "duration":["30 days","20 days","10 days","45 days","34 days",]
    }


df =pd.DataFrame(technologies)
#explicitely
df2=df.drop(lables=["fee"],axis=1)
df2

#alternatively
df2=df.drop(columns=["fee"],axis=1)
df2

#drop colums by index
print(df.drop(df.columns[1],axis=1))
df =pd.DataFrame(technologies)
#Drop column by inplace=true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

#########################################################
#Drop Two or More Colums by Index Name
df2=df.drop(["courses","fee"],axis=1)
print(df2)

#Drop Two or More Columns by Index
df =pd.DataFrame(technologies)

df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
####################################################
#Drop columns from list of columns
df= pd.DataFrame(technologies)
df.columns
lisCol =["courses","fee"]
df2=df.drop(lisCol,axis=1)
print(df2)

##########################################################
#Remove colums from dataframe inplace
df= pd.DataFrame(technologies)
df.drop(df.columns[1],axis =1,inplace=True)
df

# using inplace=True
##############################################
##############################################
##Pandas Select 
import pandas as pd
import numpy as np
technologies =({
    "courses":["Spark","PySpark","python","java","Hadoop","C++","C"],
    "fee":[22000,25000,23000,24000,np.nan,25000,25000],
    "duration":["30 days","20 days","10 days","45 days","34 days","67 days","80days"],
    "discount":[1000,20000,3000,4000,5000,6000,70000]
    
    
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df =pd.DataFrame(technologies,index=row_labels)
print(df)

##################################################33


df =pd.DataFrame(technologies,index=row_labels)
#below are quick example
df2=df.iloc[:,0:2]
df2
#this line uses the slicing operator to get dataframe 
#item by index
#the first slice [:] indicates to return all rows
#the second slice specicifies that only columns 
#between o and 2 (excluding 2 ) should be returned 
df2=df.iloc[0:2, :]
df2
#in case , the first slice [0,2] is 
#requesting only rows 0 through lof the datafarems 
#the second slice  [:] indicates that all colums are required
#slicing specific ROWS and Columns using iloc attribute 
df3=df.iloc[:,1:3]
df3

#The second operator [1:3] yields columns 1 and 3 only.
#Select Rows by Interger Index 
df2=df.iloc[2]     #select row by index
df2

#specific set of row if we want
 
df2 = df.iloc[[2,3,6]]      #select the rows by index no
df2 = df.iloc[1:5]         #integer index range 
df2 = df.iloc[:1]          #Select First Row
df2 = df.iloc[:3]          #select first 3 rows
df2 = df.iloc[-1:]         #select last row
df2 = df.iloc[-3:]         #select last 3 rows
df2 = df.iloc[::2]         #selects alternate rows
df2

#Select rows by index lables 
df2 =df.loc['r2']
df2
df2 =df.loc[['r2','r3','r6']]       #Select Rows by Index row
df2 =df.loc['r1':'r5']           #Select Rows by label row
df2 = df.loc['r1':'r5':2]  #Select Alternate Rows within 

#by using df[] notation
df2=df['courses']

#usinh loc[] to take columns slide
#loc sy
#Select multiple Columns 
df2 = df.loc[:,["courses","fee","duration"]]
#Select Random columns 

df2 = df.loc[:,["courses","fee","discount"]]
#select columns between 2 columns 
df2 = df.loc[:,'fee':'discount']
#Select column by range 
df2 =df.loc[:,'duration':]

#All columns upto duration
df2 = df.loc[:,:'duration']

##select every alternate columns 
df2 = df.loc[:,::2]
df2

#Pandas.Dataframe 
#Quer
df2=df.query("courses == 'Spark'" )
print(df2)

########################

#not equal condition
df2=df.query(" courses != 'Spark'")
df2




import pandas as pd
import numpy as np
technologies ={
    "courses":["Spark","PySpark","python","java","Hadoop","C++","C"],
    "fee":[22000,25000,23000,24000,np.nan,25000,25000],
    "discount":[1000,20000,3000,4000,5000,6000,70000]
    
    
    }

df =pd.DataFrame(technologies)
print(df)


#Pandas adda columns to Dataframe
#add new columns to the dataframe 

tutors=['Ram','Sham','Ghansham','Ganesh','Ramesh','sachin','bhagya']
df2 =df.assign(TutorsAssigned=tutors)
print(df)

#Adding multiple column to dataframe 

MNCCompanies =['TATA','HCL','GOOGLE','AMAZON','MICROSOFT','TCS','KOAS']
df2 = df.assign(MNC=MNCCompanies,tutors=tutors)
df2
#############################################
#DERIVIE NEW COLUMN FROM EXISTING COLUMN
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percentage=lambda x: x.fee * x.discount /100)
print(df2)

#Append  Column to existing dataframe 
df = pd.DataFrame(technologies)
df["MNCCompanies"]= MNCCompanies
print(df)

#add new column at the specific location 
df = pd.DataFrame(technologies)
df.insert(0, 'Tutors', tutors)
print(df)

#############################################################

import pandas as pd
import numpy as np
technologies ={
    "courses":["Spark","PySpark","python","java","Hadoop","C++","C"],
    "fee":[22000,25000,23000,24000,np.nan,25000,25000],
    "discount":[1000,20000,3000,4000,5000,6000,70000]
    }

df =pd.DataFrame(technologies)
df.columns
print(df.columns)

#Pandas  Rename Column name 
df2=df.rename(columns={'courses':'courses_list'})
print(df2.columns)

df.rename(columns={'courses':'courses_list','fee':'courses_fee','duration':'courses_duration'},inplace=True)