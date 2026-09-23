from collections import Counter
import numpy as np
            
        

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x.sort()
    x_dic = {}
    for i in x:
        if i in x_dic:
            x_dic[i] += 1
        else:
            x_dic[i] = 1

    mode = max(x_dic, key = x_dic.get)

    mean = 0
    for i in x_dic:
        mean += i * x_dic[i]
    mean = mean / len(x)

    median = 0
    if len(x) % 2 == 0:
        median = (x[int(len(x) / 2) - 1] + x[int((len(x) + 2) / 2) - 1]) / 2
    else:
        median = x[int((len(x) + 1) / 2) - 1]

    return {"mean": float(mean), "median": float(median), "mode": float(mode)}