import gmpy
from pwn import *

def npqe(n, p, q, e, enc) :
    phi = (p-1) * (q-1)
    d = gmpy.invert(e, phi)
    d = long(d)
    m = pow(enc, d, n)
    print hex(m)
    result = hex(m)[2:].decode('hex').decode('base64')
    result = hex(int(result))[2:].decode('hex')
    print result
    return result

if __name__ == '__main__':
    s = remote('203.251.182.94', 4000)
    enc = int(s.recvline().split()[2])
    e = int(s.recvline().split()[2])
    p = int(s.recvline().split()[2])
    q = int(s.recvline().split()[2])
    result = npqe(p*q, p, q, e, enc)
    s.send(result)

    s.interactive()
