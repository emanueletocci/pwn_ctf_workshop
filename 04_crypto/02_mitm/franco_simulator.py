from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import unpad
import pwn

print("Attack Man-in-the-Middle\n")

# Public data stolen from the web by Franco
p = 60238423281201603035618738734175500073376069852072170831139700677986577196703
g = 2

io = pwn.remote("ip","port")
io.recvline()

alice_pub = int(io.recvline().strip().decode().split(" ")[-1])
bob_pub = int(io.recvline().strip().decode().split(" ")[-1])


fake_public_key = ...

print(f"Franco sends the new public key: {fake_public_key}")


io.sendlineafter(b"Insert the key to send to Alice: ",str(fake_public_key).encode())

shared_secret_malicious = ...

io.recvline()
io.recvline()
ct_hex = io.recvline().strip().decode().split(" ")[-1].strip()

ciphertext = bytes.fromhex(ct_hex)
print(f"Secret key forged to: {shared_secret_malicious}")


aes_key = SHA256.new(long_to_bytes(shared_secret_malicious)).digest()
cipher = AES.new(aes_key, AES.MODE_ECB)

flag = unpad(cipher.decrypt(ciphertext), 16).decode()
print(f"Flag succesfully obtained: {flag}")
