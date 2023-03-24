def is_prime(number: int) -> bool:
    """
    Checks whether a number is a prime or not
    :param number: The number to check
    :type number: int
    :return: Is number a prime?
    :rtype: bool
    """
    # Checks if number can divide by any of its prior numbers
    # YES, IT IS SUB-OPTIMAL :(
    return 0 not in list(map(lambda x: number % x, range(2, number)))


def main():
    print(is_prime(321932190218321798321))
    print(is_prime(43))


if __name__ == '__main__':
    main()
