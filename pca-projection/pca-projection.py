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

def covariance_matrix_and_centre(X: list) -> tuple(np.ndarray, list):
    """
    Returns the covariance matrix as a NumPy array with its centred mean matrix
    """
    # Write code here
    
    Xc = X - np.mean(X,axis = 0)
    sig = np.matmul(matrix_transpose(list(Xc)), Xc) /(len(Xc)-1)
    return sig, Xc
    
def calculate_eigs(matrix: list) -> tuple(np.ndarray, np.ndarray):
    """
    Returns a sorted NumPy array of real eigenvalues, with their eigenvectors.
    """
    # Write code here
    eigvalues, eigenvectors = np.linalg.eig(matrix)
    order = np.argsort(eigvalues*-1)
    return eigvalues[order], eigenvectors[:, order]
    
def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    sig, Xc = covariance_matrix_and_centre(X)
    _, eigvecs = calculate_eigs(sig)
    W = []
    for i in range(k):
        W.append(np.transpose(eigvecs)[i])
    W = np.transpose(W)
    return np.matmul(Xc, W)

    