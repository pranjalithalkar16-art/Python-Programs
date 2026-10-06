def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primes_in_range(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    return primes


# Test cases using assert

assert is_prime(2) == True
assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert primes_in_range(10, 20) == [11, 13, 17, 19]

print("All test cases passed!")