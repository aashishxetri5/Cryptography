import random as r

def getPrime():
    isPrime = True
    while True:
        num = r.randint(2, 15)

        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
            else:
                isPrime = True

        if isPrime:
            return num
        else:
            continue


def getPrivateKey(publicKey, phi):
    for i in range(1, phi):
        if (publicKey * i) % phi == 1:
            return i


def encryption(plaintext, n, publicKey):
    return (plaintext**publicKey) % n

def decryption(encrText, n, Kprivate):
    return (encrText**Kprivate) % n

p = getPrime()
q = getPrime()
print(p, q)

n = p * q
print(n)

phi = (p - 1) * (q - 1)
publicKey = r.randint(1, phi - 1)
print(phi, publicKey)

while True:
    if phi % publicKey == 0:
        publicKey = r.randint(1, phi - 1)
    else:
        break

Kprivate = getPrivateKey(publicKey, phi)
print(Kprivate)

# Encryption
plainText = int(input(f"Enter a number below {p} and {q}: "))
# plainText = ord(plainText)

y = encryption(plainText, n, publicKey)
x = decryption(y, n, Kprivate)

print("Encrypted text: ", plainText)
print("Encrypted text: ", y)
print("Decrypted text: ", x)
