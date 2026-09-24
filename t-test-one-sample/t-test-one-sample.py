import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    mean = np.mean(x)
    s = 0
    for i in range(len(x)):
        s += (x[i] - mean)**2

    s = math.sqrt(s/(len(x) - 1))

    t = ((mean - mu0) / (s / math.sqrt(len(x))))
    return float(t)