import math


def merge_sort(list_):
    # Basic implementation of merge sort algorithm, in preparation for
    # implementing the count-array-inversions algorithm

    length = len(list_)

    if length <= 1:
        return list_

    split_point = math.ceil(length / 2)
    x = merge_sort(list_[:split_point])
    y = merge_sort(list_[split_point:])

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


def count_inversions(list_):
    # Augmenting the merge sort with also counting the number of inversions
    # needed to sort array

    length = len(list_)

    if length <= 1:
        return list_, 0

    split_point = math.ceil(length / 2)
    x, x_inversions = count_inversions(list_[:split_point])
    y, y_inversions = count_inversions(list_[split_point:])

    inversions = x_inversions + y_inversions

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
                inversions += len(x) - i
        except IndexError:
            if len(x) <= i:
                sorted_list.append(y[j])
                j += 1
            elif len(y) <= j:
                sorted_list.append(x[i])
                i += 1

    return sorted_list, inversions
