def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """
    #if min value isn't even adds 1
    if min_value % 2 != 0:
        min_value += 1
    
    #value for total
    total = 0
    #calculate the sum
    for num in range(min_value, max_value + 1, 2): #Increments of 2
        total += num

    return total

# # # Run code example
min_value = 5
max_value = 34
result = sum_of_evens(min_value, max_value) # returns 22
print(result)