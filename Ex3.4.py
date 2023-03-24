class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg: str):
        self._arg = arg

    def __str__(self) -> str:
        return "The username contains an illegal character \"%s\" at index %d" % self.show_illegal_char()

    def show_illegal_char(self) -> tuple[str, int]:
        """
        Finds the illegal char (not alphanumeric nor "_") in the username and its index.
        :return: The illegal character in the username and its index
        :rtype: tuple[str, int]
        """
        for char in self._arg:
            if not (char.isalnum() or char == "_"):
                return char, self._arg.index(char)


class UsernameTooShort(Exception):
    def __str__(self) -> str:
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self) -> str:
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self) -> str:
        return "The password is missing a character"


class PasswordMissingUpper(PasswordMissingCharacter):
    def __str__(self) -> str:
        return super().__str__() + " (Uppercase)"


class PasswordMissingLower(PasswordMissingCharacter):
    def __str__(self) -> str:
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self) -> str:
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self) -> str:
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self) -> str:
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self) -> str:
        return "The password is too long"


def check_input(username: str, password: str) -> None:
    """
    Checks whether the username & password are valid or not
    :param username: The username to check
    :type username: str
    :param password: The password to check
    :type password: str
    :return: None
    :raises UsernameContainsIllegalCharacter: If username contains illegal chars
    :raises UsernameTooShort: If username is too short
    :raises UsernameTooLong: If username is too long
    :raises PasswordTooShort: If password is too short
    :raises PasswordTooLong: If password is too long
    :raises PasswordMissingUpper: If password is missing an uppercase char
    :raises PasswordMissingLower: If password is missing a lowercase char
    :raises PasswordMissingDigit: If password is missing a digit
    :raises PasswordMissingSpecial: If password is missing a special char
    """
    username_length, password_length = len(username), len(password)
    special_chars = set('!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~')  # More efficient

    # Check characters in username
    for char in username:
        if not (char.isalnum() or char == "_"):
            raise UsernameContainsIllegalCharacter(username)

    if username_length < 3:
        raise UsernameTooShort()
    if username_length > 16:
        raise UsernameTooLong()

    if password_length < 8:
        raise PasswordTooShort()
    if password_length > 40:
        raise PasswordTooLong()

    # Check characters in password
    has_uppercase = has_lowercase = has_digit = has_special = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if not has_uppercase:
        raise PasswordMissingUpper()
    if not has_lowercase:
        raise PasswordMissingLower()
    if not has_digit:
        raise PasswordMissingDigit()
    if not has_special:
        raise PasswordMissingSpecial()

    print("OK")  # Valid username & password


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            check_input(username, password)
        except UsernameContainsIllegalCharacter as e:
            print(e)
            print()
            continue
        except UsernameTooShort as e:
            print(e)
            print()
            continue
        except UsernameTooLong as e:
            print(e)
            print()
            continue
        except PasswordMissingUpper as e:
            print(e)
            print()
            continue
        except PasswordMissingLower as e:
            print(e)
            print()
            continue
        except PasswordMissingDigit as e:
            print(e)
            print()
            continue
        except PasswordMissingSpecial as e:
            print(e)
            print()
            continue
        except PasswordTooShort as e:
            print(e)
            print()
            continue
        except PasswordTooLong as e:
            print(e)
            print()
            continue
        break  # Username & password are valid!


if __name__ == '__main__':
    main()
