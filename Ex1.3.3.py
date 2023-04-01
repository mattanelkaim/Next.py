def is_funny(string: str) -> bool:
    """
    Checks whether a string contains only 'a' and 'h'
    :param string: The string to check
    :type string: str
    :return: Whether contains only 'a' and 'h' or not
    :rtype: bool
    """
    # Use not any to stop as soon as meeting a true expression
    return not any(x for x in string if x not in {'a', 'h'})  # Could have used a list comprehension inefficiently


def main():
    print(is_funny("hahahahahaha"))


if __name__ == '__main__':
    main()
