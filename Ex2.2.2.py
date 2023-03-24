class Capybara:
    """
    A class used to represent the holy Capybara.
    :ivar name: The name of the current Capy
    :ivar _age: The age of the current Capy
    """
    def __init__(self):
        self.name = "Ok I Pull Up"
        self._age = 5

    def birthday(self) -> None:
        self._age += 1

    @property
    def age(self) -> int:
        return self._age


def main():
    first_capy = Capybara()
    second_capy = Capybara()
    first_capy.birthday()
    print(f"First capy age: {first_capy.age}")
    print(f"Second capy age: {second_capy.age}")


if __name__ == '__main__':
    main()
