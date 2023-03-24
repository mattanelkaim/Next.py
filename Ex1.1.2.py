def double_letter(my_str: str) -> str:
    """
    Returns the given string where all letters are doubled
    :param my_str: The string whose letters need to be doubled
    :type my_str: str
    :return: The string with doubled letters
    :rtype: str
    """
    # Double letters using lambda & map, then join list to a string
    return "".join(list(map(lambda x: 2 * x, my_str)))


def main():
    print(double_letter("we are the champions!"))


if __name__ == '__main__':
    main()
