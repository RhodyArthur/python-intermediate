# Task 6.1: Using Built-in Context Managers (3 points)
# Demonstrate proper use of context managers:

def read_multiple_files(filenames):
    """
    Read multiple files using context managers
    Return a dictionary: {filename: content}
    Handle missing files gracefully
    """
    files  = {}
    for filename in filenames:
        try:
            with open(filename) as f:
                content = f.read()
                files[filename] = content

        except FileNotFoundError:
            files[filename] = None
    return files



def write_transaction_log(transactions):
    """
    Write transactions to a file using context manager
    Each transaction should be on a new line with timestamp
    """
    from datetime import datetime

    with open('transactions.log', 'a') as f:
        for transaction in transactions:
            timestamp = datetime.now().strftime('%Y-%m-%d - %H:%M:%S')
            f.write(f'{timestamp}-{transaction}\n')