import unittest
from helpers.stanford import read_weighted_graph_file
from algorithms.dijkstrasshortestpath import *


class TestDijkstrasShortestPath(unittest.TestCase):

    def test_can_load_data(self):
        data = read_weighted_graph_file('dijkstraData.txt')

        vertex_2 = [(42, 1689), (127, 9365), (5, 8026), (170, 9342), (131, 7005),
         (172, 1438), (34, 315), (30, 2455), (26, 2328), (6, 8847),
         (11, 1873), (17, 5409), (157, 8643), (159, 1397), (142, 7731),
         (182, 7908), (93, 8177)]

        self.assertEqual(data[2], vertex_2)

    def test_can_calculate_cost(self):
        test_graph = { 1: [(2, 10)],
                       2: [(1, 10), (3, 10)],
                       3: [(2, 10)]
                      }

        explored = set()
        explored.add(1)
        min_cost = dict()
        min_cost[1] = 0

        vertices, costs = calculate_costs(test_graph, explored, min_cost)

        self.assertEqual(vertices, [2])
        self.assertEqual(costs, [10])

    def test_selects_minimum_vertex(self):
        test_graph = { 1: [(2, 10), (3, 5)],
                       2: [(3, 10)]
                    }

        explored = set()
        explored.add(1)
        min_cost = dict()
        min_cost[1] = 0

        vertex, cost = explore_vertex(test_graph, explored, min_cost)

        self.assertEqual(vertex, 3)
        self.assertEqual(cost, 5)

    def test_traverse_graph(self):
        test_graph = {
            1: [(2, 10), (3, 20), (4, 30)],
            2: [(1, 10), (4, 10), (5, 20)],
            3: [(1, 20), (5, 30)],
            4: [(2, 10), (6, 10)],
            5: [(2, 20), (3, 30)],
            6: [(4, 10)]
        }

        start_vertex = 1
        shortest_paths = dijkstras_shortest_path(test_graph, start_vertex)

        self.assertEqual(shortest_paths[1], 0)
        self.assertEqual(shortest_paths[2], 10)
        self.assertEqual(shortest_paths[3], 20)
        self.assertEqual(shortest_paths[6], 30)

    def test_can_handle_non_connected_graph(self):
        test_graph = {
            1: [(2, 10), (3, 20), (4, 30)],
            2: [(1, 10), (4, 10), (5, 20)],
            3: [(1, 20), (5, 30)],
            4: [(2, 10), (6, 10)],
            5: [(2, 20), (3, 30)],
            6: [(4, 10)],
            7: [(8, 10)],
            8: [(7, 10)]
        }

        start_vertex = 1
        shortest_paths = dijkstras_shortest_path(test_graph, start_vertex)
        self.assertEqual(shortest_paths[8], 1000000)

