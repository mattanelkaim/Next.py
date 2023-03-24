def is_funny(string: str) -> bool:
    """
    Checks whether a string contains only 'a' and 'h'
    :param string: The string to check
    :type string: str
    :return: Whether contains only 'a' and 'h' or not
    :rtype: bool
    """
    # Builds a list of all elements that are not 'a' or 'h', then it's funny if empty!
    return len([x for x in string if x != 'a' and x != 'h']) == 0


def main():
    print(is_funny("hahahahahaha"))


if __name__ == '__main__':
    main()
