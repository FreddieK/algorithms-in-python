import unittest
#from algorithms.countinversions import merge_sort, count_inversions
import algorithms as algo

#from helpers.stanford import read_file

from algorithms.quicksort import QuickSort
from helpers import stanford


class TestCountInversions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        filename = 'QuickSort.txt'
        self.data = stanford.read_file(filename)

    def test_expected_data_in_file(self):
        self.assertEqual(self.data[0:4], [2148, 9058, 7742, 3153])

    def test_list_with_one_item_returns_item(self):
        qs = QuickSort()
        self.assertEqual(qs.sort([1]), [1])

    def test_pivot_strategy_first_returns_first_item_in_list(self):
        qs = QuickSort()
        pivot = qs._choose_pivot([0, 1, 2])
        self.assertEqual(pivot, 0)