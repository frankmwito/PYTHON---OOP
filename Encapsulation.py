# Encapsulation

class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
        
    # Getter method for balance
    def get_balance(self, account_number):
        if account_number == self.__account_number:  # Verify account number
            return f"{self.name}'s balance is {self.__balance}"
        else:
            return "Invalid account number"
    
    # Setter method for deposit
    def set_account_information(self, account_number):
        if account_number == self.__account_number:
            amount = float(input("Enter the amount you wish to deposit: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                self.__balance += amount
                print(f"New balance: {self.__balance}")
        else:
            print("Invalid account number")
            
# Creating an account
name = input("Enter your name: ")
account_number = input("Enter your account number: ")

account = Account(name, account_number)

# Get balance
print(account.get_balance(account_number))

# Deposit money
account.set_account_information(account_number)

                 