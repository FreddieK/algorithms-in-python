import numpy as np


def read_file(filename='knapsack1.txt'):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()

    sack_size, num_items = [int(value) for value in content[0].strip().split()]
    items = [[int(value) for value in line.strip().split()] for line in
             content[1:]]

    return items, sack_size, num_items


def knapsack(n=4, W=6, items=[[3, 4], [2, 3], [4, 2], [4, 3]]):
    """

    :return:
    """
    A = np.zeros(shape=(n+1, W+1))
    for i in range(1, n+1):
        if i % 100 == 0:
            print(i, n)

        for x in range(0, W+1):
            dont_take_item = A[i-1][x]
            if x - items[i-1][1] >= 0:
                take_item = A[i-1][x-items[i-1][1]] + items[i-1][0]
            else:
                take_item = 0  # Fallback if can't fit item in sack

            A[i][x] = max([dont_take_item, take_item])

    return A
