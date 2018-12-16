import numpy as np
import pyximport; pyximport.install(setup_args={'include_dirs': np.get_include()})
import algorithms.stanford2.knapsack_loop2 as knapsack_loop


def knapsack(n, W, items):
    A = knapsack_loop.calculate_optimal_solution(W, items, n)
    return A
