import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    det = np.linalg.det(A)
    if det == 0 or len(A) != len(A[0]):
        return None
    swap_matrix = A.copy()
    aug_matrix = np.concatenate((swap_matrix, np.eye(len(A))), axis = 1)
    for i in range(len(A[0])):
        if aug_matrix[i][i] == 0:
            continue
        factor = 1 / aug_matrix[i][i]
        aug_matrix[i] = factor * aug_matrix[i]
        for j in range(len(aug_matrix)):
            if i == j:
                continue
            sub_fact = aug_matrix[j][i]
            aug_matrix[j] = aug_matrix[j] - ((sub_fact) * aug_matrix[i])
    aug_matrix = np.array(aug_matrix)
    cutoff_aug = int(len(aug_matrix[0]) / 2)
    return aug_matrix[0: cutoff_aug, cutoff_aug : cutoff_aug * 2 ]