primes = []
for i in range(1, 101):
    for t in range(2, i):
        if (i % t == 0):
            break
    else:
      primes.append(i)
print("primes =", primes)
