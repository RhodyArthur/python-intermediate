# Task 8.1: Generator Functions (5 points)
# Create these generators:

def even_numbers(n):
    """
    Generator that yields first n even numbers
    """
    count = 0
    num = 2

    while count < n:
        yield num
        num += 2
        count += 1

def fibonacci_generator(n):
    """
    Generator that yields first n Fibonacci numbers
    """
    count = 0
    x, y = 0, 1

    while count < n:
        yield x
        x, y = y, x + y
        count += 1

def file_line_generator(filename):
    """
    Generator that yields lines from a file one at a time
    Strips whitespace from each line
    """
    try:
        with open(filename) as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        return


# Task 8.2: Custom Iterator Class (5 points)
# Create an iterator class:

class RangeIterator:
    """
    Custom iterator that works like range()
    
    Usage:
        for i in RangeIterator(1, 10, 2):
            print(i)  # 1, 3, 5, 7, 9
    """
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value

for i in RangeIterator(1, 5, 2):
    print(i)