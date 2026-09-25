import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    means = np.mean(X, keepdims = True, axis = axis)
    stds = np.std(X, keepdims = True, axis = axis)
    stds = np.where(stds < eps, np.inf, stds)
    
    z = (X - means) / stds
   

    return z