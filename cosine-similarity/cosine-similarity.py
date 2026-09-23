import numpy as np

def norm2(a: list) -> float:
    norm = 0
    for i in range(len(a)):
        norm += a[i] * a[i]
    return float(np.sqrt(norm))
    
def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    dp = 0
    for i in range(len(x)):
        dp += x[i] * y[i]

    return float(dp)

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a2 = norm2(a)
    b2 = norm2(b)

    if a2 == 0 or b2 == 0:
        return float(0)
    else:
        return float(dot_product(a,b) / (a2*b2))