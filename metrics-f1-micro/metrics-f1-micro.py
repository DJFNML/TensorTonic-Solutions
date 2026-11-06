def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    accurate = 0
    total = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_true[i]:
            accurate += 1
        total += 1

    return round(float(accurate / total),4)