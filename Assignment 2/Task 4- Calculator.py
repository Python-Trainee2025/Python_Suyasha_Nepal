# Create a calculator that takes two numbers and an operator (+, -, *, /) and
# performs the operation. Handle division by zero and invalid input errors.

def calculator():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        opr = input("Enter the operator: ")

        if opr == "+":
            print(f"{num1} {opr} {num2} = ", num1 + num2)
        elif opr == "-":
            print(f"{num1} {opr} {num2} = ", num1 - num2)
        elif opr == "*":
            print(f"{num1} {opr} {num2} = ", num1 * num2)
        elif opr == "/":
            print(f"{num1} {opr} {num2} = ", num1 / num2)
        else:
            print(f"{opr} is an invalid operation.")

    except ZeroDivisionError:
        print("Division by zero is not possible.")

    except ValueError:
        print("Invalid input. Enter a valid number.")


calculator()