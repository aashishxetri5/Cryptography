def primeFactors(n):
    realn = n
    count = 0
    factors = {}

    while(n % 2 == 0):
        count += 1
        n //= 2 #Updating n by quotient when divided by zero.
    if(count != 0):
        factors[2] = count
    
    for i in range(3, int(realn**0.5)+1, 2):
        count=0
        while (n % i == 0):
            count += 1
            n //= i
        if(count != 0):
            factors[i] = count
    if n > 1:
        factors[n] = 1
    return factors


num = int(input("Enter a number: "))
print(primeFactors(num))
