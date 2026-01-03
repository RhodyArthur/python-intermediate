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