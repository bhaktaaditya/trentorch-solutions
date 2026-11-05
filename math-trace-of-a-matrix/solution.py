import numpy as np


def trace(A):
    return np.trace(A)


def trace_of_product(A, B):
    return (A * B.T).sum()
