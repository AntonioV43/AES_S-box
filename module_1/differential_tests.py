def ddt(sbox):
    table = [[0]*256 for _ in range(256)]
    for dx in range(256):
        for x in range(256):
            dy = sbox[x] ^ sbox[x ^ dx]
            table[dx][dy] += 1
    return table

def dap(sbox):
    table = ddt(sbox)
    return max(max(row) for row in table[1:]) / 256

def du(sbox):
    table = ddt(sbox)
    return max(max(row) for row in table[1:])
