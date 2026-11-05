import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.array(x)
    if len(np.shape(x)) == 1:
        m = np.max(x)
        p = np.exp(x - m) / np.sum(np.exp(x - m))
        return p
    else:
        P = []
        for a in x:
            m = np.max(a)
            p = np.exp(a - m) / np.sum(np.exp(a - m))
            P.append(p)
        return np.array(P)