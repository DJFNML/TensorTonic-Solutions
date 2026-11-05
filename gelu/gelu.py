import numpy as np
from scipy import special

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)
    return (x / 2) * (1 + special.erf(x / np.sqrt(2)))