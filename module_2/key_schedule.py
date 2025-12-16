from module_1.sbox44 import SBOX44
import numpy as np

RCON = [
    0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36
]

def sub_word(word):
    return [SBOX44[b] for b in word]

def rot_word(word):
    return word[1:] + word[:1]

def expand_key(key):
    key_bytes = [ord(c) for c in key.ljust(16, '\x00')]
    w = [key_bytes[i:i+4] for i in range(0,16,4)]

    for i in range(4, 44):
        temp = w[i-1].copy()
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= RCON[i//4 - 1]
        w.append([w[i-4][j] ^ temp[j] for j in range(4)])

    round_keys = []
    for i in range(0, 44, 4):
        rk = np.array(w[i:i+4]).T
        round_keys.append(rk)

    return round_keys
