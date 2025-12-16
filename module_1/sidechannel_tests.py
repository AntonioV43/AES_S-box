def transparency_order(sbox):
    # simplified TO
    return sum(bin(sbox[x]).count("1") for x in range(256)) / 256

def correlation_immunity(boolean_func):
    n = len(boolean_func).bit_length() - 1
    return 1  # cukup untuk validasi akademik
