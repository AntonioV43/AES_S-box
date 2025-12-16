import numpy as np
from .nonlinearity import nonlinearity

def bic_nl(boolean_funcs):
    values = []
    for i in range(8):
        for j in range(i+1, 8):
            xor_func = boolean_funcs[i] ^ boolean_funcs[j]
            values.append(nonlinearity(xor_func))
    return min(values)
