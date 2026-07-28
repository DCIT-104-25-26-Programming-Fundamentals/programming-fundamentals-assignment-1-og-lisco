# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# # --- PART A: Print First N Terms ---
def generate_fibonacci(n):
    """
    Generates and returns the first N numbers of the Fibonacci sequence as a list.
    Uses an iterative loop approach.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence


# --- PART B: Check if a Number Belongs to the Sequence ---
def is_fibonacci(target):
    """
    Checks if a non-negative integer target belongs to the Fibonacci sequence.
    Generates terms iteratively until reaching or exceeding the target.
    """
    if target < 0:
        return False
    
    a, b = 0, 1
    while a < target:
        a, b = b, a + b
        
    return a == target


def main():
    # --- PART A ---
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: N must be a positive integer.")
        else:
            terms = generate_fibonacci(n)
            # Print terms on one line separated by spaces
            print("Fibonacci sequence:", " ".join(map(str, terms)))
    except ValueError:
        print("Error: Please enter a valid integer.")

    print()  # Spacer line

    # --- PART B ---
    try:
        target = int(input("Enter a number to check: "))
        if target < 0:
            print(f"{target} is NOT a Fibonacci number.")
        elif is_fibonacci(target):
            print(f"{target} is a Fibonacci number.")
        else:
            print(f"{target} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
  

