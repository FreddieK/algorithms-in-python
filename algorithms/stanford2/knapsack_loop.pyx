# cython: language_level=3
# cython: infer_types=True


def calculate_optimal_solution(A, W, items, n):
    for i in range(1, n + 1):
        if i % 50 == 0:
            print(i, n)
        for x in range(0, W + 1):
            dont_take_item = A[i - 1][x]
            if x - items[i - 1][1] >= 0:
                take_item = A[i - 1][x - items[i - 1][1]] + items[i - 1][0]
            else:
                take_item = 0  # Fallback if can't fit item in sack

            A[i][x] = max([dont_take_item, take_item])
    return A