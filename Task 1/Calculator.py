def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def display_menu():
    print("\nWelcome to Terminal Calculator 🧮")
    print("Choose your operation:")
    print("1. Add ➕")
    print("2. Subtract ➖")
    print("3. Multiply ✖️")
    print("4. Divide ➗")
    print("5. Exit 🚪")

while True:
    display_menu()
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("👋 Exiting the calculator.math hero")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("❌ Invalid choice! Please select a number from 1 to 5.")
