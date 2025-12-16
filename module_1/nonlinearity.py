import numpy as np
from scipy.linalg import hadamard

def nonlinearity(boolean_func):
    n = len(boolean_func).bit_length() - 1
    H = hadamard(2**n)
    f = np.array(boolean_func)
    spectrum = H @ (1 - 2*f)
    return (2**(n-1)) - (np.max(np.abs(spectrum)) // 2)
