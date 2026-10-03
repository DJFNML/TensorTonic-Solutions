import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X = np.array(X)
    gram_inv = np.linalg.inv(np.matmul(np.transpose(X), X))
    w = np.matmul(np.matmul(gram_inv,np.transpose(X)), np.array(y))

    return list(w)
    