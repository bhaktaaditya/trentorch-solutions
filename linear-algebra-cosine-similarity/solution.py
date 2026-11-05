import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    nA = np.dot(a,a)**.5
    nB = np.dot(b,b)**.5
    if nB!=0 and nA!=0:
        return (np.dot(a,b))/(nA*nB)
    else:
        return 0.0
