# multiple inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
        
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, date):
        # Explicitly call both Person and Employee constructors
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.date = date
        
    def __repr__(self):
        return f"This employee {self.name}, ID: {self.employee_id}, with salary {self.salary}, was hired on {self.date}."
    
    
# Input for manager details
name = input("Enter name of person: ")
age = int(input("Enter the age of person: "))
employee_id = int(input("Enter the employee ID: "))
salary = float(input("Enter the salary of the employee: "))
date = input("Enter the hiring date: ")

# Create a Manager instance
manager = Manager(name, age, employee_id, salary, date)

# Print manager details
print(manager)