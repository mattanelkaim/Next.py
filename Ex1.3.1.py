def intersection(list_1: list, list_2: list) -> list:
    """
    Finds the elements that are in both lists, without duplicates
    :param list_1: The first list to check
    :type list_1: list
    :param list_2: The second list to check
    :type list_2: list
    :return: The elements that intersect list_1 and list_2
    :rtype: list
    """
    # First find intersections, then cast to set to lose duplicates and back to list
    return list({x for x in list_1 if x in list_2})


def main():
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


if __name__ == '__main__':
    main()
