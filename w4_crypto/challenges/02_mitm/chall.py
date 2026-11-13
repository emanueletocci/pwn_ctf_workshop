import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad

# Secret flag
FLAG = b"ptm{?????????????????}"

# Public Diffie-Hellman Parameters

p = 60238423281201603035618738734175500073376069852072170831139700677986577196703
g = 2

def server_simulation():
    
    print("[DH NETWORK SERVICE SIMULATION] Cryptographic connection between Alice and Bob ... [DH NETWORK SERVICE SIMULATION]")

    # 1. prvate key generation
    alice_private = random.randint(100000000, p-2)
    bob_private =   random.randint(100000000, p-2)

    # 2. public key generation
    alice_public = pow(g, alice_private, p) # pow(base,exp,mod)
    bob_public   = pow(g, bob_private, p)   # pow(base,exp,mod)

    print(f"Alice generates her public key: {alice_public}")
    print(f"Bob generates his public key: {bob_public}")

    # --- FRANCO INTERCEPTION ---
    
    print("😈 [FRANCO IN ACTION] You are between Alice and Bob [FRANCO IN ACTION] 😈")
    print("Bob wants to send to Alice hs public key, but maybe you have other plans")
    
    while True:
        try:
            forged_to_alice = int(input("Insert the key to send to Alice: "))
            if forged_to_alice != 0: #security
                break
        except ValueError:
            print("It must be an integer")

    print(f"Franco send {forged_to_alice} to Alice!")


    shared_secret_alice = pow(forged_to_alice, alice_private, p)

    # print(shared_secret_alice) secret

    aes_key = SHA256.new(long_to_bytes(shared_secret_alice)).digest()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(FLAG, 16)) 
    

    print(f"Alice sends the encrypted flag")
    print(f"ciphertext = {ciphertext.hex()}")

if __name__ == "__main__":
    server_simulation()