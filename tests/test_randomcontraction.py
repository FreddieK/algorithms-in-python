import unittest
from helpers import stanford
from algorithms.randomcontraction import RandomContraction


class TestRandomContraction(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        filename = 'kargerMinCut.txt'
        self.list_ = stanford.read_graph_file(filename)

    def test_expected_data_in_file(self):
        self.assertEqual(self.list_[5][0:5], [6, 155, 56, 52, 120])
        self.assertEqual(len(self.list_), 200)

    def test_can_fetch_lists(self):
        rc = RandomContraction(self.list_)
        vertices, edges = rc._get_lists()
        self.assertEqual(len(vertices), 200)
        self.assertEqual(len(edges), 2517)

    def test_can_contract_edges(self):
        contracted_edge = RandomContraction._contract_edges([0, 1], 1, 24)
        self.assertEqual(contracted_edge, [0, 24])

    def test_can_contract_graph(self):
        rc = RandomContraction(self.list_)
        vertices, edges = rc._get_lists()
        vertices_original_length = len(vertices)
        edges_original_length = len(edges)
        rc._contract_graph(vertices, edges)
        self.assertEqual(vertices_original_length, len(vertices) + 1)
        self.assertEqual(edges_original_length, len(edges) + 1)

    def test_can_iteratively_calculate_minimum_cut(self):
        rc = RandomContraction(self.list_, 10)
        rc.run()
        self.assertEqual(rc.minimumCut, 20)
