import numpy as np

def sac(sbox):
    total = 0
    count = 0
    for x in range(256):
        for i in range(8):
            x_flip = x ^ (1 << i)
            diff = sbox[x] ^ sbox[x_flip]
            total += bin(diff).count("1")
            count += 8
    return total / count
