#!/bin/python3 

#Importing the class in Employees.py
from Employees import Employees 

#Create a variable with the object filled for one employee
e1 = Employees("Bob", "Sales", "Director of Sales", 100000, 20)

#Create seconed employee
e2 = Employees("Linda", "Executive", "CIO", 150000, 10)

#return name, role, & eligible for the 2 specific employees
print(e1.name)
print(e2.role)
print(e1.eligible_for_retirement())

#Thank You TCM Security