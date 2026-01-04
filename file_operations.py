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
    

# Task 4.2: CSV Operations (5 points)
# Create a student management system with CSV:
# - `save_students_csv(filename, students)` - saves list of student dicts to CSV
# - `load_students_csv(filename)` - loads students from CSV and returns list of dicts
# - `add_student_csv(filename, student)` - appends a new student to existing CSV
# - `find_student_by_id(filename, student_id)` - finds and returns student dict

# Student dict format: `{'id': 1, 'name': 'Alice', 'age': 20, 'grade': 'A'}`

import csv

def save_students_csv(filename, students):
    headers = ['id', 'name', 'age', 'grade']
    with open(filename, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)

def load_students_csv(filename):
    try: 
        with open(filename) as f:
            reader = csv.DictReader(f)
        return reader
    except FileNotFoundError:
        return []


# def add_student_csv(filename, student):
#     pass

# def find_student_by_id(filename, student_id):
#     pass