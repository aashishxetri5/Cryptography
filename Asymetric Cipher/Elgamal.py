import random as r

def encr(e1, e2, plaintext):
    e = r.randint(1, p-1)
    c1 = (e1 ** e) % p
    c2 = (plaintext * (e2 ** e)) % p
    return c1, c2

def keyGen():
    p = 577
    e1 = 7
    d = r.randint(1, p-1)
    e2 = (e1**d) % p
    return e1, e2, d, p

def decr(d, p, c1, c2):
    for i in range(p):
        if((pow(c1, d)*i)%p == 1):
            c1_inv = i
    
    p = c2 * c1_inv % p
    return p


e1, e2, d, p = keyGen()
plaintext = int(input(f"Enter a no. under {p}: "))
c1, c2  = encr(e1, e2, plaintext)

print(f"Cipher: {c1}, {c2}")

p = decr(d, p, c1, c2)
print(f"Deciphered Plaintext: {p}")
