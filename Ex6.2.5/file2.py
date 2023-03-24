from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    """
    A class used to represent a birthday card.
    Inherits from GreetingCard.
    :param sender_age: The age of the sender. Default is 0.
    :type sender_age: int
    :ivar _sender_age: The sender's age of the individual card
    """
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch", sender_age: int = 0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self) -> None:
        """
        Prints the card's participants and some more values
        """
        super().greeting_msg()
        print(f"Happy birthday! I am {self._sender_age} years old.")
