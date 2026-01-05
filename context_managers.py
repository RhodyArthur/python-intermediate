# Task 6.1: Using Built-in Context Managers (3 points)
# Demonstrate proper use of context managers:

def read_multiple_files(filenames):
    """
    Read multiple files using context managers
    Return a dictionary: {filename: content}
    Handle missing files gracefully
    """
    files  = {}
    for filename in filenames:
        try:
            with open(filename) as f:
                content = f.read()
                files[filename] = content

        except FileNotFoundError:
            files[filename] = None
    return files



def write_transaction_log(transactions):
    """
    Write transactions to a file using context manager
    Each transaction should be on a new line with timestamp
    """
    from datetime import datetime

    with open('transactions.log', 'a') as f:
        for transaction in transactions:
            timestamp = datetime.now().strftime('%Y-%m-%d - %H:%M:%S')
            f.write(f'{timestamp}-{transaction}\n')

#  Task 6.2: Class-based Context Manager (6 points)
# Create a `Timer` context manager as a class:
import time
class Timer:
    """
    Context manager that measures execution time
    
    Usage:
        with Timer("My Operation"):
            # code to time
        
    Should print: "My Operation took 1.23 seconds"
    """
    def __init__(self, name):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed = end_time - self.start_time
        print(f"{self.name} took {elapsed:.2f} seconds")
        if exc_type:
            print(f"Exception: {exc_val}")
        return False
    
# Task 6.3: Function-based Context Manager (6 points)
# Create context managers using `@contextmanager`:

from contextlib import contextmanager
import os
@contextmanager
def temporary_file(filename):
    """
    Context manager that creates a file on entry
    and deletes it on exit
    Yields the file handle for writing
    """
    file = None
    try:
        file = open(filename, 'w')
        yield file
    finally:
        if file:
            file.close()
        if os.path.exists(filename):
            os.remove(filename)

@contextmanager
def database_connection(db_name):
    """
    Simulates database connection
    Prints "Connected to {db_name}" on entry
    Prints "Disconnected from {db_name}" on exit
    Yields a mock connection object (can be a dict)
    """
    print(f"Connected to {db_name}")
    connection = {"database": db_name, "status": "connected"}
    try:
        yield connection
    finally:
        print(f"Disconnected from {db_name}")