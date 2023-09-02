def kFinder(n):
    k = []
    i = 2

    for i in range(2, 10):
        if((n % 2**i) == 0):
            k.append(i)
            
    if(n % 2 == 0):
        k.append(1)
    return k

def getM(n, k):
    return (n/2**k)

def miller_rabin(n, a, k):
    m = getM(n-1, k)
    T = (a**m % n)
    print(T, m)

    if (T == 1 or T == n-1):
        return "Prime"
    
    for i in range(k-1):
        T = T**2 % (n)
        if T == 1: return "Composite"
        if T == n-1: return "Prime"
    
    return "Composite"

number = int(input("Enter a number: "))
k = kFinder(number-1)
a = 2

if len(k) == 0:
    k.append(0)

for i in k:
    print(f"\nFor k = {i}")
    print(miller_rabin(number, a, i))
