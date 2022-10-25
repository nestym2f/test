"""
1-python is an interpreted language
means that is not have to be compiled like Ruby, PHP, JS 
2-python is dinamycally typed language
means you dont have to declare the return type of the function or variables
3-Module vs Package
The main difference between a module and a package in Python is that a module is a simple Python script
with a .py extension file that contains collections of functions and global variables while a package is 
a directory that contains a collection of modules, and this directory also contains an __init__.py file 
by which the interpreter interprets it as a package.
"""

#4-protected data member
_var2 = None
# private data member
__var3 = None

"""Single Underscore:
Single Underscore in Interpreter
Single Underscore after a name
Single Underscore before a name
Single underscore in numeric literals
Double Underscore:
Double underscore before a name
Double underscore before and after a name"""
#------------------------------------------------------------------------------
"""Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take 
some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create 
a static method in python.
When to use the class or static method?
We generally use the class method to create factory methods. Factory methods return class objects 
( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions."""

# Python program to demonstrate
# use of class method and static method.
from datetime import date
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

"""
Method resolution order in Python Inheritance MRO
Search of methods are first on the class and then on the parent class 
"""