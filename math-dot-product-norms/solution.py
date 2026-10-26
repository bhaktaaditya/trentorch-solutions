import numpy as np


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    return sum(a*b)


def l1_norm(x: np.ndarray) -> float:
    return sum(abs(x))


def l2_norm(x: np.ndarray) -> float:
    return sum(x**2)**.5


def linf_norm(x: np.ndarray) -> float:
    return max(abs(x))
