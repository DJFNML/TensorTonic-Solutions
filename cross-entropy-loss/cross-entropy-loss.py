import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    losses = []
    for i in range(len(y_pred)):
        p_i_yi = y_pred[i][y_true[i]]
        losses.append(-np.log(p_i_yi))

    return np.average(losses)