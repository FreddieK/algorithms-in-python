import unittest
from algorithms.depthfirstsearch import DepthFirstSearch
from helpers import stanford

class TestDepthFirstSearch(unittest.TestCase):

    def test_can_load_depth_first_search_class(self):
        dfs = DepthFirstSearch([])
        self.assertEqual(type(dfs), DepthFirstSearch)

    def test_can_do_simple_search(self):
        # perform search to find sinks
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph.dfs(1)
        self.assertEqual(graph.explored, [1, 2, 3, 4, 5, 6])

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9]]
        graph = DepthFirstSearch(edges)
        graph.dfs(1)
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_can_recursively_search_to_explore_complete_graph(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph.dfs_loop()
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6])

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9]]
        graph = DepthFirstSearch(edges)
        graph.dfs_loop()
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_can_reverse_search(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph.dfs(6, reverse=True)
        self.assertEqual(graph.explored, [6, 5, 4, 3, 2, 1])
        # Call the graph object with a reverse flag to search backwards

    def test_can_assign_labels(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph.dfs(1)
        #self.assertEqual(graph.explored, [1, 2, 3, 4, 5, 6])
        self.assertEqual(graph.labels[6], 6)
        self.assertEqual(graph.labels[1], 1)

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9], [9, 10]]
        graph = DepthFirstSearch(edges)
        graph.dfs(1)
        self.assertEqual(graph.labels[1], 1)
        self.assertEqual(graph.labels[10], 10)

    def test_can_get_fully_connected_parts(self):
        @pass

    @unittest.skip
    def test_can_read_data(self):
        filename = 'SCC.txt'
        vertices = stanford.read_graph_file(filename, ' ')
        self.assertEqual(vertices[0], [1, 1])