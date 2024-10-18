# Class methods

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.details = {}

    # Class method to create a Student from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['grade'])
    
    def display(self):
        # Populating details dictionary with phone number and address
        for i in range(2):
            phone_number = int(input(f"Enter the phone number @ {i+1}: "))
            home_address = input(f"Enter the Home Address of the student @ {i+1}: ")
            self.details[phone_number] = home_address
        
        return f"The details are: {self.name} : {self.age} : {self.grade} : {self.details}"
    
# Example usage:
student_dict = {
    'name': input("Enter the name of student: "),
    'age': int(input("Enter the age of the student: ")),
    'grade': int(input("Enter the class grade of the student: "))
}

# Creating a Student object from a dictionary using class method
student1 = Student.from_dict(student_dict)

# Displaying student details
print(student1.display())
