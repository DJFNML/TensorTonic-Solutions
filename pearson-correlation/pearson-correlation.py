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

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    
    Xc = X - np.mean(X,axis = 0)
    sig = np.matmul(matrix_transpose(list(Xc)), Xc) /(len(Xc)-1)
    return sig


def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    sig = covariance_matrix(X)
    denomElement = np.sqrt(np.diag(sig))
    denom = np.outer(denomElement, np.transpose(denomElement))
    return sig / denom