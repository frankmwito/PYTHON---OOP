# static methods

class MathOperations:
    @staticmethod
    def sqrt(num):
        return num ** 0.5
 
num = float(input("Enter any number: "))   

result = MathOperations.sqrt(num)
print(f"The square root of {num} is {result}")