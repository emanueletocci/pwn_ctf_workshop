import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad


FLAG = b"ptm{??????????}"

p = 60238423281201603035618738734175500073376069852072170831139700677986577196703
g = 2

def server_simulation():
    
    print("[DH NETWORK SERVICE SIMULATION] Cryptographic connection between Alice and Bob ... [DH NETWORK SERVICE SIMULATION]")
    
    alice_private = random.randint(100000000, p-2)
    bob_private =   random.randint(100000000, p-2)

    alice_public = pow(g, alice_private, p)
    bob_public =   pow(g, bob_private, p)

    print(f"Alice generates her public key: {alice_public}")
    print(f"Bob generates his public key: {bob_public}")
    

    print("😈 [FRANCO IN ACTION] You are between Alice and Bob [FRANCO IN ACTION] 😈")
    print("Bob wants to send to Alice hs public key, but maybe you have other plans")
    
    
    while True:
        try:
            fake_key = int(input("Insert the key to send to Alice: "))
            if fake_key in [1,0,-1,p-1]:
                print("Too Easy") 
                continue
            break
        except ValueError:
            print("It must be an integer")


    shared_secret = pow(fake_key, bob_private, p)

    print(f"Franco send {fake_key} to Alice!")


    # print(shared_secret_alice) secret

    aes_key = SHA256.new(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(FLAG, 16)) 
    

    print(f"Alice sends the encrypted flag")
    print(f"ciphertext = {ciphertext.hex()}")

if __name__ == "__main__":
    server_simulation()