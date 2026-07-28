# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# def read_matrix(rows, cols, name=""):
    """Helper function to read a matrix from user input line by line."""
    if name:
        print(f"\nEntering values for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Error: Expected {cols} numbers. Try again.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Prints a matrix in a neat, aligned grid format."""
    for row in matrix:
        print(" ".join(f"{val:<4}" for val in row))


# --- PART A: Transpose Matrix ---
def transpose_matrix(matrix):
    """Computes and returns the transpose of a matrix (M x N -> N x M)."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty result grid (N x M)
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# --- PART B: Add Two Matrices ---
def add_matrices(matrix_a, matrix_b):
    """Performs element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            
    return result


# --- PART C: Multiply Two Matrices ---
def multiply_matrices(matrix_a, matrix_b):
    """Multiplies matrix A (M x N) and matrix B (N x P) to produce (M x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Result size: rows_a x cols_b
    result = [[0] * cols_b for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result


def main():
    print("=== PART A: TRANSPOSE MATRIX ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    mat_a = read_matrix(m, n)
    
    print("\nOriginal Matrix:")
    display_matrix(mat_a)
    
    transposed = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    display_matrix(transposed)

    print("\n" + "="*35)
    print("=== PART B: ADD TWO MATRICES ===")
    print(f"Reading two matrices of size ({m} x {n})...")
    mat_b1 = read_matrix(m, n, "Matrix 1")
    mat_b2 = read_matrix(m, n, "Matrix 2")
    
    added = add_matrices(mat_b1, mat_b2)
    print("\nMatrix Sum Result:")
    display_matrix(added)

    print("\n" + "="*35)
    print("=== PART C: MULTIPLY TWO MATRICES ===")
    m_a = int(input("Enter rows for Matrix A: "))
    n_a = int(input("Enter columns for Matrix A: "))
    
    print(f"Matrix B MUST have {n_a} rows.")
    p_b = int(input("Enter columns for Matrix B: "))
    
    mat_c1 = read_matrix(m_a, n_a, "Matrix A")
    mat_c2 = read_matrix(n_a, p_b, "Matrix B")
    
    multiplied = multiply_matrices(mat_c1, mat_c2)
    print("\nMatrix Product Result (A x B):")
    display_matrix(multiplied)


if __name__ == "__main__":
    main()

