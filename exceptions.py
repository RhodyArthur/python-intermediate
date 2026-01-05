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

