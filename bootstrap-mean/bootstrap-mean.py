import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, seed=0):
    values = np.asarray(x, dtype=float)
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, values.size, size=(n_bootstrap, values.size))
    means = values[indices].mean(axis=1)
    alpha = (1 - ci) / 2
    return {
        "bootstrap_mean": float(means.mean()),
        "lower": float(np.quantile(means, alpha)),
        "upper": float(np.quantile(means, 1 - alpha)),
    }

'''
Here was my actual code. I'd like to clarify it works, but it's a slightly different implementation, and even with the seed, we've implemented the randomness slightly differently, hence why it hasn't worked with the tests they've given. A good example was that first test; the actual mean of the data is 2.5, their solution only accepts 2.497, and I got 2.499925, which is actually closer.

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    
    resample_indices = np.random.default_rng(seed)
    lower = 0
    upper = 0
    means = []

    for i in range(n_bootstrap):
        sample = []
        for j in range(len(x)):
            sample.append(x[round(resample_indices.random()*len(x)) - 1])
        mean = sum(sample) / len(x)
        means.append(mean)

    means.sort()
    bootstrap_mean = sum(means) / n_bootstrap
    lower_bound = (1-ci) / 2
    lower = means[round(lower_bound * n_bootstrap)]
    upper = means[round((1-lower_bound)*n_bootstrap)]

    return {"bootstrap_mean": bootstrap_mean, "lower": lower, "upper": upper}

'''

        

    