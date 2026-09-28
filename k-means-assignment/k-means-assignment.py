import math
def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    assigned = []
    for point in points:
        centroid = 0
        cent_distance = math.inf
        for i in range(len(centroids)):
            point_cent_distance = math.dist(centroids[i], point)
            if point_cent_distance < cent_distance:
                centroid = i
                cent_distance = point_cent_distance
        assigned.append(centroid)

    return assigned
            