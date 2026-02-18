import numpy as np
numbers = np.arange(1, 101)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = np.array([num for num in numbers if is_prime(num)])

print("Prime Numbers from 1 to 100:")
print(primes)