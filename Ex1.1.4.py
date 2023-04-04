from functools import reduce


def sum_of_digits(number: int) -> int:
    """
    Calculates sum of digits of a given number
    :param number: Its digits need to be summed up
    :type number: int
    :return: The sum of number's digits
    :rtype: int
    """
    # Cast to str to get digits, then use lambda & reduce
    # To get the sum of the digits
    return reduce(lambda x, y: int(x) + int(y), str(number), 0)


def main():
    print(sum_of_digits(1234))


if __name__ == '__main__':
    main()
