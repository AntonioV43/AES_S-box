def algebraic_degree(boolean_func):
    # sederhana: brute-force ANF (cukup untuk tugas)
    degree = 0
    n = len(boolean_func).bit_length() - 1
    for i in range(1, 2**n):
        if boolean_func[i]:
            degree = max(degree, bin(i).count("1"))
    return degree
