# Task 7.1: Simple Decorators (5 points)
# Create these function decorators:
from time import time

def timer(func):
    """
    Decorator that prints execution time of function
    """
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed = end_time - start_time
        print(f'Execution time of function: {elapsed}')
    return wrapper
    
def logger(func):
    """
    Decorator that prints function name and arguments before execution
    """
    pass

def validate_positive(func):
    """
    Decorator that ensures all numeric arguments are positive
    Raises ValueError if any argument is negative
    """
    pass

# Test your decorators
@timer
@logger
def calculate_sum(a, b):
    return a + b

@validate_positive
def divide(a, b):
    return a / b