# Task 1.1: Basic Class Implementation (5 points)
# Create a `Book` class with the following:
# - Attributes: `title`, `author`, `pages`, `price`
# - Method `get_info()` that returns a formatted string with all book details
# - Method `apply_discount(percentage)` that reduces the price by the given percentage
# - `__str__` method that returns a readable representation

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Title: {self.title} \n Author: {self.author} \n Number of pages {self.pages} \n Price: ${self.price}"
    
    def apply_discount(self, percentage):
        discount = self.price * (percentage/100)
        return self.price - discount
    
    def __str__(self):
        return f"Title: {self.title} \n Author: {self.author} \n Number of pages {self.pages} \n Price: ${self.price}"
    
book = Book("Python Mastery", "John Doe", 350, 29.99)
print(book.get_info())
book.apply_discount(10)
print(book)
    
# Task 1.2: Class and Instance Variables (5 points)
# Create a `BankAccount` class with:
# - Class variable `bank_name = "MyBank"`
# - Class variable `total_accounts` that tracks the number of accounts created
# - Instance variables: `account_number`, `owner`, `balance`
# - Method `deposit(amount)` that adds to balance
# - Method `withdraw(amount)` that subtracts from balance (don't allow overdraft)
# - Class method `get_bank_info()` that returns bank name and total accounts

class BankAccount:
    bank_name = "MyBank"
    total_accounts = 0

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return self.balance
        return "Amount must be positive"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount 
            return self.balance
        return "Balance is insufficient to withdraw"
    
    @classmethod
    def get_bank_info(cls):
        return f"Bank name: {cls.bank_name} \n Total accounts: {cls.total_accounts}"

acc1 = BankAccount(101, "Alice", 500)
acc2 = BankAccount(102, "Bob", 1000)
print(acc1.deposit(200))
print(acc2.withdraw(1500))

print(BankAccount.get_bank_info())
