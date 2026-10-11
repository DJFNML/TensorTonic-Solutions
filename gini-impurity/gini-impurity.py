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
    
    