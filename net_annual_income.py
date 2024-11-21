def annual_net_income(gross_salary):
    """
    Calculates the annual net income after tax deduction.
    
    Parameters:
    ----------
    gross_salary : float
        The annual gross salary before tax.
    
    Returns:
    -------
    float:
        The net salary after tax deduction.
    
    Example:
    --------
    If the gross salary is 50,000, the net salary after a 20% tax will be 40,000.
    """
    tax_rate = 0.20  # 20% tax rate
    tax_deduction = gross_salary * tax_rate  # Calculate tax deduction
    net_salary = gross_salary - tax_deduction  # Calculate net salary
    return net_salary

# Example usage
gross_salary = 50000
net_income = annual_net_income(gross_salary)
print(f"The annual net income is: {net_income}")  # Expected output: The annual net income is: 40000.0
