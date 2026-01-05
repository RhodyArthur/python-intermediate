# Task 5.1: Basic Exception Handling (5 points)
# Create a calculator with proper exception handling:
# - `safe_divide(a, b)` - handles ZeroDivisionError
# - `safe_int_convert(value)` - handles ValueError
# - `safe_list_access(lst, index)` - handles IndexError
# - All functions should return a tuple: (success: bool, result/error_message)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero"
    else:
        return result

def safe_int_convert(value):
    # Your code here
    pass

def safe_list_access(lst, index):
    # Your code here
    pass