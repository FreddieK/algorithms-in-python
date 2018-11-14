import math


class Heap:

    def __init__(self, order='min'):
        # order: min or max
        self.order = order
        self.tree = {}

    def insert(self, value):
        insert_index = len(self.tree) + 1
        self.tree[insert_index] = value

        if len(self.tree) > 1:
            self._bubble_up(insert_index)

    def _bubble_up(self, newly_inserted_index):
        parent_index = math.floor(newly_inserted_index / 2)
        if (self.order == 'min' and
                self.tree[newly_inserted_index] < self.tree[parent_index]) \
            or (self.order == 'max' and
                self.tree[newly_inserted_index] > self.tree[parent_index]):

            self.tree[newly_inserted_index], self.tree[parent_index] = \
                self.tree[parent_index], self.tree[newly_inserted_index]
            if parent_index != 1:
                self._bubble_up(parent_index)

    def _bubble_down(self, parent_index):
        # Overly complex due to supporting both min and max case, refactor?

        left_child_index = 2*parent_index
        right_child_index = 2*parent_index + 1

        if len(self.tree) == left_child_index:
            child_index = left_child_index
        else:
            if (self.order == 'min' and
                self.tree[left_child_index] < self.tree[right_child_index]) \
                or (self.order == 'max' and
                    self.tree[left_child_index] > self.tree[right_child_index]):
                child_index = left_child_index
            else:
                child_index = right_child_index

        if (self.order == 'min' and
            self.tree[child_index] < self.tree[parent_index]) \
            or (self.order == 'max' and
                self.tree[child_index] > self.tree[parent_index]):
            self.tree[child_index], self.tree[parent_index] = \
                self.tree[parent_index], self.tree[child_index]

            if len(self.tree) >= 2*child_index:
                self._bubble_down(child_index)

    def extract(self):
        extract_value = self.tree[1]
        max_index = len(self.tree)
        self.tree[1] = self.tree[max_index]
        del self.tree[max_index]

        if len(self.tree) > 1:
            self._bubble_down(1)

        return extract_value


class MedianMaintenance:

    def __init__(self):
        self.max_heap = Heap('max')
        self.min_heap = Heap()
        self.medians = []

    def insert(self, value):
        if len(self.max_heap.tree) == 0:
            self.max_heap.insert(value)
            self.medians.append(self.max_heap.tree[1])
            return
        elif len(self.min_heap.tree) == 0:
            if value < self.max_heap.tree[1]:
                self.max_heap.insert(value)
                move_value = self.max_heap.extract()
                self.min_heap.insert(move_value)
            else:
                self.min_heap.insert(value)
            self.medians.append(self.max_heap.tree[1])
            return

        if value <= self.max_heap.tree[1]:
            self.max_heap.insert(value)
            if (len(self.max_heap.tree) - len(self.min_heap.tree)) > 1:
                move_value = self.max_heap.extract()
                self.min_heap.insert(move_value)
        elif value >= self.min_heap.tree[1]:
            self.min_heap.insert(value)
            if (len(self.min_heap.tree) - len(self.max_heap.tree)) > 1:
                move_value = self.min_heap.extract()
                self.max_heap.insert(move_value)
        else:
            if len(self.max_heap.tree) == len(self.min_heap.tree):
                self.max_heap.insert(value)
            elif len(self.max_heap.tree) > len(self.min_heap.tree):
                self.min_heap.insert(value)
            elif len(self.max_heap.tree) < len(self.min_heap.tree):
                self.max_heap.insert(value)

        if len(self.max_heap.tree) == len(self.min_heap.tree):
            self.medians.append(self.max_heap.tree[1])
        elif len(self.max_heap.tree) > len(self.min_heap.tree):
            self.medians.append(self.max_heap.tree[1])
        elif len(self.max_heap.tree) < len(self.min_heap.tree):
            self.medians.append(self.min_heap.tree[1])

    def loop_insert(self, list_):
        for value in list_:
            self.insert(value)

    def modulo_median(self, modulo=10000):
        return sum(self.medians) % modulo