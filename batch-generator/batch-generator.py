import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    random = np.random.default_rng(seed)
    new_perm = random.permutation(np.arange(len(X)))
    for start in range(0, len(X), batch_size):
        idx = new_perm[start:start + batch_size]
        if drop_last and len(idx) < batch_size:
            return
        yield X[idx], y[idx]
            