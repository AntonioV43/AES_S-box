import numpy as np

def text_to_state(text):
    bytes_ = [ord(c) for c in text.ljust(16, '\x00')]
    return np.array(bytes_).reshape(4,4).T

def state_to_text(state):
    return ''.join(chr(b) for b in state.T.flatten())

def xor_states(a, b):
    return a ^ b
