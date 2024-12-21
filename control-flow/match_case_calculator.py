# match_case_calculator.py

# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using if-elif-else
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
        exit()  # Exit the program if division by zero
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please choose one of (+, -, *, /).")
    exit()  # Exit if the operation is invalid

# Output the result
print(f"The result is {result}.")

