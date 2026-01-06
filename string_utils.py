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

    if cleaned_s == cleaned_s[::-1]:
        return True
    else:
        return False
    
def word_count(s):
    wc = {}

    for word in s.lower().split():
        wc[word] = wc.get(word, 0) +1
    return wc
print(word_count('A man a plan a canal Panama man'))