class BigThing:
    """
    A class used to check instances of a given var.
    :param var: The var to check its superclass
    :type var: int or list or dict or str
    :ivar _var: The var of the current instance
    """
    def __init__(self, var: "int or list or dict or str"):
        self._var = var

    def size(self) -> int:
        """
        Checks the superclass of the given var,
        Calculates the length of the var if it's not an int.
        :return: var if int, else length of var
        :rtype: int
        """
        if isinstance(self._var, int):
            return self._var
        elif isinstance(self._var, (list, dict, str)):
            return len(self._var)


class BigCat(BigThing):
    """
    A class used to represent a cat, preferably a big one.
    Inherits from BigThing.
    :param weight: The weight of the cat
    :type weight: int
    :ivar _weight: The weight of the current cat
    """
    def __init__(self, var: "int or list or dict or str", weight: int):
        super().__init__(var)
        self._weight = weight

    def size(self) -> str:
        """
        Judges the weight of you poor cat
        :return: The medical condition of your cat
        :rtype: str
        """
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:  # Elif
            return "Fat"
        else:
            return "OK"  # Else


def main():
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
