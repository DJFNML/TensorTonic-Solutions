import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)
    fpr_shift = fpr[1:]
    tpr_shift = tpr[1:]
    fpr_back = fpr[:-1]
    tpr_back = tpr[:-1]

    return float(np.sum(0.5 * (fpr_shift - fpr_back) * (tpr_shift + tpr_back)))
    