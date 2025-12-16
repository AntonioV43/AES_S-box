from module_2.encrypt import encrypt

pt = "HELLO WORLD"
key = "SECRETKEY123456"

ct = encrypt(pt, key)
print("Ciphertext:", ct)
