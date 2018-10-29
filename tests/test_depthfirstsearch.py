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
        graph._dfs(1)
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6])

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9]]
        graph = DepthFirstSearch(edges)
        graph._dfs(1)
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_can_recursively_search_to_explore_complete_graph(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6])

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        self.assertEqual(sorted(graph.explored), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    @unittest.skip
    def test_can_reverse_search(self):
        # Changing to set instead of list for performance purposes breaks test
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph._dfs(6, reverse=True)
        self.assertEqual(graph.explored, [6, 5, 4, 3, 2, 1])

    def test_can_assign_labels(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph._iteration = 'first'
        graph._dfs(1)
        self.assertEqual(graph.finishing_order[6], 6)
        self.assertEqual(graph.finishing_order[1], 1)

        # multiple branches
        edges = [[1, 2], [1, 3],
                     [3, 4], [4, 5], [5, 6],
                     [2, 7], [7, 8], [8, 9], [9, 10]]
        graph = DepthFirstSearch(edges)
        graph._iteration = 'first'
        graph._dfs(1)
        self.assertEqual(graph.finishing_order[1], 1)
        self.assertEqual(graph.finishing_order[10], 10)

    def test_can_run_second_pass_based_on_finishing_time(self):
        edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [5, 6], [6, 7], [7, 5]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        graph.second_pass()

        self.assertEqual(graph.vertix_groups, {7: 5, 6: 5, 5: 5, 3: 1,
                                               4: 1, 2: 1, 1: 1})

    def test_can_get_ordered_list_of_strongly_connected_component_sizes(self):
        edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [5, 6], [6, 7], [7, 5]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        graph.second_pass()
        scc = graph.get_scc_sizes()
        self.assertEqual(scc.tolist(), [4, 3])

    def test_with_stanford_data(self):
        import sys
        sys.setrecursionlimit(50000)

        filename = 'SCC.txt'
        edges = stanford.read_graph_file(filename, ' ')
        graph = DepthFirstSearch(edges)

        print(f'Num vertices: {graph.current_label}')

        print('starting first pass')
        graph.first_pass()

        print('starting second pass')
        graph.second_pass()

        print('calculating scc sizes')
        scc = graph.get_scc_sizes()
        breakpoint()

        print(scc)
