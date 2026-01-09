def main():
    try:
        n1 = float(input("Enter number1: "))
        n2 = float(input("Enter number2: "))
    except ValueError:
        print("Invalid number entered. Please enter numeric values only.")
        return  # Stops function safely if input is bad
    op = input("Enter operator (+, -, *, /): ").strip()

    if op == '+':
        print("The result is:", n1 + n2)
    elif op == '-':
        print("The result is:", n1 - n2)
    elif op == '*':
        print("The result is:", n1 * n2)
    elif op == '/':
        if n2 != 0:
            print("The result is:", n1 / n2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Operator not supported. Please use +, -, *, or /.")

if __name__ == "__main__":
    main()
