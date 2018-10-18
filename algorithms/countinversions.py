import math


def merge_sort(list):
    # Basic implementation of merge sort algorithm, in preparation for
    # implementing the count-array-inversions algorithm

    length = len(list)

    if length <= 1:
        return list

    split_point = math.ceil(length / 2)
    x = merge_sort(list[:split_point])
    y = merge_sort(list[split_point:])

    i = 0
    j = 0
    sorted_list = []

    for k in range(length):
        try:
            if x[i] < y[j]:
                sorted_list.append(x[i])
                i += 1
            else:
                sorted_list.append(y[j])
                j += 1
        except IndexError:
            if len(x) <= i:
                sorted_list.append(y[j])
                j += 1
            elif len(y) <= j:
                sorted_list.append(x[i])
                i += 1

    return sorted_list


def _count_split_inversions():
    pass


def count_inversions(array):
    # O(n log(n)) algorithm for counting array inversions
    # https://lagunita.stanford.edu/courses/course-v1:Engineering+Algorithms1+SelfPaced/info

    length = len(array)

    if length == 1:
        return 0

    split_point = math.ceil(length / 2)
    x = count_inversions(array[:split_point])
    y = count_inversions(array[split_point:])
    z = _count_split_inversions(array)

    return x+y+z
