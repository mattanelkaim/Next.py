class UnderAge(Exception):
    """
    A customized exception to reject underage kids.
    :param age: The age of the underage
    :type age: int
    :ivar _age: The age of the current underage
    """
    def __init__(self, age: int):
        self._age = age

    def __str__(self) -> str:
        return f"You are a katin, only {self._age} years old! Come back in {18 - self._age} years."


def send_invitation(name: str, age: int) -> None:
    """
    Invites adults, otherwise raises an exception
    :param name: The name of the invited person
    :type name: str
    :param age: The age of the invited person
    :type age: int
    :return: None
    :raises: UnderAge: If age is below 18
    """
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print(f"You should send an invite to {name}")


def main():
    send_invitation("Mattan", 16)


if __name__ == '__main__':
    main()
