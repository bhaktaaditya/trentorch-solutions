import numpy as np


def matmul_from_scratch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """result[i, j] = sum_p(a[i, p] * b[p, j])"""
    m = np.zeros((a.shape[0], b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            m[i,j] = sum(a[i]*b[:, j])
    return m
