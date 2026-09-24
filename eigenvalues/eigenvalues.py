import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    eigvalues = np.linalg.eigvals(matrix)
    eigvalues = np.sort(eigvalues)
    return eigvalues