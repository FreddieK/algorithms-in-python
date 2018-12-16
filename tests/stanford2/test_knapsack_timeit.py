import timeit
from algorithms.stanford2.knapsack import read_file, knapsack
import algorithms.stanford2.knapsack_2 as knapsack2
import algorithms.stanford2.knapsack_3 as knapsack3
import pytest


def test_reads_file_correctly():
    items, sack_size, num_items = read_file()

    assert num_items == 100
    assert len(items) == num_items
    assert sack_size == 10000


def test_pure_python():
    items, sack_size, num_items = read_file()
    time_raw = timeit.timeit(lambda: knapsack(num_items, sack_size,
                                              items), number=10)
    print(f'Pure Python runs in {time_raw}')


def test_cython_one():
    items, sack_size, num_items = read_file()
    time_raw = timeit.timeit(lambda: knapsack2.knapsack(num_items, sack_size,
                                                        items), number=10)
    print(f'Dynamic Cython runs in {time_raw}')


def test_cython_type_annotated():
    items, sack_size, num_items = read_file()
    time_raw = timeit.timeit(lambda: knapsack3.knapsack(num_items, sack_size,
                                                        items), number=10)
    print(f'Type Annotated Cython runs in {time_raw}')