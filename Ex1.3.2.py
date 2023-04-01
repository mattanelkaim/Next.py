def is_prime(number: int) -> bool:
    """
    Checks whether a number is a prime or not
    :param number: The number to check
    :type number: int
    :return: Is number a prime?
    :rtype: bool
    """
    # Checks if number can divide by any of its prior numbers
    # Also, checking up to sqrt of number for efficiency
    return 0 not in map(lambda x: number % x, range(2, int(number ** 0.5)))


def main():
    print(is_prime(321_932_190_218_321_798_321))
    print(is_prime(43))


if __name__ == '__main__':
    main()
