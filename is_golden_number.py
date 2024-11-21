def is_golden_number(n):
    """
    Determines if a given positive integer less than 1000 is a golden number.
    
    A number is considered golden if:
    1. It can be expressed as a sum of two positive integers a and b: n = a + b.
    2. The product a * b is divisible by 1000.
    
    Parameters:
    ----------
    n : int
        A positive integer less than 1000.
    
    Returns:
    -------
    bool:
        True if the number is a golden number, otherwise False.
    """
    if n >= 1000 or n <= 0:
        raise ValueError("Input must be a positive integer less than 1000.")
    
    # Iterate through all possible pairs of (a, b)
    for a in range(1, n):
        b = n - a  # Since n = a + b
        if a * b % 1000 == 0:  # Check if a * b is divisible by 1000
            return True
    
    return False
# Test cases
print(is_golden_number(65))  # Expected output: True
print(is_golden_number(70))  # Expected output: True
print(is_golden_number(61))  # Expected output: False
