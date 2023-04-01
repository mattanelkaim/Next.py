# names.txt contains names separated by new lines
def print_longest_name(file_path: str) -> None:
    """
    Prints the longest name in a file
    :param file_path: The path to the file
    :type file_path: str
    :return: None
    """
    with open(rf"{file_path}", 'r') as file:
        print(max(file.read().splitlines(), key=len))


def print_total_names_length(file_path: str) -> None:
    """
    Prints the sum of the length of the names in a file
    :param file_path: The path to the file
    :type file_path: str
    :return: None
    """
    with open(rf"{file_path}", 'r') as file:
        print(sum(len(name) for name in file.read().splitlines()))


def print_shortest_names(file_path: str) -> None:
    """
    Prints the shortest names in a file
    :param file_path: The path to the file
    :type file_path: str
    :return: None
    """
    with open(rf"{file_path}", 'r') as file:
        content = file.read().splitlines()
        min_length = len(min(content, key=len))
        print('\n'.join([name for name in content if len(name) == min_length]))


def write_lengths(src_file_path: str, dst_file_path: str) -> None:
    """
    Writes the length of each name from dst_file in a new file separated by newlines
    :param src_file_path: The path to the file containing the names
    :type src_file_path: str
    :param dst_file_path: The path to a new/existing file that will contain the lengths
    :type dst_file_path: str
    :return: None
    """
    with open(rf"{dst_file_path}", 'w') as dst_file:
        with open(rf"{src_file_path}", 'r') as src_file:
            dst_file.write(('\n'.join(map(lambda x: str(len(x)), src_file.read().splitlines()))))


def print_elements_with_length(file_path: str) -> None:
    """
    Prints all names with a length (inputted from user) in a file
    :param file_path: The path to the file
    :type file_path: str
    :return: None
    """
    word_length = int(input("Enter name length: "))
    with open(rf"{file_path}", 'r') as file:
        print('\n'.join([x for x in file.read().splitlines() if len(x) == word_length]))


def main():
    print_longest_name("names.txt")
    print_total_names_length("names.txt")
    print_shortest_names("names.txt")
    write_lengths("names.txt", "name_length.txt")
    print_elements_with_length("names.txt")


if __name__ == "__main__":
    main()
