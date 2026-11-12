#!/usr/bin/env python3
import json, secrets, hashlib
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# The secret message (the flag) we want to protect
FLAG = b'ptm{????????????}'

# Generate a large 1024-bit prime number 'p' and set the generator 'g' to 2
p = getPrime(1024)
g = 2

# Set the bit length to 256
N = 256
# Pick 2 random, unique positions between 0 and 255
zeros = secrets.SystemRandom().sample(range(N), 2)
# Create a 256-bit number where all bits are set to 1 (2^256 - 1) 
# The key here is WEEKLY generated, so we can assume that the private key is a 256-bit number with only 2 bits set to 0.
a = (1 << N) - 1
# Flip the bits at the 2 chosen positions from 1 to 0
for z in zeros:
    a ^= 1 << z

# Generate a random 256-bit odd number for Bob's private key
b = secrets.randbits(256) | 1           
# Compute Alice's and Bob's public keys using modular exponentiation
A, B = pow(g, a, p), pow(g, b, p)

# Compute the Diffie-Hellman shared secret using Bob's public key and Alice's private key
shared = pow(B, a, p)

# Convert the shared secret number to a string and hash it with SHA-256 to get a 32-byte AES key
key = hashlib.sha256(str(shared).encode()).digest()
# Generate a random 16-byte Initialization Vector (IV) for AES-CBC mode
iv = secrets.token_bytes(16)
# Pad the flag to a multiple of 16 bytes and encrypt it using AES-CBC
ct = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(FLAG, 16))

# Save all the public parameters and the encrypted flag into 'output.txt' in JSON format
json.dump(dict(p=p, g=g, A=A, B=B, iv=iv.hex(), ct=ct.hex()),
          open("output.txt", "w"), indent=1)
print("output.txt written")