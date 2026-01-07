# `validators.py` should contain: `is_email(s)`, `is_phone(s)`, `is_url(s)`
import re

def is_email(s):
    """
    Determine if a string value is an email
    :param s: string value
    """
    if not s:
        return False
    
    if not isinstance(s, str): return False

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, s) is not None

def is_phone(s):
    if not s:
        return False
    
    if not isinstance(s, str): return False

    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, s) is not None


def is_url(s):
    if not s:
        return False
    
    if not isinstance(s, str): return False

    pattern = r'^(https?:\/\/)?([\w\-])+\.{1}([a-zA-Z]{2,63})([\/\w\-]*)*\/?$'
    return re.match(pattern, s) is not None