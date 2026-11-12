import random

p = 60238423281201603035618738734175500073376069852072170831139700677986577196703
g = 2
ciphertext = bytes.fromhex("a9aa2585e1782be652bdc35afcbfb1a32c79442ad38fa02d79120a28fcb4f0fc79e3bee2cb9a94ae28675514febda7db")
## Public data (can be seen by Franco): p,g, ciphertext

# --- Alice Turn ---
# Alice choses her private key (in real scenario randomly)
alice_private = 676767

# --- Calculate Alice public Key ---

# Formula: Shared_key = (g ** Private_Alice) mod p
# Since you are working with huge numbers; use pow(base,exp,mod)

alice_public = pow(g, alice_private, p)

# --- Bob calculates his public key ---

bob_public = 44692970352474333943508099310438158509252745661204648111734232007330507026525


# --- Calculate Shared Secret ---

# Formula: Shared_key = (Public_bob ** Private_Alice) mod p
# Since you are working with huge numbers; use pow(base,exp,mod)

shared_secret = pow(bob_public, alice_private, p)


print(f"Chiave segreta condivisa: {shared_secret}")

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad, unpad

# -- ENCRYPTION ---
# This is how the flag was encrypted
#print(AES.new(SHA256.new(long_to_bytes(shared_secret)).digest(),AES.MODE_ECB).encrypt(pad(flag,16)).hex())

# -- DECRYPTION ---
# Gift from Santa
print(unpad(AES.new(SHA256.new(long_to_bytes(shared_secret)).digest(),AES.MODE_ECB).decrypt(ciphertext),16).decode())
