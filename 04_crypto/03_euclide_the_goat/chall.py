#!/usr/bin/env python3

import hashlib, secrets, json
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = b"ptm{???????????????}"

p = getPrime(1024)
g = secrets.randbelow(p - 2) + 2


a = secrets.randbelow(p - 2) + 2
b = secrets.randbelow(p - 2) + 2
A = (a * g) % p
B = (b * g) % p

shared = (a * B) % p       
key = hashlib.sha256(str(shared).encode()).digest()
iv = secrets.token_bytes(16)
ct = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(FLAG, 16))

json.dump(dict(p=p, g=g, A=A, B=B, iv=iv.hex(), ct=ct.hex()),
          open("output.txt", "w"), indent=1)
print("output.txt written")
