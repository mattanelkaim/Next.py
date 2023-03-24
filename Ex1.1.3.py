def four_dividers(number: int) -> list[int]:
    """
    Returns a list of all four dividers from 1 to number itself (included)
    :param number: The max of the range (should be included in range)
    :type number: int
    :return: All four dividers between 1 and number (included)
    :rtype: list[int]
    """
    # Get a range of all numbers between 4 (1,2,3 % 4 != 0) and number + 1 (to include),
    # Then use lambda & filter to get all 4 dividers, then convert to a list
    return list(filter(lambda x: x % 4 == 0, range(4, number + 1)))


def main():
    print(four_dividers(100))


if __name__ == '__main__':
    main()
