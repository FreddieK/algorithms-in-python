import unittest
from algorithms.stanford2.primsMST import *


class TestPrimsMST(unittest.TestCase):

    def test_can_read_data(self):
        metadata, list_ = read_file()

        self.assertEqual(len(list_), 2184)
        self.assertEqual(metadata, [500, 2184])

    def test_selects_correct_edge(self):
        list_ = [[1, 2, 1],
                 [1, 3, 4],
                 [1, 4, 3],
                 [2, 4, 2],
                 [3, 4, 5]]

        prims = PrimsMST(4, list_, 1)
        self.assertEqual(prims._find_best_edge(), [1, 2, 1])
        self.assertEqual(prims._find_best_edge(), [2, 4, 2])
        self.assertEqual(prims._find_best_edge(), [1, 3, 4])

    def test_find_mst(self):
        list_ = [[1, 2, 1],
                 [1, 3, 4],
                 [1, 4, 3],
                 [2, 4, 2],
                 [3, 4, 5]]

        prims = PrimsMST(4, list_, 1)
        tree, cost = prims.find_mst()
        self.assertEqual(tree, {1, 2, 3, 4})
        self.assertEqual(cost, 7)

    @unittest.skip
    def test_with_stanford_data(self):
        metadata, list_ = read_file()

        prims = PrimsMST(metadata[0], list_, 1)
        tree, cost = prims.find_mst()
        self.assertEqual(len(tree), 500)
        print(cost)
