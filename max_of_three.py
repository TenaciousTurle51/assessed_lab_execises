def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    num_list=[num1,num2,num3]
    num_list.sort()
    maximum = num_list[2]



    return maximum
maximum = max_of_three(10,20.0,30)
print(f"{maximum} is the maximum")
# # You are out of the body function where you can test your code.
# Example usage:
# maximum = max_of_three(10, 20, 30)
# print(maximum, "is the maximum")
