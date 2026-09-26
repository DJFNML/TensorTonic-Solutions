import numpy as np

def meanminusnan(X:list):
    return np.nanmean(X, axis = 0)

def medianminusnan(X:list):
    return np.nanmedian(X, axis = 0)

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    X = np.array(X)
    method = {"mean": meanminusnan, "median":medianminusnan}
    
    imputed_vals = method[strategy](X)
    clean_imputed_vals = np.nan_to_num(imputed_vals)
    if X.ndim == 2:
        for i in range(len(X)):
            for j in range(len(X[i])):
                if np.isnan(X[i][j]):
                    X[i][j] = clean_imputed_vals[j]
    
        return np.array(X)
    else:
        for i in range(len(X)):
            if np.isnan(X[i]):
                X[i] = clean_imputed_vals
        return np.array(X)
    
    