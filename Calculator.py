# Simple Calculator with basic arithmetic operations

def calculator():
    print("Welcome to the simple calculator!")

    # Input: Two numbers and an operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose the operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter the number corresponding to the operation: ")

    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    elif operation == '4':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operation! Please choose 1, 2, 3, or 4.")

# Call the calculator function
calculator()
