from module_1.sbox44 import SBOX44

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = SBOX44[state[i][j]]
    return state
