import numpy as np
def gini_individual(y: list) -> float:
    label_count = {}
    for x in y:
        if x in label_count:
            label_count[x] += 1
        else:
            label_count[x] = 1

    p_sum = 0
    for x in label_count:
        p_sum += (label_count[x] / len(y))**2

    return 1 - p_sum
    
def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    if len(y_left) + len(y_right) == 0:
        return 0
    
    N_L = len(y_left) / (len(y_left) + len(y_right))
    N_R = len(y_right) / (len(y_right) + len(y_left))
    
    G_L = gini_individual(y_left)
    G_R = gini_individual(y_right)
    return (N_L * G_L) +(N_R * G_R)
    
def decision_tree_split(X: list, y: list) -> list:
    """
    Returns the best feature index and threshold.
    """
    # Write code here
    parent_impurity = gini_individual(y)
    ginis = []
    pivots = []
    X = np.array(X)
    for i in range(len(X[0])):
        order = np.argsort(X[:, i])
        feature = X[order, i]
        y_sorted = [y[k] for k in order]
        feature_gini = -np.inf
        feature_pivot = 0
        y_left = []
        y_right = y_sorted.copy()
        for j in range(len(feature)-1):
            y_left.append(y_right.pop(0))
            if feature[j] == feature[j+1]:
                continue
            gini = gini_impurity(y_left, y_right)
            if parent_impurity - gini > feature_gini: 
                feature_pivot = (feature[j] + feature[j+1])/2
                feature_gini = parent_impurity - gini
        
        ginis.append(feature_gini)
        pivots.append(feature_pivot)

    feature = np.argmax(ginis)
    pivot = pivots[feature]

    return [feature, pivot]
    
    
                
    