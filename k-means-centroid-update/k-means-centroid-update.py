import numpy as np

def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    centroids = {}
    for i in range(len(points)):
        if assignments[i] in centroids:
            centroids[assignments[i]]+= [points[i]]
        else:
            centroids[assignments[i]] = [points[i]]

    centres = []
    centre_dim = 0
    for centroid in centroids:
        cluster = centroids[centroid]
        cluster = np.array(cluster)
        centre_dim = len(cluster[0])
        centre = np.zeros(centre_dim)
        centre = np.array(centre)
        
        for i in range(len(cluster)):
            centre += cluster[i]
        centre = centre / len(cluster)
        centres.append(list(centre))
    for i in range(k):
        if i not in centroids:
            centres.append(list(np.zeros(centre_dim)))
    
    return centres