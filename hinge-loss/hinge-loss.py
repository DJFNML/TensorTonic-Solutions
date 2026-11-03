import numpy as np

def meanreduction(y_true: list, y_score: list, margin: float = 1.0) -> float:
    return np.sum(np.maximum(np.zeros(np.shape(np.array(y_score))), margin - (np.array(y_true) * np.array(y_score)))) / len(y_true)
    
def sumreduction(y_true: list, y_score: list, margin: float = 1.0) -> float:
    return np.sum(np.maximum(np.zeros(np.shape(y_score)), margin - (np.array(y_true) * np.array(y_score))))
    
def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    method = {"mean": meanreduction, "sum": sumreduction}
    return float(method[reduction](y_true, y_score, margin))
    