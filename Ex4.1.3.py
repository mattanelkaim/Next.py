from time import time


def first_prime_over(n: int) -> int:
    """
    Calculates the next prime after n
    :param n: Start checking primes starting with its next integer
    :type n: int
    :return: The next prime after n
    :rtype: int
    """
    primes = (x for x in range(n + 1, n << 1) if is_prime(x))  # Primes from n + 1 to 2 * n
    return next(primes)


# Just playing with prime numbers
def is_prime(n: int) -> bool:
    # Corner case or 2 / 3
    if n <= 3:
        return n > 1
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check from 5 to sqrt(n), skipping multiples of 2 and 3
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def main():
    start = time()
    print(first_prime_over(513_532_512))
    end = time()
    print(f"Took {end - start} seconds.")


if __name__ == '__main__':
    main()
