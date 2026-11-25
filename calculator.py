

# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Taking valid number input
def read_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Please enter a valid number!")


# Unit Converter
def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometer to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilogram to Pounds")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            km = read_number("Enter kilometers: ")
            miles = km * 0.621371
            print("Miles:", miles)

        elif choice == "2":
            c = read_number("Enter Celsius: ")
            f = (c * 9/5) + 32
            print("Fahrenheit:", f)

        elif choice == "3":
            kg = read_number("Enter kilograms: ")
            pounds = kg * 2.20462
            print("Pounds:", pounds)

        elif choice == "4":
            break

        else:
            print("Invalid choice! Try again.")


# Main Calculator
def main():
    while True:
        print("\n===== MY CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Converter")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you for using my calculator!")
            break

        elif choice in ("1", "2", "3", "4"):
            num1 = read_number("Enter first number: ")
            num2 = read_number("Enter second number: ")

            if choice == "1":
                print("Result:", add(num1, num2))

            elif choice == "2":
                print("Result:", subtract(num1, num2))

            elif choice == "3":
                print("Result:", multiply(num1, num2))

            elif choice == "4":
                print("Result:", divide(num1, num2))

        elif choice == "5":
            unit_converter()

        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()