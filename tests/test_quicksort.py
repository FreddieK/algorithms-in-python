import unittest
from algorithms.quicksort import QuickSort
from helpers import stanford


class TestQuickSort(unittest.TestCase):

    def test_expected_data_in_file(self):
        filename = 'QuickSort.txt'
        data = stanford.read_file(filename)
        self.assertEqual(data[0:4], [2148, 9058, 7742, 3153])

    def test_first_as_pivot_simple_sort(self):
        qs = QuickSort()
        list_ = list(range(0, 10))
        list_.reverse()
        qs.sort(list_)
        self.assertEqual(list_, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_first_as_pivot(self):
        qs = QuickSort()
        list_ = [0, 1, 2, 3, 4]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 0)

    def test_last_as_pivot_simple_sort(self):
        qs = QuickSort(pivot_strategy='last')
        list_ = list(range(0, 10))
        list_.reverse()
        qs.sort(list_)
        self.assertEqual(list_, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_last_as_pivot(self):
        qs = QuickSort(pivot_strategy='last')
        list_ = [0, 1, 2, 3, 4]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 4)

    def test_median_as_pivot_simple_sort(self):
        qs = QuickSort(pivot_strategy='median')
        list_ = list(range(0, 10))
        list_.reverse()
        qs.sort(list_)
        self.assertEqual(list_, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_median_as_pivot(self):
        qs = QuickSort(pivot_strategy='median')
        list_ = [0, 1, 2, 3, 4]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 2)

        list_ = [0, 1, 2, 3, 4, 5]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 2)

        list_ = [8, 2, 4, 5, 7, 1]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 4)

        list_ = [2, 5]
        pivot_point = qs._find_pivot(list_, 0, len(list_))
        self.assertEqual(pivot_point, 2)

    def test_sort_first_as_pivot(self):
        filename = 'QuickSort.txt'
        data = stanford.read_file(filename)
        qs = QuickSort()
        qs.sort(data)
        self.assertEqual(qs.comparisons, 162085)

    def test_sort_last_as_pivot(self):
        filename = 'QuickSort.txt'
        data = stanford.read_file(filename)
        qs = QuickSort(pivot_strategy='last')
        qs.sort(data)
        self.assertEqual(qs.comparisons, 164123)

    def test_sort_median_as_pivot(self):
        filename = 'QuickSort.txt'
        data = stanford.read_file(filename)
        qs = QuickSort(pivot_strategy='median')
        qs.sort(data)
        self.assertEqual(qs.comparisons, 138382)
