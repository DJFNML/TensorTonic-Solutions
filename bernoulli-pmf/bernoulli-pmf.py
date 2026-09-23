import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = []
    for i in x:
        pfunc = lambda x: p if x == 1 else (1-p)
        pmf +=[float(pfunc(i))]

    variance =  float(p*(1-p))
    pmf = np.array(pmf)
    return {"pmf": pmf, "mean": float(p), "variance": variance}