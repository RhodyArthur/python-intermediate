# Task 5.1: Basic Exception Handling (5 points)
# Create a calculator with proper exception handling:
# - `safe_divide(a, b)` - handles ZeroDivisionError
# - `safe_int_convert(value)` - handles ValueError
# - `safe_list_access(lst, index)` - handles IndexError
# - All functions should return a tuple: (success: bool, result/error_message)

def safe_divide(a, b):
    try:
        result = a / b
        return (True, result)
    except ZeroDivisionError:
        return (False, "Division by zero")

def safe_int_convert(value):
    try:
        result = int(value)
        return (True, result)
    except ValueError:
        return (False, f"Cannot convert {value} to integer")

def safe_list_access(lst, index):
    try:
        result = lst[index]
        return (True, result)
    except IndexError:
        return (False, "Index out of range")


#  Task 5.2: Custom Exceptions (8 points)
# Create a banking system with custom exceptions:

# Define these custom exceptions:
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class AccountNotFoundError(Exception):
    pass

# Create BankSystem class with these methods:
class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id, initial_balance):
        # Raise InvalidAmountError if initial_balance < 0
        if initial_balance < 0:
            raise InvalidAmountError("Initial amount must be positive")
        self.accounts[account_id] = initial_balance
            
    def deposit(self, account_id, amount):
        # Raise AccountNotFoundError if account doesn't exist
        # Raise InvalidAmountError if amount <= 0
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account does not exist")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.accounts[account_id] += amount 
        return self.accounts[account_id]
    
    def withdraw(self, account_id, amount):
        # Raise AccountNotFoundError if account doesn't exist
        # Raise InvalidAmountError if amount <= 0
        # Raise InsufficientFundsError if balance < amount
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account does not exist")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if self.accounts[account_id] < amount:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.accounts[account_id] -= amount
        return self.accounts[account_id]
    
    def get_balance(self, account_id):
        # Raise AccountNotFoundError if account doesn't exist
        if account_id not in self.accounts:
            raise AccountNotFoundError("Account not found")
        return self.accounts[account_id]
