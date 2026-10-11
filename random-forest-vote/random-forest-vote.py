import numpy as np
def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    # Write code here
    result = []
    for i in range(len(predictions[0])):
        vote_dict = {}
        for j in range(len(predictions)):
            if predictions[j][i] in vote_dict:
                vote_dict[predictions[j][i]] += 1
            else:
                vote_dict[predictions[j][i]] = 1

        result.append(max(sorted(vote_dict), key = vote_dict.get))

    return result
        
        