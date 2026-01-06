# Task 8.1: Generator Functions (5 points)
# Create these generators:

def even_numbers(n):
    """
    Generator that yields first n even numbers
    """
    count = 0
    num = 2
    while count < n:
        yield num
        num += 2
        count += 1

def fibonacci_generator(n):
    """
    Generator that yields first n Fibonacci numbers
    """
    pass

def file_line_generator(filename):
    """
    Generator that yields lines from a file one at a time
    Strips whitespace from each line
    """
    pass