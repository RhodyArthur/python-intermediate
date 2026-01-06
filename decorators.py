# Task 7.1: Simple Decorators (5 points)
# Create these function decorators:
import time
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
                raise ValueError(f"All arguments must be positive. Got {arg}")
            
        for value in kwargs.values():
            if (isinstance(value, (int, float)) and value < 0):
                raise ValueError(f"All arguments must be positvie. Got {arg}")
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

print(calculate_sum(5,3))
print(divide(10,2))
# print(divide(-10,2))

# Task 7.2: Decorators with Arguments (5 points)
# Create decorators that accept arguments:

def repeat(times):
    """
    Decorator that repeats function execution
    @repeat(3)
    def greet(): ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
                return result
        return wrapper
    return decorator

def retry(max_attempts):
    """
    Decorator that retries function if it raises an exception
    @retry(3)
    def unstable_function(): ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                        if attempt == max_attempts:
                            raise
                        print(f"Attempt {attempt} failed: {e}. Retrying...")
            return None
        return wrapper
    return decorator


# Task 7.3: Class Decorator (5 points)
# Create a class that works as a decorator:

class CountCalls:
    """
    Decorator that counts how many times a function is called
    
    Usage:
        @CountCalls
        def my_func():
            pass
        
        my_func()
        my_func()
        print(my_func.call_count)  # 2
    """
    def __init__(self, func):
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)