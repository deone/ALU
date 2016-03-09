import math

def number_check(x, y):
    if is_prime(x) and is_prime(y) and abs(y - x) == 6:
        return True
    return False

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
