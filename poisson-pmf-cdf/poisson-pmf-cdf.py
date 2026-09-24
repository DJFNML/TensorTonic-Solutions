import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    poipmf = lambda lam, k: (math.exp(-lam) * lam**k) / math.factorial(k)

    pmf = poipmf(lam, k)
    cdf = 0
    for i in range(k+1):
        cdf += poipmf(lam, i)

    return {"pmf": pmf, "cdf": cdf}