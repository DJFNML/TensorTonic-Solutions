import numpy as np
def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    entropy = 0
    z = set(y)
    if len(y) == 0:
        return float(0)
    for x in z:
        p_i = y.count(x) / len(y)
        entropy += p_i * np.log2(p_i)

    return -entropy