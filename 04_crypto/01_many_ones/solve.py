#!/usr/bin/env python3
import json, secrets, hashlib
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad, unpad

with open("output.txt", "r") as f:
    data = json.load(f)

p = data["p"]
g = data["g"]
A = data["A"]
B = data["B"]

iv = bytes.fromhex(data["iv"])
ct = bytes.fromhex(data["ct"])

N = 256

# The Alice private key (a) is a 256-bit number with only 2 bits set to 0. 
# We can brute-force the possible values of a by flipping 2 bits in the range [0, 255] and 
# checking if the resulting shared secret matches the one used to encrypt the flag.
a = (1 << N) - 1

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a_candidate = a ^ (1 << i) ^ (1 << j)
        A_candidate = pow(g, a_candidate, p)

        if A_candidate != A:
            continue

        shared_key = pow(B, a_candidate, p)
        # Convert the shared secret number to a string and hash it with SHA-256 to get a 32-byte AES key
        key = hashlib.sha256(str(shared_key).encode()).digest()

        decrypted = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), 16).decode()
        print(decrypted)
        break




