Python-OOPs-Code
Employee Management System
This Python code defines an Employee class and a subclass Programmer to manage employees in a company. It demonstrates object-oriented principles such as inheritance, class methods, instance methods, and properties. The program also showcases the use of various Python features, including static methods, class methods, operator overloading, and email management using getters and setters.

Features
Employee Class: Models an employee with basic attributes like name and salary. Includes methods for increasing the salary, changing increment rates, and generating email addresses based on the name.
Programmer Class: Inherits from Employee and adds attributes for programming language and experience. It overrides the salary increment logic.
Class Methods: Used to create Employee objects from a string and to modify class-level attributes like the salary increment.
Static Methods: Determines if a place is open on a given day.
Operator Overloading: Allows adding two Employee objects by summing their salaries.
Properties: Manages the email attribute of an employee with custom setters and deleters for better control.
Code Explanation
Employee Class
The Employee class has the following attributes and methods:

Attributes:

fname: First name of the employee.
lname: Last name of the employee.
salary: The salary of the employee.
Increment: Class-level increment factor for salary adjustments (default is 2).
Methods:

increase(): Increases the employee's salary by the current increment factor.
from_str(): Class method that creates an employee instance from a hyphen-separated string (e.g., "John-Doe-50000").
change_increment(): Class method to change the global increment factor for all employees.
is_open(): Static method to check if a place is open based on the day of the week.
__add__(): Operator overloading for adding two Employee objects by summing their salaries.
__repr__() & __str__(): Custom string representations for printing employee details.
The email property automatically generates an email based on the first and last names, and the setter allows setting a custom email. The deleter removes the email and prints a message.

Programmer Class
The Programmer class inherits from Employee and adds the following:

Attributes:

proglang: Programming language expertise.
exp: Experience in years.
Methods:

increase(): Overrides the salary increase logic by adding an extra factor to the Increment.

Requirements
Python 3.x or higher.
