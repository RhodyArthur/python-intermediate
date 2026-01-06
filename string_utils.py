# Task 9.1: Create a Utilities Module (5 points)
# Create a file `string_utils.py` with these functions:
# - `reverse_string(s)` - reverses a string
# - `is_palindrome(s)` - checks if string is palindrome
# - `word_count(s)` - counts words in string
# - `title_case(s)` - converts to title case without using .title()

def reverse_string(s):
    return s.lower().strip()[::-1]

print(reverse_string('cat is home'))