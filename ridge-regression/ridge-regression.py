import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    X = np.array(X)
    gram = np.matmul(np.transpose(X), X)
    adjusted_gram = gram + lam*np.identity(len(gram))
    w = np.matmul(np.linalg.inv(adjusted_gram), np.matmul(np.transpose(X), np.array(y)))
    return list(w)