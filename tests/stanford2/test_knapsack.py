from algorithms.stanford2.knapsack import *
import pytest

# Do first part in python
# Test cythonizing it for second part


def test_reads_file_correctly():
    items, sack_size, num_items = read_file()

    assert num_items == 100
    assert len(items) == num_items
    assert sack_size == 10000


def test_can_recursively_solve_smaller_problem():
    A = knapsack(n=4, W=6, items=[[3, 4], [2, 3], [4, 2], [4, 3]])

    assert A.max() == 8
    assert A.shape == (5, 7)


@pytest.mark.skip(reason="No actual test")
def test_stanford_data():
    items, sack_size, num_items = read_file()
    A = knapsack(num_items, sack_size, items)
    print(f'Max value is {A.max()}')


def test_stanford_part2():
    items, sack_size, num_items = read_file('knapsack_big.txt')
    A = knapsack(num_items, sack_size, items)
    print(f'Max value is {A.max()}')
    breakpoint()