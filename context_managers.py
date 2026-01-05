# Task 6.1: Using Built-in Context Managers (3 points)
# Demonstrate proper use of context managers:

def read_multiple_files(filenames):
    """
    Read multiple files using context managers
    Return a dictionary: {filename: content}
    Handle missing files gracefully
    """
    files  = {}
    try:
        for filename in filenames:
            with open(filename) as f:
                content = f.read()
                files[filename] = content
        return files

    except FileNotFoundError:
        return 'File not found'



def write_transaction_log(transactions):
    """
    Write transactions to a file using context manager
    Each transaction should be on a new line with timestamp
    """
    pass