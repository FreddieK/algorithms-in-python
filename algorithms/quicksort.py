import math
import statistics


class QuickSort:

    def __init__(self, pivot_strategy='first'):
        self.comparisons = 0
        self.pivot_strategy = pivot_strategy

    def sort(self, list_):
        left = 0
        right = len(list_)
        self._sort(list_, left, right)

    def _sort(self, list_, l, r):
        length = len(list_[l:r])
        if length <= 1:
            return
        self.comparisons += length - 1

        pivot_point = self._find_pivot(list_, l, r)

        self._partition(list_, l, r)
        pivot_position = list_.index(pivot_point)

        self._sort(list_, l, pivot_position)
        self._sort(list_, pivot_position+1, r)

    def _find_pivot(self, list_, l, r):
        # 'first' is the implicit default case
        if self.pivot_strategy == 'last':
            list_[l], list_[r-1] = list_[r-1], list_[l]
        elif self.pivot_strategy == 'median':
            m = math.floor((l+r-1)/2)
            median_list = [list_[l], list_[m], list_[r-1]]
            median_pivot = statistics.median(median_list)
            median_index = list_.index(median_pivot)
            list_[l], list_[median_index] = list_[median_index], list_[l]
        return list_[l]

    @staticmethod
    def _partition(list_, l, r):
        p = list_[l]
        i = l + 1
        for j in list(range(l+1, r)):
            if list_[j] < p:
                list_[j], list_[i] = list_[i], list_[j]
                i += 1
        list_[l], list_[i-1] = list_[i-1], list_[l]
