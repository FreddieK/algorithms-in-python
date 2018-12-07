from operator import itemgetter

def read_file(filename='clustering1.txt'):
    """
    :return: Number of nodes, list of all edges
    """
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return int(content[0].strip()), \
           [[int(value) for value in line.strip().split()] for line in
            content[1:]]


def cluster_nodes(num_nodes, edges, target_num_clusters):
    """
    Find shortest distance and merges nodes into one
    Iterates until number of clusters is down to k

    :return:
    """
    edges = sorted(edges, key=itemgetter(2))

    clusters = {}
    for node in list(range(1, num_nodes + 1)):
        clusters[node] = node

    while target_num_clusters < len(set(clusters.values())):
        _merge_clusters(clusters, edges)

    cluster_lists = {}
    for node, cluster in clusters.items():
        if cluster not in cluster_lists.keys():
            cluster_lists[cluster] = [node]
        else:
            cluster_lists[cluster].append(node)

    return [cluster_list for cluster_list in cluster_lists.values()]


def _merge_clusters(clusters, edges):
    """
    Broken out to be able to test this piece of logic separately
    """
    shortest_edge = edges[0]
    new_cluster = clusters[shortest_edge[0]]
    old_cluster = clusters[shortest_edge[1]]

    for node, cluster in clusters.items():
        if cluster == old_cluster:
            clusters[node] = new_cluster
    del edges[0]


def max_spacing_between_clusters(clusters, edges):
    """
    Calculate the min distance between clusters

    :return: max spacing, int
    """
    max_spacing = None
    for cluster in clusters:
        for edge in edges:
            if (edge[0] in cluster) and (edge[1] not in cluster):
                if (max_spacing is None) or edge[2] < max_spacing:
                    print(edge)
                    max_spacing = edge[2]

    return max_spacing
