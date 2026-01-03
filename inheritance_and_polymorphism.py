# Task 2.1: Single Inheritance (6 points)
# Create a base class `Vehicle` with:
# - Attributes: `brand`, `model`, `year`
# - Method `get_info()` that returns vehicle information
# - Method `start_engine()` that returns "Engine started"

# Create two child classes:
# - `Car` that adds `doors` attribute and overrides `start_engine()` to return "Car engine started"
# - `Motorcycle` that adds `engine_cc` attribute and overrides `start_engine()` to return "Motorcycle engine started"

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle information: \n Brand: {self.brand} \n Model: {self.model} \n Year: {self.year}"
    
    def start_engine(self):
        return "Engine started"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def start_engine(self):
        return "Motorcycle engine started"
    
# Task 2.2: Using super() (5 points)
# Create an `Employee` base class with:
# - Attributes: `name`, `employee_id`, `base_salary`
# - Method `calculate_salary()` that returns base_salary

# Create a `Manager` child class that:
# - Adds `team_size` attribute
# - Overrides `calculate_salary()` to add bonus (base_salary + team_size * 1000)
# - Uses `super()` to call parent's `__init__`

class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
    
class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size):
        super().__init__(name, employee_id, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        return super().calculate_salary() + (self.team_size * 1000)
    

# Task 2.3: Abstract Shape Hierarchy (9 points)
# Create an abstract base class `Shape` with:
# - Abstract method `area()`
# - Abstract method `perimeter()`

# Create three concrete classes:
# - `Circle` with radius
# - `Rectangle` with length and width
# - `Triangle` with three sides

# Each should implement the abstract methods correctly.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    pi = 3.147

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return Circle.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * Circle.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)
    
class Triangle(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        half_peri = (self.length + self.width + self.height) / 2
        return (half_peri * (half_peri - self.length) * (half_peri - self.width) * (half_peri - self.height)) ** 1/2 

    def perimeter(self):
        return self.length + self.width + self.height
    
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(type(shape).__name__)
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
