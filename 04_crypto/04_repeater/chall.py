#!/usr/bin/env python3
import json, secrets, hashlib
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = b"ptm{?????????????????}"

p = getPrime(1024)
g = 2

block = secrets.randbelow((1 << 16) - 1) + 1
a = int.from_bytes(block.to_bytes(2, "big") * 16, "big")

b = secrets.randbits(256) | 1
A, B = pow(g, a, p), pow(g, b, p)

shared = pow(B, a, p)
key = hashlib.sha256(str(shared).encode()).digest()
iv = secrets.token_bytes(16)
ct = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(FLAG, 16))

json.dump(dict(p=p, g=g, A=A, B=B, iv=iv.hex(), ct=ct.hex()),
          open("output.txt", "w"), indent=1)
print("output.txt written")
