import numpy as np
def stratified_split(X, y, test_size=0.2, seed=42):
    X = np.asarray(X)
    y = np.asarray(y)
    rng = np.random.default_rng(seed)
    train_indices = []
    test_indices = []
    for label in np.unique(y):
        indices = rng.permutation(np.flatnonzero(y == label))
        test_count = int(round(indices.size * test_size))
        if indices.size > 1:
            test_count = min(test_count, indices.size - 1)
        test_indices.extend(indices[:test_count])
        train_indices.extend(indices[test_count:])
    train_indices = np.sort(np.asarray(train_indices, dtype=int))
    test_indices = np.sort(np.asarray(test_indices, dtype=int))
    return {
        "X_train": X[train_indices], "X_test": X[test_indices],
        "y_train": y[train_indices], "y_test": y[test_indices],
    }

'''def stratified_split(X: list, y: list, test_size: float = 0.2, seed: int = 42) -> dict:
    """
    Returns a dictionary with X_train, X_test, y_train, and y_test.
    """
    # Write code here
    random = np.random.default_rng(seed)
    
    X_test_size = round(test_size * len(X))
    if X_test_size == len(X):
        X_test_size -= 1
    X_train_size = len(X) - X_test_size

    y_test_size = round(test_size * len(y))
    if y_test_size == len(y):
        y_test_size -= 1
    y_train_size = len(y) - y_test_size

    X = random.permutation(X)
    y = random.permutation(y)
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for i in range(X_test_size):
        X_test.append(X[i])
    for i in range(X_test_size, len(X)):
        X_train.append(X[i])

    for i in range(y_test_size):
        y_test.append(y[i])
    for i in range(y_test_size, len(y)):
        y_train.append(y[i])

    
    return {"X_train": np.array(X_train), "X_test": np.array(X_test), "y_train": np.array(y_train), "y_test": np.array(y_test)}
    
    My attempt didn't pair X and y indices properly :/ Also didn't look at unique values, samples come out shuffled, and doesn't properly fulfill the 1 value training set properly'''