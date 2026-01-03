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
    