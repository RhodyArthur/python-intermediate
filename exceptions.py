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

# Task 5.3: Exception Chain and Finally (7 points)
# Create a file processor with comprehensive error handling:

import json
class FileProcessor:
    def process_data_file(self, filename):
        """
        This method should:
        1. Open and read a JSON file
        2. Validate that it contains a 'data' key with a list
        3. Process each item (convert strings to uppercase)
        4. Write results to a new file
        5. Use try/except/else/finally appropriately
        6. Handle: FileNotFoundError, JSONDecodeError, KeyError
        7. Always close resources in finally block (or use context managers)
        8. Return success status and message
        """
        try:
            with open(filename) as f:
                content = json.load(f)
                
                if ('data' not in content or not isinstance(content['data'], list)):
                    raise KeyError('"data" must be a list')
                result = [str(item).upper() for item in content['data']]
            
            import os
            base_name = os.path.splitext(filename)[0]
            output_file = f'{base_name}_processed.json'

            with open(output_file, 'w') as f:
                json.dump({'data':result}, f, indent=4)

        except FileNotFoundError:
            return False, "File not found"
        except json.JSONDecodeError as e:
            return False, "Invalid JSON file"
        except KeyError as e:
            return (False, str(e))
        else:
            return (True, 'Result written successfully')
        finally:
            print('Processing completed')
            
    
    def batch_process_files(self, filenames):
        """
        Process multiple files and collect results
        Continue processing even if one file fails
        Return a summary of successes and failures
        """
        summary = []
        for filename in filenames:
            try:
                success, message = self.process_data_file(filename)
            except Exception as e:
                success = False
                message = f"Unexpected error: {e}"
            summary.append({
                'file': filename,
                "success": success,
                "message": message
            })
        return summary
