import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    return float(np.sum(np.array(p) * np.log((np.array(p) + eps) / np.array(q))))