def number_check(x, y):
    if is_prime(x) and is_prime(y) and abs(y - x) == 6:
        return 'True'
    return 'False'

def is_prime2(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    print number_check(100000000000133, 100000000000139)
