import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    if num_classes == None:
        num_classes = max(y) + 1
    encoding = np.zeros((len(y), num_classes))
    for i in range(len(encoding)):
        encoding[i][y[i]] = float(1)

    return encoding