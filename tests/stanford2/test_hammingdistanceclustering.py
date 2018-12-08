from algorithms.stanford2.hammingdistanceclustering import *
import pytest

def test_reads_file_correctly():
    nodes, num_nodes, num_bits = read_file()

    assert nodes.shape == (num_nodes, num_bits)
    assert nodes.shape == (200000, 24)


def test_clustering():
    nodes = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    nodes = np.array(nodes)
    clusters = cluster_nodes_v2(nodes, 1)

    assert len(clusters) == 1

    nodes = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 1]
    ]
    nodes = np.array(nodes)
    clusters = cluster_nodes_v2(nodes, 1)

    assert len(clusters) == 2

    nodes = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ]
    nodes = np.array(nodes)
    clusters = cluster_nodes_v2(nodes, 2)

    assert len(clusters) == 1


@pytest.mark.skip(reason="No actual test")
def test_with_stanford_data():
    nodes, num_nodes, num_bits = read_file()
    clusters = cluster_nodes_v2(nodes, 2)
    len(clusters)
