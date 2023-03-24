class Animal:
    """
    A class used to represent an animal.
    :cvar ZOO_NAME: The name of the zoo.
    :param name: The name of the animal.
    :type name: str
    :param hunger: The hunger level of the animal. Default is 0.
    :type hunger: int
    :ivar _name: The name of the animal.
    :ivar _hunger: The current hunger level of the animal.
    """
    ZOO_NAME = "Hayaton"

    def __init__(self, name: str, hunger: int = 0):
        self._name = name
        self._hunger = hunger

    @property
    def name(self) -> str:
        return self._name

    def is_hungry(self) -> bool:
        """
        Checks whether the animal is hungry or not.
        :return: True if hungry, otherwise False
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self) -> None:
        """
        Feeds the animal if it's hungry, reducing its hunger by 1.
        """
        if self.is_hungry():
            self._hunger -= 1

    def talk(self) -> None:
        """
        Makes a sound for each animal.
        Should be implemented in the subclasses
        """
        pass


class Dog(Animal):
    """
    A class used to represent a dog.
    Inherits from Animal.
    """
    def talk(self) -> None:
        print("woof woof")

    def fetch_stick(self) -> None:
        print("There you go, sir!")


class Cat(Animal):
    """
    A class used to represent a cat.
    Inherits from Animal.
    """
    def talk(self) -> None:
        print("meow")

    def chase_laser(self) -> None:
        print("Meeeeow")


class Skunk(Animal):
    """
    A class used to represent a dog.
    Inherits from Animal.
    :param stink_count: The stink level of the skunk. Default is 6.
    :type stink_count: int
    :ivar _stink_count: The stink level of the current skunk
    """
    def __init__(self, name: str, hunger: int = 0, stink_count: int = 6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self) -> None:
        print("tsssss")

    def stink(self) -> None:
        print("Dear lord!")


class Unicorn(Animal):
    """
    A class used to represent a unicorn.
    Inherits from Animal.
    """
    def talk(self) -> None:
        print("Good day, darling")

    def sing(self) -> None:
        print("I’m not your toy...")


class Dragon(Animal):
    """
    A class used to represent a dragon.
    Inherits from Animal.
    :param color: The color of the dragon. Default is "green".
    :type color: str
    :ivar _color: The color of the current dragon
    """
    def __init__(self, name: str, hunger: int = 0, color: str = "green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self) -> None:
        print("Raaaawr")

    def breath_fire(self) -> None:
        print("$@#$#@$")


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3),
               Skunk("Stinky", 0), Unicorn("Keith", 7),
               Dragon("Lizzy", 1450)]

    # Add new animals
    zoo_lst.extend([Dog("Doggo", 80), Cat("Kitty", 80),
                    Skunk("Stinky Jr.", 80), Unicorn("Clair", 80),
                    Dragon("McFly", 80)])

    # Feed all animals, then talk
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.name)
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.ZOO_NAME)


if __name__ == '__main__':
    main()
