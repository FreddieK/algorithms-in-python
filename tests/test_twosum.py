import unittest
from algorithms.twosum import TwoSum, TwoSumHash
from helpers import stanford


class TestTwoSum(unittest.TestCase):

    def test_can_search_for_x_y(self):
        list_ = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(TwoSum._find(1, 8, list_), True)
        self.assertEqual(TwoSum._find(1, 9, list_), False)
        self.assertEqual(TwoSum._find(1, 1, list_), False)
        self.assertEqual(TwoSum._find(3, 4, list_), True)

    def test_can_handle_negative_values(self):
        list_ = [-3, -2, -1, 4, 5, 6, 7]
        self.assertEqual(TwoSum._find(-3, -5, list_), True)
        self.assertEqual(TwoSum._find(-3, 3, list_), True)

    def test_can_search_full_list(self):
        list_ = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(TwoSum.search(9, list_), True)
        self.assertEqual(TwoSum.search(13, list_), True)
        self.assertEqual(TwoSum.search(14, list_), False)

    def test_can_search_list_of_values(self):
        list_ = [1, 2, 3, 4, 5, 6, 7]
        search_list = [9, 13, 14]
        expected_return = [True, True, False]
        self.assertEqual(TwoSum.search_list(search_list, list_), expected_return)

    @unittest.skip
    def test_can_read_data(self):
        filename = 'algo1-programming_prob-2sum.txt'
        list_ = stanford.read_file(filename)
        list_.sort()

        set_ = set(list_)

        search_list = list(range(-10000, 10001))
        search_results = TwoSumHash.search_list(search_list, set_)

        print(sum(search_results))
