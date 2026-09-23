import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    B = np.zeros((len(A[0]), len(A)))
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[j][i] = A[i][j]

    return B
