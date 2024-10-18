# Method Overloading using default arguments

class Calculator:
    def calculate(self, *args):
        sum = 0
        for num in args:
            sum += num
        print(f"The sum is: {sum}")
        return sum
        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

calculate1 = Calculator()
print(calculate1.calculate(num1, num2, num3))
