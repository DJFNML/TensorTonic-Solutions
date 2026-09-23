import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    f = lambda n,p,k: math.comb(n,k) * (p**k) * ((1-p) **(n-k))
    pmf = f(n,p,k)
    cdf = 0
    for i in range(k+1):
        cdf += f(n,p,i)

    return {"pmf": float(pmf), "cdf": float(cdf)}