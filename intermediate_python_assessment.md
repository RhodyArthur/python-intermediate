# Intermediate Python Assessment - Weeks 3-4

**Total Points: 150 (140 base + 10 bonus)**

**Time Limit: 4-5 hours**

**Instructions:**
- Complete all tasks in Python file(s)
- Test your code to ensure it works correctly
- Create actual files for file I/O operations
- Don't use external libraries except where specified (csv, json)
- Focus on proper OOP principles and error handling

---

## SECTION 1: Object-Oriented Programming - Classes & Objects (20 points)

### Task 1.1: Basic Class Implementation (5 points)
Create a `Book` class with the following:
- Attributes: `title`, `author`, `pages`, `price`
- Method `get_info()` that returns a formatted string with all book details
- Method `apply_discount(percentage)` that reduces the price by the given percentage
- `__str__` method that returns a readable representation

```python
class Book:
    # Your code here
    pass

# Test your class
book = Book("Python Mastery", "John Doe", 350, 29.99)
print(book.get_info())
book.apply_discount(10)
print(book)
```

### Task 1.2: Class and Instance Variables (5 points)
Create a `BankAccount` class with:
- Class variable `bank_name = "MyBank"`
- Class variable `total_accounts` that tracks the number of accounts created
- Instance variables: `account_number`, `owner`, `balance`
- Method `deposit(amount)` that adds to balance
- Method `withdraw(amount)` that subtracts from balance (don't allow overdraft)
- Class method `get_bank_info()` that returns bank name and total accounts

```python
class BankAccount:
    # Your code here
    pass
```

### Task 1.3: Static Methods (5 points)
Create a `MathHelper` class with static methods:
- `is_even(number)` - returns True if number is even
- `is_prime(number)` - returns True if number is prime
- `factorial(n)` - returns factorial of n
- `fibonacci(n)` - returns the nth Fibonacci number

```python
class MathHelper:
    # Your code here
    pass

# Test
print(MathHelper.is_prime(17))  # True
print(MathHelper.factorial(5))   # 120
```

### Task 1.4: Magic Methods (5 points)
Create a `Product` class with:
- Attributes: `name`, `price`, `quantity`
- `__str__` method for readable representation
- `__repr__` method for detailed representation
- `__eq__` method to compare products by name
- `__lt__` method to compare products by price (for sorting)

```python
class Product:
    # Your code here
    pass

# Test
p1 = Product("Laptop", 999.99, 5)
p2 = Product("Mouse", 29.99, 10)
print(p1 < p2)  # False (comparing price)
```

---

## SECTION 2: Inheritance & Polymorphism (20 points)

### Task 2.1: Single Inheritance (6 points)
Create a base class `Vehicle` with:
- Attributes: `brand`, `model`, `year`
- Method `get_info()` that returns vehicle information
- Method `start_engine()` that returns "Engine started"

Create two child classes:
- `Car` that adds `doors` attribute and overrides `start_engine()` to return "Car engine started"
- `Motorcycle` that adds `engine_cc` attribute and overrides `start_engine()` to return "Motorcycle engine started"

```python
class Vehicle:
    # Your code here
    pass

class Car(Vehicle):
    # Your code here
    pass

class Motorcycle(Vehicle):
    # Your code here
    pass
```

### Task 2.2: Using super() (5 points)
Create an `Employee` base class with:
- Attributes: `name`, `employee_id`, `base_salary`
- Method `calculate_salary()` that returns base_salary

Create a `Manager` child class that:
- Adds `team_size` attribute
- Overrides `calculate_salary()` to add bonus (base_salary + team_size * 1000)
- Uses `super()` to call parent's `__init__`

```python
class Employee:
    # Your code here
    pass

class Manager(Employee):
    # Your code here
    pass
```

### Task 2.3: Abstract Shape Hierarchy (9 points)
Create an abstract base class `Shape` with:
- Abstract method `area()`
- Abstract method `perimeter()`

Create three concrete classes:
- `Circle` with radius
- `Rectangle` with length and width
- `Triangle` with three sides

Each should implement the abstract methods correctly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    # Your code here
    pass

class Circle(Shape):
    # Your code here
    pass

class Rectangle(Shape):
    # Your code here
    pass

class Triangle(Shape):
    # Your code here - use Heron's formula for area
    pass
```

---

## SECTION 3: Encapsulation & Properties (15 points)

### Task 3.1: Private Attributes (5 points)
Create a `User` class with:
- Private attribute `__password`
- Public attribute `username`
- Method `set_password(password)` that only accepts passwords with 8+ characters
- Method `check_password(password)` that returns True if password matches
- Don't allow direct access to `__password`

```python
class User:
    # Your code here
    pass

# Test
user = User("alice")
user.set_password("secret123")
print(user.check_password("secret123"))  # True
print(user.check_password("wrong"))       # False
```

### Task 3.2: Property Decorators (5 points)
Create a `Temperature` class with:
- Private attribute `_celsius`
- Property `celsius` with getter and setter (setter validates value >= -273.15)
- Property `fahrenheit` with getter and setter (converts to/from celsius)
- Property `kelvin` with getter (read-only, converts from celsius)

```python
class Temperature:
    # Your code here
    pass

# Test
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0
temp.fahrenheit = 32
print(temp.celsius)      # 0
```

### Task 3.3: Full Encapsulation Example (5 points)
Create a `BankAccountSecure` class with:
- Private attributes: `__account_number`, `__balance`, `__pin`
- Properties for account_number (read-only) and balance (read-only)
- Method `deposit(amount, pin)` that adds to balance if pin is correct
- Method `withdraw(amount, pin)` that subtracts if pin is correct and sufficient funds
- Method `change_pin(old_pin, new_pin)` that changes pin if old_pin is correct

```python
class BankAccountSecure:
    # Your code here
    pass
```

---

## SECTION 4: File Operations (20 points)

### Task 4.1: Text File Operations (5 points)
Write functions to:
- `write_log(filename, message)` - appends a timestamped message to a log file
- `read_log(filename)` - returns all log entries as a list
- `count_words_in_file(filename)` - returns a dictionary of word frequencies
- Use context managers for all file operations

```python
from datetime import datetime

def write_log(filename, message):
    # Your code here
    pass

def read_log(filename):
    # Your code here
    pass

def count_words_in_file(filename):
    # Your code here
    pass
```

### Task 4.2: CSV Operations (5 points)
Create a student management system with CSV:
- `save_students_csv(filename, students)` - saves list of student dicts to CSV
- `load_students_csv(filename)` - loads students from CSV and returns list of dicts
- `add_student_csv(filename, student)` - appends a new student to existing CSV
- `find_student_by_id(filename, student_id)` - finds and returns student dict

Student dict format: `{'id': 1, 'name': 'Alice', 'age': 20, 'grade': 'A'}`

```python
import csv

def save_students_csv(filename, students):
    # Your code here
    pass

def load_students_csv(filename):
    # Your code here
    pass

def add_student_csv(filename, student):
    # Your code here
    pass

def find_student_by_id(filename, student_id):
    # Your code here
    pass
```

### Task 4.3: JSON Operations (5 points)
Create a configuration manager:
- `save_config(filename, config_dict)` - saves configuration to JSON with nice formatting
- `load_config(filename)` - loads and returns configuration dict
- `update_config(filename, key, value)` - updates a specific key in the config
- `get_config_value(filename, key, default=None)` - gets a value or returns default

```python
import json

def save_config(filename, config_dict):
    # Your code here
    pass

def load_config(filename):
    # Your code here
    pass

def update_config(filename, key, value):
    # Your code here
    pass

def get_config_value(filename, key, default=None):
    # Your code here
    pass
```

### Task 4.4: File Operations with Error Handling (5 points)
Create a robust file reader:
- `safe_read_file(filename)` - reads file content, handles FileNotFoundError
- `safe_write_file(filename, content)` - writes content, handles PermissionError
- `copy_file(source, destination)` - copies file with proper error handling
- All functions should return appropriate messages on success/failure

```python
def safe_read_file(filename):
    # Your code here - return (success: bool, content/error: str)
    pass

def safe_write_file(filename, content):
    # Your code here - return (success: bool, message: str)
    pass

def copy_file(source, destination):
    # Your code here - return (success: bool, message: str)
    pass
```

---

## SECTION 5: Exception Handling (20 points)

### Task 5.1: Basic Exception Handling (5 points)
Create a calculator with proper exception handling:
- `safe_divide(a, b)` - handles ZeroDivisionError
- `safe_int_convert(value)` - handles ValueError
- `safe_list_access(lst, index)` - handles IndexError
- All functions should return a tuple: (success: bool, result/error_message)

```python
def safe_divide(a, b):
    # Your code here
    pass

def safe_int_convert(value):
    # Your code here
    pass

def safe_list_access(lst, index):
    # Your code here
    pass
```

### Task 5.2: Custom Exceptions (8 points)
Create a banking system with custom exceptions:

```python
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
        pass
    
    def deposit(self, account_id, amount):
        # Raise AccountNotFoundError if account doesn't exist
        # Raise InvalidAmountError if amount <= 0
        pass
    
    def withdraw(self, account_id, amount):
        # Raise AccountNotFoundError if account doesn't exist
        # Raise InvalidAmountError if amount <= 0
        # Raise InsufficientFundsError if balance < amount
        pass
    
    def get_balance(self, account_id):
        # Raise AccountNotFoundError if account doesn't exist
        pass
```

### Task 5.3: Exception Chain and Finally (7 points)
Create a file processor with comprehensive error handling:

```python
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
        pass
    
    def batch_process_files(self, filenames):
        """
        Process multiple files and collect results
        Continue processing even if one file fails
        Return a summary of successes and failures
        """
        pass
```

---

## SECTION 6: Context Managers (15 points)

### Task 6.1: Using Built-in Context Managers (3 points)
Demonstrate proper use of context managers:

```python
def read_multiple_files(filenames):
    """
    Read multiple files using context managers
    Return a dictionary: {filename: content}
    Handle missing files gracefully
    """
    pass

def write_transaction_log(transactions):
    """
    Write transactions to a file using context manager
    Each transaction should be on a new line with timestamp
    """
    pass
```

### Task 6.2: Class-based Context Manager (6 points)
Create a `Timer` context manager as a class:

```python
class Timer:
    """
    Context manager that measures execution time
    
    Usage:
        with Timer("My Operation"):
            # code to time
        
    Should print: "My Operation took 1.23 seconds"
    """
    def __init__(self, name):
        # Your code here
        pass
    
    def __enter__(self):
        # Your code here
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Your code here
        pass
```

### Task 6.3: Function-based Context Manager (6 points)
Create context managers using `@contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def temporary_file(filename):
    """
    Context manager that creates a file on entry
    and deletes it on exit
    Yields the file handle for writing
    """
    pass

@contextmanager
def database_connection(db_name):
    """
    Simulates database connection
    Prints "Connected to {db_name}" on entry
    Prints "Disconnected from {db_name}" on exit
    Yields a mock connection object (can be a dict)
    """
    pass
```

---

## SECTION 7: Decorators (15 points)

### Task 7.1: Simple Decorators (5 points)
Create these function decorators:

```python
def timer(func):
    """
    Decorator that prints execution time of function
    """
    pass

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
```

### Task 7.2: Decorators with Arguments (5 points)
Create decorators that accept arguments:

```python
def repeat(times):
    """
    Decorator that repeats function execution
    @repeat(3)
    def greet(): ...
    """
    pass

def retry(max_attempts):
    """
    Decorator that retries function if it raises an exception
    @retry(3)
    def unstable_function(): ...
    """
    pass
```

### Task 7.3: Class Decorator (5 points)
Create a class that works as a decorator:

```python
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
        # Your code here
        pass
    
    def __call__(self, *args, **kwargs):
        # Your code here
        pass
```

---

## SECTION 8: Generators & Iterators (10 points)

### Task 8.1: Generator Functions (5 points)
Create these generators:

```python
def even_numbers(n):
    """
    Generator that yields first n even numbers
    """
    pass

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
```

### Task 8.2: Custom Iterator Class (5 points)
Create an iterator class:

```python
class RangeIterator:
    """
    Custom iterator that works like range()
    
    Usage:
        for i in RangeIterator(1, 10, 2):
            print(i)  # 1, 3, 5, 7, 9
    """
    def __init__(self, start, stop, step=1):
        # Your code here
        pass
    
    def __iter__(self):
        # Your code here
        pass
    
    def __next__(self):
        # Your code here
        pass
```

---

## SECTION 9: Modules & Packages (10 points)

### Task 9.1: Create a Utilities Module (5 points)
Create a file `string_utils.py` with these functions:
- `reverse_string(s)` - reverses a string
- `is_palindrome(s)` - checks if string is palindrome
- `word_count(s)` - counts words in string
- `title_case(s)` - converts to title case without using .title()

Create a file `math_utils.py` with these functions:
- `is_prime(n)` - checks if number is prime
- `gcd(a, b)` - finds greatest common divisor
- `lcm(a, b)` - finds least common multiple
- `mean(numbers)` - calculates average

Then create `main.py` that imports and uses these modules:

```python
# main.py
# Import and demonstrate usage of both modules
```

### Task 9.2: Create a Package (5 points)
Create a package structure:

```
mypackage/
    __init__.py
    validators.py
    converters.py
```

- `validators.py` should contain: `is_email(s)`, `is_phone(s)`, `is_url(s)`
- `converters.py` should contain: `celsius_to_fahrenheit(c)`, `km_to_miles(km)`, `kg_to_pounds(kg)`
- `__init__.py` should expose commonly used functions

Create a test file that imports from the package:

```python
# test_package.py
from mypackage import is_email
from mypackage.converters import celsius_to_fahrenheit
```

---
## BONUS SECTION: Integrated Mini-Project (10 points)

### Create a Contact Management System

Build a complete contact management system that combines all concepts:

**Requirements:**

1. **Data Model (OOP)**
   - `Contact` class with: name, email, phone, address
   - `ContactBook` class to manage multiple contacts
   - Proper encapsulation and validation

2. **Persistence (File I/O)**
   - Save contacts to JSON file
   - Load contacts from JSON file
   - Auto-save on modifications

3. **Error Handling**
   - Custom exceptions: `DuplicateContactError`, `ContactNotFoundError`
   - Handle file operation errors gracefully

4. **Features**
   - Add contact
   - Search contact by name
   - Update contact
   - Delete contact
   - List all contacts
   - Export contacts to CSV

5. **CLI Interface**
   - Menu-driven interface
   - Input validation with appropriate error messages

```python
# Your implementation here

class Contact:
    pass

class ContactBook:
    pass

def main():
    """
    Main CLI loop
    """
    pass

if __name__ == "__main__":
    main()
```

## BONUS SECTION: Integrated Mini-Project (10 points)
### Create a Task Management System
Build a complete task management system that combines all concepts:
**Requirements:**

**Data Model (OOP)**

- Task class with: id, title, description, status, priority, due_date
- TaskManager class to manage multiple tasks
- Proper encapsulation and validation
- Use properties for status validation (must be: "pending", "in_progress", "completed")


**Persistence (File I/O)**

- Save tasks to JSON file
- Load tasks from JSON file
- Auto-save on modifications


**Error Handling**

- Custom exceptions: TaskNotFoundError, InvalidTaskStatusError
- Handle file operation errors gracefully


**Features (Methods in TaskManager)**

- add_task(task) - add a new task
- get_task(task_id) - get task by ID
- update_task(task_id, **updates) - update task fields
- delete_task(task_id) - remove a task
- list_tasks(status=None) - list all tasks or filter by status
- mark_completed(task_id) - mark task as completed
- Save and load methods


**Additional Requirements**

- Use context managers for file operations
- Use decorators to log all operations
- Use generators for listing large numbers of tasks
- Proper exception handling throughout

---

## Test Cases

Create comprehensive tests for your solutions:

```python
if __name__ == "__main__":
    print("=== Testing Intermediate Python Assessment ===\n")
    
    # Section 1 Tests
    print("Section 1: OOP Basics")
    book = Book("Python Guide", "Jane Smith", 400, 39.99)
    print(book.get_info())
    book.apply_discount(15)
    print(f"After discount: ${book.price:.2f}")
    
    # Section 2 Tests
    print("\nSection 2: Inheritance")
    car = Car("Toyota", "Camry", 2023, 4)
    print(car.start_engine())
    
    # Section 3 Tests
    print("\nSection 3: Encapsulation")
    user = User("alice")
    user.set_password("secure123")
    print(f"Password correct: {user.check_password('secure123')}")
    
    # Section 4 Tests
    print("\nSection 4: File Operations")
    write_log("test.log", "Application started")
    print(read_log("test.log"))
    
    # Section 5 Tests
    print("\nSection 5: Exception Handling")
    success, result = safe_divide(10, 2)
    print(f"Division: {result}")
    
    # Section 6 Tests
    print("\nSection 6: Context Managers")
    with Timer("Test operation"):
        sum([i**2 for i in range(1000)])
    
    # Section 7 Tests
    print("\nSection 7: Decorators")
    @timer
    def test_func():
        return sum(range(1000))
    test_func()
    
    # Section 8 Tests
    print("\nSection 8: Generators")
    print(list(fibonacci_generator(10)))
    
    # Section 10 Tests
    print("\nSection 10: API Requests")
    posts = get_all_posts()
    print(f"Fetched {len(posts)} posts")
    
    print("\n=== Assessment Complete ===")
```

---

## Scoring Guide

- **130-150 points**: Excellent! Ready for FastAPI and advanced concepts
- **100-129 points**: Good understanding, review weaker areas
- **70-99 points**: Decent foundation, need more practice on intermediate concepts
- **Below 70 points**: Review OOP and file I/O fundamentals before proceeding

---

## Submission Checklist

- [ ] All class implementations complete
- [ ] File operations tested with actual files
- [ ] Exception handling properly implemented
- [ ] Context managers working correctly
- [ ] Decorators functioning as expected
- [ ] API requests successfully making calls
- [ ] Code is properly commented
- [ ] Test cases pass
- [ ] Bonus project (if attempted) is functional

---

## Additional Notes

- Use Python 3.8+ features where appropriate
- Follow PEP 8 style guidelines
- Write docstrings for all classes and functions
- Handle edge cases (empty strings, None values, etc.)
- Use type hints where beneficial
- Consider performance for large data operations

Good luck! 🚀