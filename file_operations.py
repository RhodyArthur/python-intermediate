# Task 4.1: Text File Operations (5 points)
# Write functions to:
# - `write_log(filename, message)` - appends a timestamped message to a log file
# - `read_log(filename)` - returns all log entries as a list
# - `count_words_in_file(filename)` - returns a dictionary of word frequencies
# - Use context managers for all file operations

from datetime import datetime

def write_log(filename, message):
    # Your code here
    pass

def read_log(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines
        return lines
    except FileNotFoundError:
        return "File not found"

def count_words_in_file(filename):
    # Your code here
    pass