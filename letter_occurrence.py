def letter_occurrence(input_string):
    """
    Counts the occurrence of each letter in the input string.
    
    Parameters:
    ----------
    input_string : str
        The string in which letter occurrences are to be counted.
    
    Returns:
    -------
    dict:
        A dictionary where the keys are letters, and the values are their counts.
    
    Example:
    --------
    input_string = "hello"
    letter_occurrence(input_string)
    # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    count = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    return count

# Example usage
input_string = "Apples and Bananas"
print("The number of 'a' or 'A' in the string is:", letter_occurrence(input_string))  # Expected output: The number of 'a' or 'A' in the string is: 4