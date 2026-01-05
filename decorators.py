# Task 7.1: Simple Decorators (5 points)
# Create these function decorators:
from time import time
from functools import wraps
def timer(func):
    """
    Decorator that prints execution time of function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f'Execution time of {func.__name__}: {elapsed:.4f} seconds')
        return result
    return wrapper
    
def logger(func):
    """
    Decorator that prints function name and arguments before execution
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

def validate_positive(func):
    """
    Decorator that ensures all numeric arguments are positive
    Raises ValueError if any argument is negative
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if (isinstance(arg, (int, float)) and arg < 0):
                raise ValueError(f"All arguments must be positve. Got {arg}")
            
        for value in kwargs.values():
            if (isinstance(value, (int, float)) and value < 0):
                raise ValueError(f"All arguments must be positve. Got {arg}")
        result = func(*args, **kwargs)
        return result
    return wrapper


# Test your decorators
@timer
@logger
def calculate_sum(a, b):
    return a + b

@validate_positive
def divide(a, b):
    return a / b