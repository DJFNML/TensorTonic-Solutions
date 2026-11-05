import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    w = np.zeros(np.shape(X[0]))
    b = 0.0
    n = len(y)
    for x in range(steps):
        z = np.matmul(X,w) + b
        p = _sigmoid(z)
        L = np.sum(y * np.log(p) + (1-y) * np.log(1-p)) / (-n)
        w_deriv = np.matmul(np.transpose(X), p-y) / n
        b_deriv = np.sum(p-y) / n
        w = w - lr * w_deriv
        b = b - lr * b_deriv

    return (w,b)