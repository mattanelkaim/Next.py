class GreetingCard:
    """
    A class used to represent the
    properties of a greeting card.
    :param recipient: The name of the recipient. Default is "Dana Ev".
    :type recipient: str
    :param sender: The name of the sender. Default is "Eyal Ch".
    :type sender: str
    :ivar _recipient: The name of the individual card's recipient
    :ivar _sender: The name of the individual card's sender
    """
    def __init__(self, recipient: str = "Dana Ev", sender: str = "Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self) -> None:
        """
        Prints the card's participants
        """
        print(f"recipient: {self._recipient}, sender: {self._sender}")
