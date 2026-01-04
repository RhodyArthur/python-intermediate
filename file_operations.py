# Task 4.1: Text File Operations (5 points)
# Write functions to:
# - `write_log(filename, message)` - appends a timestamped message to a log file
# - `read_log(filename)` - returns all log entries as a list
# - `count_words_in_file(filename)` - returns a dictionary of word frequencies
# - Use context managers for all file operations

from datetime import datetime

def write_log(filename, message):
    with open(filename, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {message}\n")


def read_log(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return []
    

def count_words_in_file(filename):
    word_frequency = {}
    try:
        with open(filename, 'r') as f:
            content = f.read()

            for word in content.lower().split():
                word_frequency[word] = word_frequency.get(word, 0) + 1
        return word_frequency

    except FileNotFoundError:
        return {}