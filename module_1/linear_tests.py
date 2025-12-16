def lap(sbox):
    max_bias = 0
    for a in range(1,256):
        for b in range(1,256):
            count = 0
            for x in range(256):
                if bin(a & x).count("1") % 2 == bin(b & sbox[x]).count("1") % 2:
                    count += 1
            bias = abs(count - 128)
            max_bias = max(max_bias, bias)
    return max_bias / 256
