from file2 import GreetingCard, BirthdayCard


def main():
    my_greeting = GreetingCard("Niv", "Mattan")
    my_birthday = BirthdayCard("Nivos", "Mattos", 16)

    my_greeting.greeting_msg()
    print()  # New line
    my_birthday.greeting_msg()


if __name__ == '__main__':
    main()
