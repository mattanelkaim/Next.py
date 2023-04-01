from itertools import chain
from typing import Generator


def parse_ranges(ranges_string: str) -> Generator[int, int, None]:
    """
    Creates a generator with all nums specified in the ranges.
    Input format: a-b,c-d,e-f
    :param ranges_string: The ranges of the numbers
    :type ranges_string: str
    :return: A generator with all nums in the ranges.
    :rtype: Generator[int, int, None]
    """
    ranges = (map(int, x.split("-")) for x in ranges_string.split(","))
    # Join all generators to 1 big iterable
    nums_gen = (num for start, end in ranges for num in range(start, end + 1))
    return nums_gen


def main():
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == '__main__':
    main()
