from pwn import *
HOST = "130.192.5.212"
PORT = 8767

r = remote(HOST,PORT)

r.recvuntil(b"Go!")

for _ in range(100):
    q = r.recvuntil(b"=").decode()
    q = q.split()

    a,b = int(q[2]),int(q[4])
    print(a,b, a+b)

    r.sendline(str(a+b))

r.interactive()

# new challenges: 8769, 8770
