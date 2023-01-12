def calculator():
    operation = input("Please select an operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(num1 + num2)

    elif operation == '-':
        print(num1 - num2)

    elif operation == '*':
        print(num1 * num2)

    elif operation == '/':
        print(num1 / num2)
    else:
        print("Invalid operator")

calculator()
