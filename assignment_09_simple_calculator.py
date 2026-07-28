# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# # Arithmetic operation functions


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a % b


def exponentiate(a, b):
    return a**b


def get_number_input(prompt):
    """Helper function to safely get a float/int number from user."""
    while True:
        try:
            val = input(prompt).strip()
            # Convert to int if it's a whole number, else float
            num = float(val)
            return int(num) if num.is_integer() else num
        except ValueError:
            print("Error: Invalid number. Please try again.")


def display_menu():
    """Prints the calculator menu."""
    print("\n" + "--------------------------------")
    print("        SIMPLE CALCULATOR")
    print("--------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid option. Please select a number from 1 to 7.")
            continue

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        if choice == "1":
            res = add(num1, num2)
            op_symbol = "+"
        elif choice == "2":
            res = subtract(num1, num2)
            op_symbol = "-"
        elif choice == "3":
            res = multiply(num1, num2)
            op_symbol = "*"
        elif choice == "4":
            res = divide(num1, num2)
            op_symbol = "/"
        elif choice == "5":
            res = modulus(num1, num2)
            op_symbol = "%"
        elif choice == "6":
            res = exponentiate(num1, num2)
            op_symbol = "**"

        if res is not None:
            print(f"Result: {num1} {op_symbol} {num2} = {res}")


if __name__ == "__main__":
    main()

