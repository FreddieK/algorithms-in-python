import unittest
from algorithms.medianmaintenance import Heap, MedianMaintenance
from helpers import stanford


class TestMedianMaintenance(unittest.TestCase):

    def test_can_insert_into_heap(self):
        min_heap = Heap()
        self.assertEqual(len(min_heap.tree), 0)
        min_heap.insert(5)
        self.assertEqual(len(min_heap.tree), 1)
        min_heap.insert(5)
        self.assertEqual(len(min_heap.tree), 2)

    def test_min_heap_gets_sorted(self):
        heap = Heap()
        self.assertEqual(len(heap.tree), 0)
        heap.insert(5)
        heap.insert(3)
        self.assertEqual(heap.tree, {1: 3, 2: 5})

        heap.insert(3)
        heap.insert(1)
        self.assertEqual(heap.tree, {1: 1, 2: 3, 3: 3, 4: 5})

    def test_max_heap_gets_sorted(self):
        heap = Heap('max')
        self.assertEqual(len(heap.tree), 0)
        heap.insert(5)
        heap.insert(3)
        self.assertEqual(heap.tree, {1: 5, 2: 3})

        heap.insert(3)
        heap.insert(6)
        self.assertEqual(heap.tree, {1: 6, 2: 5, 3: 3, 4: 3})

    def test_supports_min_extraction(self):
        heap = Heap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(3)
        heap.insert(1)
        heap.insert(7)
        extract_min = heap.extract()
        self.assertEqual(extract_min, 1)
        self.assertEqual(heap.tree, {1: 3, 2: 3, 3: 7, 4: 5})

    def test_supports_max_extraction(self):
        heap = Heap('max')
        heap.insert(5)
        heap.insert(3)
        heap.insert(3)
        heap.insert(1)
        heap.insert(7)
        extract_max = heap.extract()
        self.assertEqual(extract_max, 7)
        self.assertEqual(heap.tree, {1: 5, 2: 3, 3: 3, 4: 1})

    def test_median_maintenance_inserts(self):
        mm = MedianMaintenance()
        mm.insert(5)
        mm.insert(5)
        mm.insert(5)
        mm.insert(5)
        self.assertEqual(mm.max_heap.tree, {1: 5, 2: 5})
        self.assertEqual(mm.min_heap.tree, {1: 5, 2: 5})

        mm = MedianMaintenance()
        mm.insert(3)
        mm.insert(5)
        self.assertEqual(mm.max_heap.tree, {1: 3})
        self.assertEqual(mm.min_heap.tree, {1: 5})

        mm = MedianMaintenance()
        mm.insert(5)
        mm.insert(3)
        self.assertEqual(mm.max_heap.tree, {1: 3})
        self.assertEqual(mm.min_heap.tree, {1: 5})

        mm = MedianMaintenance()
        mm.insert(5)
        mm.insert(3)
        mm.insert(1)
        mm.insert(2)
        mm.insert(4)
        mm.insert(6)
        mm.insert(8)
        mm.insert(7)
        mm.insert(9)
        self.assertEqual(mm.max_heap.tree, {1: 4, 2: 3, 3: 2, 4: 1})
        self.assertEqual(mm.min_heap.tree, {1: 5, 2: 7, 3: 6, 4: 8, 5: 9})

        mm = MedianMaintenance()
        mm.insert(1)
        mm.insert(2)
        mm.insert(3)
        mm.insert(5)
        mm.insert(6)
        mm.insert(7)
        mm.insert(4)
        self.assertEqual(mm.max_heap.tree, {1: 4, 2: 3, 3: 2, 4: 1})
        self.assertEqual(mm.min_heap.tree, {1: 5, 2: 7, 3: 6})

    def test_median_is_calculated_correctly(self):
        mm = MedianMaintenance()

        mm.insert(1)
        self.assertEqual(mm.medians[0], 1)

        mm.insert(2)
        self.assertEqual(mm.medians[1], 1)

        mm.insert(3)
        # 1, 2, 3
        self.assertEqual(mm.medians[2], 2)

        mm.insert(6)
        # 1, 2, 3, 6
        self.assertEqual(mm.medians[3], 2)

        mm.insert(1)
        # 1, 1, 2, 3, 6
        self.assertEqual(mm.medians[4], 2)

        mm.insert(1)
        # 1, 1, 1, 2, 3, 6
        self.assertEqual(mm.medians[5], 1)

    def test_can_iterate_list(self):
        numbers_to_insert = [5, 2, 3, 6, 2, 1]
        mm = MedianMaintenance()
        mm.loop_insert(numbers_to_insert)
        self.assertEqual(mm.medians, [5, 2, 3, 3, 3, 2])

    def test_can_get_modulo(self):
        numbers_to_insert = [4, 3, 3, 3]
        mm = MedianMaintenance()
        mm.loop_insert(numbers_to_insert)
        self.assertEqual(mm.modulo_median(4), 1)

    def test_can_read_in_file(self):
        filename = 'Median.txt'
        numbers = stanford.read_file(filename)
        mm = MedianMaintenance()
        mm.loop_insert(numbers)
        print(mm.modulo_median())