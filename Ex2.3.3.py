class Capybara:
    """
    A class used to represent the holy Capybara.
    :cvar count_animals: Counts the # of Capybaras created
    :param name: The name of the Capy. Default is "Ok I Pull Up".
    :type name: str
    :ivar _name: The name of the current Capy
    :ivar _age: The age of the current Capy
    """
    count_animals = 0

    def __init__(self, name: str = "Ok I Pull Up"):
        self._name = name
        self._age = 5
        Capybara.count_animals += 1

    def birthday(self) -> None:
        self._age += 1

    @property
    def age(self) -> int:
        return self._age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


def main():
    first_capy = Capybara("Capy Slay")
    second_capy = Capybara()
    print(f"First capy age: {first_capy.age}")
    print(f"Second capy age: {second_capy.age}")

    second_capy.name = "Gort"
    print(f"Second capy age: {second_capy.age}")

    print(f"Total capy: {Capybara.count_animals}")


if __name__ == '__main__':
    main()
