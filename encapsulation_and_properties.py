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