def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return "Error! Division by zero." if num2 == 0 else num1 / num2

def main():
    operations = {'1': '+', '2': '-', '3': '*', '4': '/'}
    while True:
        print("\nSimple Calculator")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        result = calculate(num1, num2, operations[choice])
        print(f"{num1} {operations[choice]} {num2} = {result}")

if __name__ == "__main__":
    main()
