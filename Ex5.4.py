MAX_ID = 999999999


def check_id_valid(id_number: int) -> bool:
    """
    Check ID num validity according to Israel's ID num validity check algorithm.
    :param id_number: The ID number to check
    :type id_number: int
    :return: Is the ID number is valid?
    :rtype: bool
    """
    digits = map(int, str(id_number))
    after_mul = (val * (i % 2 + 1) for i, val in enumerate(digits))
    after_add = map(lambda x: x % 10 + x // 10, after_mul)  # Add the digits in 2-digit num
    return sum(after_add) % 10 == 0


class IDIterator:
    """
    An iterator to go through possible valid ID numbers.
    :param start_id: The ID number to start counting from. Default is 100000000.
    :type start_id: int
    :ivar _id = The current ID number of the iterator
    """
    def __init__(self, start_id: int = 100000000):
        self._id = start_id

    def __iter__(self) -> "IDIterator":
        return self

    def __next__(self) -> int:
        """
        Finds the next valid ID in the iterator.
        :return: Next valid ID
        :rtype: int
        :raises: StopIteration: If there are no more elements in the iterator
        """
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1

        if self._id > MAX_ID:
            raise StopIteration

        return self._id


def id_generator(current_id: int = 123456780):
    """
    Generator function that calculates next valid ID number
    :param current_id: The ID number to start calculating from. Default is 123456780.
    :type current_id: int
    :return: The next valid ID number, -1 if crossed max
    :rtype: Generator[int]
    """
    while True:
        if current_id <= MAX_ID:
            current_id += 1
            while not check_id_valid(current_id):
                current_id += 1
            yield current_id
        else:
            yield -1


def main():
    user_id = int(input("Enter your ID number: "))
    machine = input("Generator or Iterator? (gen/it)? ")

    if machine not in ["gen", "it"]:
        raise ValueError("Invalid machine name!")

    if machine == "gen":
        my_id_generator = id_generator(user_id)
        # Print next 10 valid ID numbers
        for _ in range(10):
            try:
                print(next(my_id_generator))
            except StopIteration:
                print("Reached maximum of valid ID numbers!")
                break
    else:  # Must be "it"
        my_id_iterator = IDIterator(user_id)
        # Print next 10 valid ID numbers
        for _ in range(10):
            print(next(my_id_iterator))


if __name__ == '__main__':
    main()
