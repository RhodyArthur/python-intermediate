# Create a file `math_utils.py` with these functions:
# - `is_prime(n)` - checks if number is prime
# - `gcd(a, b)` - finds greatest common divisor
# - `lcm(a, b)` - finds least common multiple
# - `mean(numbers)` - calculates average

def is_prime(n):
    if n < 2:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True

def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def mean(numbers):
    return sum(numbers) / len(numbers)