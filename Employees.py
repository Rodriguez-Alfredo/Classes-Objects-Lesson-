#!/bin/python3
#Class is an object instructer - create objects
#python is an obect oriented language

#Create class an give a a name
class Employees:

  #defining the object ex(.name = name)
	def __init__(self, name, department, role, salary, years_employed):
		self.name = name
		self.department = department
		self.role = role
		self.salary = salary
		self.years_employed = years_employed

  #discover if they are eligible for retirement
	def eligible_for_retirement(self): 

    #Identify 20 or greater is eligible
		if self.years_employed >= 20:
			return True

    #Not eligible
		else:
			return False
			
#all classes has the init funciton - used when class is being initiated 

#Thank You TCM Security
