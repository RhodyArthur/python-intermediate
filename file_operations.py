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

headers = ['id', 'name', 'age', 'grade']
def save_students_csv(filename, students):
    with open(filename, 'w', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)

def load_students_csv(filename):
    try: 
        with open(filename) as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []


def add_student_csv(filename, student):
    with open(filename, 'a', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(student)

def find_student_by_id(filename, student_id):
    try: 
        with open(filename) as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row['id'] == str(student_id):
                    return row
        return None
    except FileNotFoundError:
        return None
    
# Task 4.3: JSON Operations (5 points)
# Create a configuration manager:
# - `save_config(filename, config_dict)` - saves configuration to JSON with nice formatting
# - `load_config(filename)` - loads and returns configuration dict
# - `update_config(filename, key, value)` - updates a specific key in the config
# - `get_config_value(filename, key, default=None)` - gets a value or returns default

import json

def save_config(filename, config_dict):
    with open(filename, 'w') as f:
        json.dump(config_dict, f, indent=4)


def load_config(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_config(filename, key, value):
    config_dict = load_config(filename)
    config_dict[key] = value
    save_config(filename, config_dict)

def get_config_value(filename, key, default=None):
    config_dict = load_config(filename)
    return config_dict.get(key, default)


# Task 4.4: File Operations with Error Handling (5 points)
# Create a robust file reader:
# - `safe_read_file(filename)` - reads file content, handles FileNotFoundError
# - `safe_write_file(filename, content)` - writes content, handles PermissionError
# - `copy_file(source, destination)` - copies file with proper error handling
# - All functions should return appropriate messages on success/failure

def safe_read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
        return True
    except FileNotFoundError:
        return 'File not found'


def safe_write_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return True
    except PermissionError:
        return 'You do not have the right permissions to write to this file'


def copy_file(source, destination):
    # Your code here - return (success: bool, message: str)
    pass