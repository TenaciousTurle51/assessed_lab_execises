def Calculator(): #Define function/ Name
    num1 = int(input("Insert num 1: "))
    num2 = int(input("Insert num 2: "))
    operator = input("What is operator: ") #(+, -, *, /, %, >, >=, <, <=)
    #User input

    result = 0
    #preload the result


    #Maths: Find/check user input and compile result
    if operator == "+":
        result = num1 + num2
        print("The result is:", result)
    elif operator == "-":
        result = num1 - num2
        print("The result is:", result)
    elif operator == "*":
        result = num1 * num2
        print("The result is:", result)
    elif operator == "/":
        if num2 !=0:
            result = num1/num2
            print("The result is:", result)
        else:
            print("Error: Division by zero")
    elif operator ==">":
        result = num1 > num2
        print(f"The comparison result is: {result}")
    elif operator ==">=":
        result = num1 >= num2
        print(f"The comparison result is: {result}")
    elif operator =="<":
        result = num1 < num2
        print(f"The comparison result is: {result}")
    elif operator =="<=":
        result = num1 <= num2
        print(f"The comparison result is: {result}")
    else:
        print("Invalid operator") #not listed or invalid operator
    return result

Calculator() #Call the function


