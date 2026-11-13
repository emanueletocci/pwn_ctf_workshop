from pwn import *
HOST = "130.192.5.212"
PORT = 8769

r = remote(HOST,PORT)

r.recvuntil(b"Go!")

for _ in range(1000):
    q = r.recvuntil(b"=").decode()
    q = q.split()

    a,b = int(q[2]),int(q[4])
    op = q[3]
    print(a, op, b)
    if (op == "+"):
        result = a + b
    elif (op == "-"):
        result = a - b
    elif (op == "*" ):
        result = a * b
    elif (op == "/"):
        result = a // b
    else:
        result = a**b

    r.sendline(str(result).encode())

r.interactive()

# new challenges: 8769, 8770