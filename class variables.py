# class variables

class Employee:
    # Class variables
    num_of_employees = 0  # Track the number of employees
    employment_year = 2024
    
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.num_of_employees += 1  # Accessing class variable via class name

# Create Employee instances
name1 = input("Enter the name of the first employee: ")
age1 = int(input("Enter the age of the first employee: "))
employee1 = Employee(name1, age1)

name2 = input("Enter the name of the second employee: ")
age2 = int(input("Enter the age of the second employee: "))
employee2 = Employee(name2, age2)

name3 = input("Enter the name of the third employee: ")
age3 = int(input("Enter the age of the third employee: "))
employee3 = Employee(name3, age3)

# Print the total number of employees
print(f"Total number of employees: {Employee.num_of_employees}")

# Print employee details
print(f"Employee 1: Name = {employee1.name}, Age = {employee1.age}")
print(f"Employee 2: Name = {employee2.name}, Age = {employee2.age}")
print(f"Employee 3: Name = {employee3.name}, Age = {employee3.age}")
