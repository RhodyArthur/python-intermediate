# Task 9.1: Create a Utilities Module (5 points)
# Create a file `string_utils.py` with these functions:
# - `reverse_string(s)` - reverses a string
# - `is_palindrome(s)` - checks if string is palindrome
# - `word_count(s)` - counts words in string
# - `title_case(s)` - converts to title case without using .title()

def reverse_string(s):
    return "".join(s.split()).lower()[::-1]

def is_palindrome(s):
    cleaned_s = "".join(s.split()).lower()
    reverse_string = cleaned_s[::-1]

    if cleaned_s == reverse_string:
        return True
    else:
        return False
print(is_palindrome('A man a plan a canal Panama'))