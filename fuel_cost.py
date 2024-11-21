def fuel_cost(distance_miles):
    # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter

    # Calculate total fuel needed in gallons
    fuel_needed_gallons = distance_miles / MPG

    # Convert fuel to liters
    fuel_needed_liters = fuel_needed_gallons * LITERS_PER_GALLON

    # Calculate total cost
    total_cost = fuel_needed_liters * PRICE_PER_LITER

    return round(total_cost, 2)
distance = 100  # Distance in miles
cost = fuel_cost(distance)
print(f"The total fuel cost for {distance} miles is £{cost}.")
