import unittest
from algorithms.countinversions import merge_sort


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

    @unittest.skip
    def test_simple_count_inversions(self):
        self.assertEqual(count_inversions([1]), 0)
        self.assertEqual(count_inversions([1, 5, 4]), 1)

        #self.assertEqual(count_inversions([1, 5, 4, 3]), 3)