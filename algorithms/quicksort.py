class QuickSort:
    pivot_strategy = None

    def __init__(self, pivot_strategy='first'):
        self.pivot_strategy = pivot_strategy

    def sort(self, list_):
        length = len(list_)

        if length == 1:
            return list_

        pivot_point = self.choose_pivot(list_)

        for item in list_:
            # run through list and sort items smaller than pivot to the left,
            # and larger to the right

        # in the end, put pivot point at the end of the left part

        # recursively call function again with left and right partitions
        # if length == 1, just return list...


    def _choose_pivot(self, list_):
        # choose pivot point (pluggable selection mechanism)

        if self.pivot_strategy == 'first':
            return list_[0]
