# Custom exception class

class InvalidAgeError(Exception):
    """Custom exception class for invalid age"""
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be 18 or above to register for voting.")
        self.age  = age
        
def register_for_voting(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print(f"User with age {age} is eligible for voting")
        
        

try:
    register_for_voting(int(input("Enter your age: ")))
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError as ve:
    print(f"Error: {ve}")