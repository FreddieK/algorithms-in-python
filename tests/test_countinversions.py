import unittest
from algorithms.countinversions import merge_sort, count_inversions


class TestCountInversions(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        filename = 'data/IntegerArray.txt'
        with open(filename) as f:
            content = f.readlines()
        self.data = [int(x.strip()) for x in content]

    def test_can_read_in_data_file(self):
        self.assertEqual(self.data[0:4], [54044, 14108, 79294, 29649])

    def test_working_merge_sort(self):
        shorter_sort = sorted(self.data[0:4])
        self.assertEqual(merge_sort(self.data[0:4]), shorter_sort)

        longer_sort = sorted(self.data[0:15])
        self.assertEqual(merge_sort(self.data[0:15]), longer_sort)

    def test_simple_count_inversions(self):
        _, inversions = count_inversions([1, 2, 3, 4, 5, 6])
        self.assertEqual(inversions, 0)

        _, inversions = count_inversions([2, 3, 4, 5, 6, 1])
        self.assertEqual(inversions, 5)

        _, inversions = count_inversions([1, 3, 5, 2, 4, 6])
        self.assertEqual(inversions, 3)

        _, inversions = count_inversions([6, 2, 3, 4, 5, 1])
        self.assertEqual(inversions, 9)

        _, inversions = count_inversions(self.data)
        self.assertEqual(inversions, 2407905288)
