import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    return np.maximum(x, np.zeros(np.shape(np.array(x))))