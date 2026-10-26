import math
import numpy as np

def gaussian_naive_bayes(X_train: list, y_train: list, X_test: list) -> list:
    """
    Returns a predicted class label for every test sample.
    """
    # Write code here
    data = {}
    for i in range(len(y_train)):
        y = y_train[i]
        if y in data: 
            data[y].append(X_train[i])
        else:
            data[y] = [X_train[i]]
    probs = {}
    for dat in data:
        data[dat] = np.array(data[dat])
        probs[dat] = [[], []]
        probs[dat][0] = sum(data[dat]) / len(data[dat])
        probs[dat][1] = (sum((data[dat] - probs[dat][0])**2) / len(data[dat])) + np.exp(-9)

    y_test = []
    for x in X_test:
        p_value = 0
        pred = 0
        for prob in probs:
            new_p = np.prod((1 / np.sqrt(2 * math.pi * probs[prob][1])) * np.exp((-(x - probs[prob][0])**2) / (2*probs[prob][1])))
            if (new_p >= p_value and p_value == 0) or (new_p > p_value):
                p_value = new_p
                pred = prob
        y_test.append(pred)
    return y_test
            

    
        

    