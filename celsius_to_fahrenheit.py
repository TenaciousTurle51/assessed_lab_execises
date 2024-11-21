def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    ----------
    celsius : float
        The temperature in degrees Celsius.

    Returns:
    -------
    float:
        The temperature converted to degrees Fahrenheit.
    
    Formula:
    --------
    Fahrenheit = (Celsius * 9/5) + 32
    """
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F.")  # Expected output: 25°C is equal to 77.0°F.
