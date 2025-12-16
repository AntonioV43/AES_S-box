from module_2.aes_core import text_to_state, state_to_text, xor_states
from module_2.subbytes import sub_bytes
from module_2.shiftrows import shift_rows
from module_2.mixcolumns import mix_columns
from module_2.key_schedule import expand_key

def encrypt(plaintext, key):
    state = text_to_state(plaintext)
    round_keys = expand_key(key)

    state = xor_states(state, round_keys[0])

    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = xor_states(state, round_keys[r])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = xor_states(state, round_keys[10])

    return state_to_text(state)
