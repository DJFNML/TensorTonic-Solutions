import numpy as np
def entropy(y:list) -> float:
    label_count = {}
    for x in y:
        if x in label_count:
            label_count[x] += 1
        else:
            label_count[x] = 1

    p_sum = 0
    for x in label_count:
        p_sum += (label_count[x] / len(y)) * np.log2(label_count[x] / len(y))

    return -p_sum
def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """
    # Write code here
    Y_L = []
    Y_R = []
    for i in range(len(y)):
        if split_mask[i] == True:
            Y_L.append(y[i])
        else:
            Y_R.append(y[i])

    N_L = len(Y_L) / (len(Y_L) + len(Y_R))
    N_R = len(Y_R) / (len(Y_L) + len(Y_R))

    return entropy(y) - (N_L * entropy(Y_L)) - (N_R * entropy(Y_R)) 