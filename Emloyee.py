class Employee:
    
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.Increment = 2  # Instance-level Increment, can be overridden for each object
        #self.email = fname + lname + '@email.com'

    def increase(self):
        self.salary = int(self.salary * self.Increment)

    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, int(salary))  # Convert salary to int
    
    @classmethod
    def change_increment(cls, amount):
        cls.Increment = amount  # Change class-level Increment attribute

    @staticmethod
    def is_open(day):
        # Determines if a place is open based on the day
        if day == "Sunday":
            return False
        else:
            return True

    def __add__(self, other):
        # Add the salary of two Employee objects (or Programmer objects)
        return self.salary + other.salary

    def __repr__(self):
        # Custom string representation for Employee
        return 'Employee ({},{},{})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        # Custom string representation of Employee
        return 'The Name of the Employee is {} {}'.format(self.fname,self.lname)

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return 'Email not set'
        else:
            return self.fname + '.' + self.lname + '@email.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        print("Email address deleted")
        self.fname = None
        self.lname = None


# Creating Employee objects
harsh = Employee('Harsh', 'Kumar', 50000)
aman = Employee('Aman', 'Patel', 25000)

# Creating an Employee object from a string using the class method
shivam = Employee.from_str("Shivam-Kharwar-30000")

# Printing names and salaries of all employees
print(harsh.fname, '=', harsh.salary, aman.fname, '=', aman.salary)

# Increasing salaries
aman.increase()
print(harsh.salary, aman.salary)

# Printing salary of shivam
print(shivam.salary)

# Changing increment value
Employee.change_increment(3)  # This will affect all instances
harsh.increase()
print(harsh.salary)

# Checking if the place is open
print(Employee.is_open('Sunday'))  # It's better to call a static method using the class name
print(shivam.is_open('Monday'))   # Static method can also be called using the instance, but using class name is preferred


# Programmer class inherits from Employee
class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        # Increase the salary by adding a 0.2 factor to the Increment
        self.salary = int(self.salary * (self.Increment + 0.2))
        return self.salary

# Creating a Programmer object
amol = Programmer('Amol', 'Gond', 20000, 'java', '2 yrs')
print(amol.salary)

# Increasing salary of amol
print(amol.increase())

# Printing representation of harsh
print(repr(harsh))

# Testing the addition of salaries of harsh and aman
print(harsh + aman)

# Printing the custom string representation of harsh
print(harsh)
print(str(aman))

if __name__ == '__main__':
    harsh = Employee('Harsh', 'Kumar', 100000)
    aman = Employee('Aman', 'Patel', 75000)
    amol.lname = 'God'  # Modify last name for the amol instance

    # Print emails of employees
    print(harsh.email, '/', aman.email)  # Should output emails for harsh and aman
    
    # Setting a new email for Amol
    amol.email = 'God.Amol@email.com'  # Set new email with valid format
    print(amol.email)  # Should print "God.Amol@email.com"

    # Deleting email for amol
    del amol.email
    print(amol.email)  # Should print 'Email not set' because fname and lname are now None
