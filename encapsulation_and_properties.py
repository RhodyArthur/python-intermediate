# Task 3.1: Private Attributes (5 points)
# Create a `User` class with:
# - Private attribute `__password`
# - Public attribute `username`
# - Method `set_password(password)` that only accepts passwords with 8+ characters
# - Method `check_password(password)` that returns True if password matches
# - Don't allow direct access to `__password`

class User:
    def __init__(self, username, password="12345678"):
        self.__password = password
        self.username = username

    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Accepts passwords with more then 8 characters")
        self.__password = password

    def check_password(self, password):
        if self.__password == password:
            return True
        return False

user = User("alice")
user.set_password("secret123")
print(user.check_password("secret123"))
print(user.check_password("wrong")) 

# Task 3.2: Property Decorators (5 points)
# Create a `Temperature` class with:
# - Private attribute `__celsius`
# - Property `celsius` with getter and setter (setter validates value >= -273.15)
# - Property `fahrenheit` with getter and setter (converts to/from celsius)
# - Property `kelvin` with getter (read-only, converts from celsius)

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            raise ValueError("Temperature must be greater than or equal to -273.15")
    
    @property
    def fahrenheit(self):
        return (self.celsius * (9/5)) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * (5/9)
            

    @property
    def kelvin(self):
        return self.celsius + 273.15
    
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0
print(temp.kelvin)       # 298.15

temp.fahrenheit = 32
print(temp.celsius)

# Task 3.3: Full Encapsulation Example (5 points)
# Create a `BankAccountSecure` class with:
# - Private attributes: `__account_number`, `__balance`, `__pin`
# - Properties for account_number (read-only) and balance (read-only)
# - Method `deposit(amount, pin)` that adds to balance if pin is correct
# - Method `withdraw(amount, pin)` that subtracts if pin is correct and sufficient funds
# - Method `change_pin(old_pin, new_pin)` that changes pin if old_pin is correct

class BankAccountSecure:
    def __init__(self, account_number, balance, pin):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = str(pin)

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Pin mismatch")
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.__balance = self.balance + amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance = self.__balance - amount

    def change_pin(self, old_pin, new_pin):
        if self.__pin != old_pin:
            raise ValueError("Incorrect old pin")
        self.__pin = new_pin