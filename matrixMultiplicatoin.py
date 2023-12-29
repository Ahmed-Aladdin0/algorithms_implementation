import numpy as np
import time


def strassen_matrix_multiplication(A, B, print_time=True):
    """
    Performs Strassen's matrix multiplication algorithm.
    """
    global start, startP
    if print_time:
        start = time.time()  # Record the start time
        startP = time.process_time()

    n = len(A)

    if n <= 2:
        return np.matmul(A, B)  # Base case: use traditional multiplication

    # Recursively divide matrices into four sub-matrices each
    a11, a12, a21, a22 = A[:n//2, :n//2], A[:n//2, n//2:], A[n//2:, :n//2], A[n//2:, n//2:]
    b11, b12, b21, b22 = B[:n//2, :n//2], B[:n//2, n//2:], B[n//2:, :n//2], B[n//2:, n//2:]

    # Calculate necessary products recursively using Strassen's algorithm
    p1 = strassen_matrix_multiplication(a11 + a22, b11 + b22, print_time=False)
    p2 = strassen_matrix_multiplication(a21 + a22, b11, print_time=False)
    p3 = strassen_matrix_multiplication(a11, b12 - b22, print_time=False)
    p4 = strassen_matrix_multiplication(a22, b21 - b11, print_time=False)
    p5 = strassen_matrix_multiplication(a11 + a12, b22, print_time=False)
    p6 = strassen_matrix_multiplication(a21 - a11, b11 + b12, print_time=False)
    p7 = strassen_matrix_multiplication(a12 - a22, b21 + b22, print_time=False)

    # Combine products to form the final result matrix
    C = np.zeros((n, n))
    C[:n//2, :n//2] = p1 + p4 - p5 + p7
    C[:n//2, n//2:] = p3 + p5
    C[n//2:, :n//2] = p2 + p4
    C[n//2:, n//2:] = p1 - p2 + p3 + p6

    if print_time:
        print("Strassen's matrix multiplication")
        print(C)
        finish = time.time()
        finishP = time.process_time()
        elapsed = finish - start
        cpu = finishP - startP
        print('Real time:', elapsed, 'seconds')
        print('CPU time:', cpu, 'seconds')
        print()
    return C

def generate_random_matrix(n, m):
    """
    Generates a random matrix of size n x m, where n and m must be powers of 2.
    Raises a ValueError if dimensions are not powers of 2 or do not match.
    """

    if n != m:
        raise ValueError("Matrix dimensions should match")

    if not (n & (n - 1) == 0) or not (m & (m - 1) == 0):
        raise ValueError("Matrix dimensions must be powers of 2")

    return np.random.randint(1, 10, size=(n, m))  # Adjust range as needed




