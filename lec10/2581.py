M = int(input())
N = int(input())

primes = []

for i in range(M, N + 1):
    if i < 2:  
        continue
    
    isprime = 1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isprime = 0
            break
            
    if isprime:
        primes.append(i)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
