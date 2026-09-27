import numpy as np

def kfold_split(N: int, k: int, shuffle: bool = True, seed: int = 0) -> list:
    """
    Returns a list of dictionaries with train_idx and val_idx.
    """
    # Write code here
    fold_size = np.floor(N/k)
    spill_over = N - (k*fold_size)
    fold_dict = []
    indices = np.arange(N)
    if shuffle == True:
        random = np.random.default_rng(seed)
        indices = random.permutation(indices)
    for i in range(k):
        fold_dict.append([])
    counter = 0
    fold = 0
    while fold < k: 
        for i in range(int(fold_size)):
            fold_dict[fold].append(indices[counter])
            counter+=1
        if spill_over > 0:
            fold_dict[fold].append(indices[counter])
            counter+=1
            spill_over -= 1
        fold +=1
            
    split_dict_list = []
    for i in range(k):
        val_set = np.array(fold_dict[i])
        train_set = []
        for j in range(k):
            if j == i:
                continue 
            else:
                train_set += fold_dict[j]
        split_dict = {"train_idx": np.array(train_set), "val_idx": val_set}
        split_dict_list.append(split_dict)

    return split_dict_list
            
        