# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:15:33 2024

@author: argade  om 

"""
class Human:
    def __init__(self,n,o):  #CONSTRUCTOR
        self.name= n
        self.occupation = o
    def do_work(self):
      if self.occupation == "tennis player":
        print(self.name,"plays tennis")
      elif self.occupation =="actor":
        print(self.name,"shoots flims")
    def speaks(self):
        print(self.name,"says how are you")
    
tom = Human("tom_criuise","actor")
tom.do_work()
tom.speaks()

"INHERITANCE CONCEPTS BELOW"

#INHERITANCE EXAMPLE 
class Vehicle:
    def general_usage(self):
        print("general use:transporation")
        
class Car(Vehicle):
    def __init__(self):
        print("I AM A CAR")
        self.wheels=4
        self.has_roof =True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:commute to work , vacation with family")
        
class Motorcycle(Vehicle):
    def __init__(self):
        print("I AM A Bike")
        self.wheels=2
        self.has_roof =False
        
    def specific_usage(self):
        self.general_usage()
        print("specific use:commute to work , RACING")
        
c =Car()
m =Motorcycle()
c.specific_usage()
m.specific_usage()
              
####################################################################

"MULTIPLE INHERITANCE"

class Father():
    def skills(self):
        print("i like to ride the bikes")
        
class Mother():
    def skills(self):
        print("i like to make food and arts ")
        
class Child():
    def skills(self):
        Father.skills(self)      
        Mother.skills(self)
        print("i like thar")
        
c=Child()
c.skills()
   
"ADVANCE PYTHON FINIHED HERE"     
################################################################