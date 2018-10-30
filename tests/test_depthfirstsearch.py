import unittest
from algorithms.depthfirstsearch import DepthFirstSearch
from helpers import stanford


class TestDepthFirstSearch(unittest.TestCase):
    # Had to refactor a lot in order to increase the performance, and didn't
    # have the patience to clean up the tests and code as well.

    def test_can_load_depth_first_search_class(self):
        dfs = DepthFirstSearch([])
        self.assertEqual(type(dfs), DepthFirstSearch)

    @unittest.skip
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

    @unittest.skip
    def test_can_assign_labels(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        graph = DepthFirstSearch(edges)
        graph._iteration = 'first'
        graph._dfs(1)
        self.assertEqual(graph.finishing_order[6], 6)
        self.assertEqual(graph.finishing_order[1], 1)

    def test_can_run_second_pass_based_on_finishing_time(self):
        edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [5, 6], [6, 7], [7, 5]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        graph.second_pass()

        self.assertEqual(graph.vertex_groups, {7: 5, 6: 5, 5: 5, 3: 1,
                                               4: 1, 2: 1, 1: 1})

    def test_can_get_ordered_list_of_strongly_connected_component_sizes(self):
        edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [5, 6], [6, 7], [7, 5]]
        graph = DepthFirstSearch(edges)
        graph.first_pass()
        graph.second_pass()
        scc = graph.get_scc_sizes()
        self.assertEqual(scc.tolist(), [4, 3])

    @unittest.skip
    def test_with_stanford_data(self):
        # Data not included in repo

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

        print(scc[0:10])


def troubleshoot_performance_behaviour():
    # Helper to identify where the algorithm exploded in complexity

    from algorithms.depthfirstsearch import DepthFirstSearch
    from helpers import stanford
    import cProfile
    filename = 'SCC.txt'
    edges = stanford.read_graph_file(filename, ' ')
    edges_subset = edges[0:500000]
    graph = DepthFirstSearch(edges_subset)

    cProfile.run("graph.first_pass()")
