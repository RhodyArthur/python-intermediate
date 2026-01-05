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
    try:
        result = int(value)
    except ValueError:
        return "Wrong value passed"
    else:
        return result

def safe_list_access(lst, index):
    try:
        result = lst[index]
    except IndexError:
        return "Index out of range"
    else:
        return result
