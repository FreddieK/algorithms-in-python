import numpy as np
import pandas as pd


def read_file(filename='clustering_big.txt'):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()

    num_nodes, num_bits = [int(value) for value in content[0].strip().split()]
    nodes = [[int(bit) for bit in node.split()] for node in content[1:]]

    return np.array(nodes), num_nodes, num_bits


def cluster_nodes(nodes, max_distance=2):
    clusters = []

    for index, node in enumerate(nodes):

        node_distances = nodes - node
        node_distances = np.sum(node_distances.__abs__(), axis=1)
        index_in_cluster = (node_distances <= max_distance)

        nodes_in_cluster = nodes[index_in_cluster]
        clusters.append(nodes_in_cluster) if len(nodes_in_cluster) > 0 else None
        nodes = nodes[~index_in_cluster]

        if index % 1000 == 0:
            print(index, len(clusters), len(nodes))
    return clusters


def cluster_nodes_v2(nodes, max_distance=2):
    clusters = {}

    nodes_to_explore_in_cluster = []
    cluster_num = 0
    iteration = 0

    while len(nodes) > 0:
        if len(nodes_to_explore_in_cluster) > 0:
            node = np.array(nodes_to_explore_in_cluster[0])
            del nodes_to_explore_in_cluster[0]
        else:
            cluster_num += 1
            node = nodes[0]
            nodes = np.delete(nodes, 0, 0)
            clusters[cluster_num] = [node.tolist()]

        node_distances = nodes - node
        node_distances = np.sum(node_distances.__abs__(), axis=1)
        index_in_cluster = (node_distances <= max_distance)

        nodes_in_cluster = nodes[index_in_cluster]
        nodes_to_explore_in_cluster = nodes_to_explore_in_cluster + \
                                      nodes_in_cluster.tolist()

        nodes = nodes[~index_in_cluster]

        clusters[cluster_num] = clusters[cluster_num] + \
                                nodes_in_cluster.tolist()

        if iteration % 1000 == 0:
            print(iteration, len(clusters), len(nodes))
        iteration += 1

    return clusters
