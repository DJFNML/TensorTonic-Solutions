def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    target_dict = dict.fromkeys(categories)
    for target in target_dict:
        target_dict[target] = [0,0]
    mean_dict = dict.fromkeys(categories, 0)
    cat_means = categories.copy()
    for i in range(len(categories)):
        target_dict[categories[i]][0] += targets[i]
        target_dict[categories[i]][1] += 1
    for target in mean_dict:
        if target_dict[target][1] == 0:
            mean_dict[target] = 0
        else:
            mean_dict[target] = target_dict[target][0] / target_dict[target][1]

    for i in range(len(categories)):
        cat_means[i] = float(mean_dict[categories[i]])

    return cat_means
        
                            
        