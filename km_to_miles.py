def km_to_miles(kilometers):
    """
    Converts kilometers to miles.

    Parameters:
    ----------
    kilometers : float
        The distance in kilometers to be converted to miles.

    Returns:
    -------
    float:
        The equivalent distance in miles.
    
    Example:
    --------
    km_to_miles(5)  # Output: 3.106855 miles
    """
    # Conversion factor from kilometers to miles
    if kilometers < 0:
        return None  # or raise an exception if negative values are not allowed

    miles = kilometers * 0.621371
    return miles

# Example usage
kilometers = 10
print("The distance in miles is:", km_to_miles(kilometers))  # Expected output: The distance in miles is: 6.21371