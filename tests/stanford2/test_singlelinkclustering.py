from algorithms.stanford2.singlelinkclustering import *
from algorithms.stanford2.singlelinkclustering import _merge_clusters
import pytest


def test_reads_file_correctly():
    num_nodes, edges = read_file()
    assert num_nodes == 500
    assert len(edges) == 124750
    assert edges[0] == [1, 2, 6808]


def test_can_cluster():
    edges = [[1, 2, 1], [1, 3, 10], [1, 4, 10], [2, 3, 10], [3, 4, 1]]
    clusters = cluster_nodes(4, edges, 2)
    assert len(clusters) == 2
    assert clusters == [[1, 2], [3, 4]]

    edges = [
        [1, 2, 1],
        [2, 3, 1],
        [2, 4, 5],
        [2, 5, 6],
        [5, 6, 3],
        [6, 7, 3]
    ]
    clusters = cluster_nodes(7, edges, 2)
    assert len(clusters) == 2
    assert clusters == [[1, 2, 3, 4], [5, 6, 7]]


def test_can_cluster_reversed_graph():
    # Reverse edge direction
    edges = [
        [2, 1, 1],
        [3, 2, 1],
        [4, 2, 5],
        [5, 2, 6],
        [6, 5, 3],
        [7, 6, 3]
    ]
    clusters = cluster_nodes(7, edges, 2)
    assert len(clusters) == 2
    assert clusters == [[1, 2, 3, 4], [5, 6, 7]]


def test_can_merge_single_iteration():
    clusters = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    edges = [[1, 2, 1], [2, 3, 1], [5, 6, 3], [6, 7, 3], [2, 4, 5], [2, 5, 6]]

    _merge_clusters(clusters, edges)
    assert clusters == {1: 1, 2: 1, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

    _merge_clusters(clusters, edges)
    assert clusters == {1: 1, 2: 1, 3: 1, 4: 4, 5: 5, 6: 6, 7: 7}

    _merge_clusters(clusters, edges)
    assert clusters == {1: 1, 2: 1, 3: 1, 4: 4, 5: 5, 6: 5, 7: 7}


@pytest.mark.skip(reason="No actual test")
def test_max_spacing_stanford_data():
    num_nodes, edges = read_file()
    clusters = cluster_nodes(num_nodes, edges, 4)
    max_spacing = max_spacing_between_clusters(clusters, edges)
    print(max_spacing)
