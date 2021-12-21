import math

def isPrime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

def main():
    primes = []
    for c in range(2, 3000):       
        if isPrime(c):
            primes.append(c)

    for c in primes:
        for d in primes:
            if c == d: continue
            g = math.sqrt(pow(c,2)+pow(d,2))
            if isPrime(g):
                print(c,d,g)
main()