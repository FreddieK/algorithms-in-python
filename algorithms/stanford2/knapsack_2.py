import numpy as np
import pyximport; pyximport.install()
import algorithms.stanford2.knapsack_loop as knapsack_loop


def knapsack(n=4, W=6, items=[[3, 4], [2, 3], [4, 2], [4, 3]]):
    A = np.zeros(shape=(n+1, W+1))
    A = knapsack_loop.calculate_optimal_solution(A, W, items, n)
    return A
