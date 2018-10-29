import unittest
from helpers import stanford
from algorithms.depthfirstsearch import DepthFirstSearch

class TestDepthFirstSearch(unittest.TestCase):
    # As the test data (SCC.txt) isn't included in the repo, these tests will
    # fail unless the data file is downloaded separately

    # @classmethod
    # def setUpClass(self):
    #     filename = 'SCC.txt'
    #     self.list_ = stanford.read_graph_file(filename, ' ')

    @unittest.skip
    def test_can_read_data(self):
        self.assertEqual(self.list_[0], [1, 1])

    def test_can_load_depth_first_search_class(self):
        dfs = DepthFirstSearch()
        self.assertEqual(type(dfs), DepthFirstSearch)

    def test_can_do_simple_search(self):
        # Construct simple graph
        # perform search to find sinks

    @unittest.skip
    def test_can_reverse_search(self):
        # Call the graph object with a reverse flag to search backwards
        #