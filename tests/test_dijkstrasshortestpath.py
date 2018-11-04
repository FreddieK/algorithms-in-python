import unittest
from helpers.stanford import read_weighted_graph_file


class TestDijkstrasShortestPath(unittest.TestCase):
    # test can load data
    # blubb

    def test_can_load_data(self):
        data = read_weighted_graph_file('dijkstraData.txt')

        vertex_2 = [2, (42, 1689), (127, 9365), (5, 8026), (170, 9342), (131, 7005),
         (172, 1438), (34, 315), (30, 2455), (26, 2328), (6, 8847),
         (11, 1873), (17, 5409), (157, 8643), (159, 1397), (142, 7731),
         (182, 7908), (93, 8177)]

        self.assertEqual(data[1], vertex_2)

    def test_next_thing(self):
        self.fail()
