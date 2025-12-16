import numpy as np

def byte_to_bits(x):
    return [(x >> i) & 1 for i in range(8)]

def sbox_to_boolean(sbox):
    boolean_funcs = [[] for _ in range(8)]
    for x in range(256):
        bits = byte_to_bits(sbox[x])
        for i in range(8):
            boolean_funcs[i].append(bits[i])
    return np.array(boolean_funcs)
