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

def l1(x:list) -> float:
    norm = 0
    for i in x:
        norm += abs(i)
    return float(norm)

def l2(x:list) -> float:
    norm = 0
    for i in x:
        norm += i**2
    return float(np.sqrt(norm))

def l_inf(x:list) -> float:
    norm = abs(x[0])
    for i in x:
        if i>norm:
            norm = i
    
    return norm

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    NORMS = {"l1": l1, "l2": l2, "max": l_inf}
    norm_matrix = []
    if axis == 0 or axis == 1:
        if axis == 0:
            matrix = matrix_transpose(matrix)
        for i in range(len(matrix)):
            row_norm = NORMS[norm_type](matrix[i])
            if row_norm == 0:
                row_norm = 1
            norm_matrix.append(np.array(matrix[i]) / row_norm)
        if axis == 0:
            norm_matrix = matrix_transpose(list(norm_matrix))
            
    else:
        coolmatrix = []
        for i in matrix:
            coolmatrix += i
        cool_norm = NORMS[norm_type](coolmatrix)
        norm_matrix = np.array(matrix) / cool_norm

    return np.array(norm_matrix)
    
        
                
        
        