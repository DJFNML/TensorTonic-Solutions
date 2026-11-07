import math
import numpy as np
def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred, dtype = float)
    for i in range(len(y_pred)):
        y_pred[i] = min(1-eps, max(eps, y_pred[i]))
    
    return list(-(y_true * np.log(y_pred) + (1-y_true) * np.log(1-y_pred))) 