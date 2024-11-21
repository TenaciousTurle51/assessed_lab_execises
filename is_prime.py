import math #to use sqrt

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...

    output = False
    #Can't be less than 2 
    if num <=1:
        return False 
    
    #check divisibily from to 2 to sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            output = False
        
        else:  #nothing found means it's prime
            output = True

    return output


# # # Run code example
boolean = is_prime(5)   # returns True
print(boolean)
  