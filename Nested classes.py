# Nested classes

class University:
    def __init__(self, university_name):
        self.university_name = university_name
        
    # Nested class Department
    class Department:
        def __init__(self, department_name, num_of_students):
            self.department_name = department_name
            self.num_of_students = num_of_students
        
        def display_department_info(self):
            return f"Department: {self.department_name}, Number of Students: {self.num_of_students}"
    
    def display_university_info(self):
        return f"University: {self.university_name}"
    
# Create an instance of the outer class (University)
uni = University("Tech University")

# Create an instance of the nested class (Department)
dept = University.Department("Computer Science", 250)

# Accessing methods from the outer class and the nested class
print(uni.display_university_info())
print(dept.display_department_info())
