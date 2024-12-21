def match_case_calculator():
    # Prompt the user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Ask for the operation they want to perform
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using if-elif-else
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return  # Exit the function
        result = num1 / num2
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return  # Exit the function

    # Output the result
    print(f"The result is {result}.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    match_case_calculator()

