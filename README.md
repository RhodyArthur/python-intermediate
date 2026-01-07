# Python Intermediate Concepts

A comprehensive repository demonstrating intermediate to advanced Python programming concepts as part of a Backend Development learning path using Python & FastAPI.

## 📚 Overview

This project covers **Phase 1 (Weeks 3-6)** of the Backend Development Roadmap, focusing on:

- Object-Oriented Programming (OOP)
- Advanced Python features (decorators, context managers, generators)
- File operations (text, CSV, JSON)
- Exception handling
- Modules and packages
- Code organization and testing

## 🗂️ Repository Structure

```
python-intermediate/
├── classes_and_objects.py          # OOP fundamentals, class/instance variables
├── inheritance_and_polymorphism.py # Inheritance hierarchies, abstract base classes
├── encapsulation_and_properties.py # Private attributes, property decorators
├── file_operations.py              # Text, CSV, JSON file handling
├── exceptions.py                   # Custom exceptions, error handling
├── context_managers.py             # Resource management (__enter__/__exit__)
├── decorators.py                   # Function decorators, wrapping, timing
├── generators_iterators.py         # Lazy evaluation, custom iterators
├── string_utils.py                 # String manipulation utilities module
├── math_utils.py                   # Mathematical utilities module
├── main.py                         # Module usage demonstrations
├── mypackage/                      # Python package example
│   ├── __init__.py                 # Package initialization
│   ├── validators.py               # Email, phone, URL validation
│   └── converters.py               # Temperature, distance, weight converters
├── test_package.py                 # Test cases for package functions
├── intermediate_python_assessment.md # Learning assessment guide
└── README.md                       # This file
```

## 🎯 Concepts Covered

### 1. Object-Oriented Programming

**Files:** [`classes_and_objects.py`](classes_and_objects.py), [`inheritance_and_polymorphism.py`](inheritance_and_polymorphism.py), [`encapsulation_and_properties.py`](encapsulation_and_properties.py)

- Classes and objects
- Instance vs class variables
- Static methods and class methods
- Magic/dunder methods (`__str__`, `__repr__`, `__add__`)
- Inheritance and method overriding
- Abstract base classes (ABC)
- Polymorphism
- Encapsulation with private attributes
- Property decorators (getters/setters)

### 2. File Operations

**File:** [`file_operations.py`](file_operations.py)

- Reading and writing text files
- CSV file operations (reading, writing, filtering)
- JSON serialization and deserialization
- Proper use of context managers (`with` statement)
- Error handling for file operations
- Working with timestamps

### 3. Exception Handling

**File:** [`exceptions.py`](exceptions.py)

- Try/except/else/finally blocks
- Custom exception classes
- Exception chaining
- Safe wrapper functions
- Error propagation
- Batch error handling

### 4. Context Managers

**File:** [`context_managers.py`](context_managers.py)

- Class-based context managers (`__enter__`/`__exit__`)
- Function-based context managers (`@contextmanager`)
- Resource cleanup and exception handling
- Timer and database connection patterns

### 5. Decorators

**File:** [`decorators.py`](decorators.py)

- Function decorators
- Decorators with arguments
- `@wraps` for preserving metadata
- Class-based decorators
- Decorator stacking
- Logging, timing, and validation decorators

### 6. Generators & Iterators

**File:** [`generators_iterators.py`](generators_iterators.py)

- Generator functions with `yield`
- Custom iterator classes
- `__iter__` and `__next__` methods
- Lazy evaluation for memory efficiency
- Fibonacci and prime number generators

### 7. Modules & Packages

**Files:** [`string_utils.py`](string_utils.py), [`math_utils.py`](math_utils.py), [`mypackage/`](mypackage/)

- Creating reusable modules
- Package structure with `__init__.py`
- Importing and using modules
- `__all__` for controlling exports
- Module organization best practices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- No external dependencies required for core modules

### Running the Code

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd python-intermediate
   ```

2. **Run individual modules:**

   ```bash
   python classes_and_objects.py
   python file_operations.py
   python decorators.py
   # ... etc
   ```

3. **Test module imports:**

   ```bash
   python main.py
   ```

4. **Run package tests:**
   ```bash
   python test_package.py
   ```

## 📖 Learning Path

This repository is part of a comprehensive **Backend Development Roadmap: Python & FastAPI** journey:

- **Phase 1 (Current):** Python Fundamentals ✓
- **Phase 2 (Next):** Web Fundamentals & HTTP
- **Phase 3:** Databases & SQL
- **Phase 4:** FastAPI Foundations
- **Phase 5+:** Authentication, Testing, Deployment

## 🧪 Key Examples

### Using String Utilities

```python
from string_utils import reverse_string, is_palindrome, word_count, title_case

text = "Hello World"
print(reverse_string(text))  # "dlroW olleH"
print(is_palindrome("racecar"))  # True
print(word_count("hello world hello"))  # {'hello': 2, 'world': 1}
print(title_case("python programming"))  # "Python Programming"
```

### Using Math Utilities

```python
from math_utils import is_prime, gcd, lcm, mean

print(is_prime(17))  # True
print(gcd(48, 18))   # 6
print(lcm(12, 15))   # 60
print(mean([10, 20, 30]))  # 20.0
```

### Using Package Converters

```python
from mypackage.converters import celsius_to_fahrenheit, km_to_miles, kg_to_pounds

print(celsius_to_fahrenheit(25))  # 77.0
print(km_to_miles(10))            # 6.21371
print(kg_to_pounds(50))           # 110.231
```

## 📝 Assessment

The repository includes an assessment guide ([`intermediate_python_assessment.md`](intermediate_python_assessment.md)) with:

- 10 core sections covering all concepts
- Point-based scoring system
- Bonus project challenges
- Readiness checklist for FastAPI

**Current Progress:** ~85% completion (Phase 1, Weeks 3-6)

## 🎓 Skills Demonstrated

- ✅ Object-Oriented Programming mastery
- ✅ Advanced Python patterns (decorators, generators, context managers)
- ✅ File I/O and data persistence
- ✅ Robust error handling
- ✅ Module and package organization
- ✅ Code reusability and maintainability
- ⏳ Type hints and type checking (in progress)
- ⏳ HTTP/REST API fundamentals (next)

## 📄 License

This is a learning project created as part of a personal development roadmap.

## 👤 Author

**Rhoda Arthur**  
Backend Developer in Training  
Focus: Python & FastAPI

---

_Last Updated: January 7, 2026_
