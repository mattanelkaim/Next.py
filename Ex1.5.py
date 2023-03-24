# names.txt contains names separated by new lines
from functools import reduce


def get_longest_name(file_path: str) -> None:
    with open(file_path, 'r') as file:
        print(sorted(file.read().splitlines(), key=len)[-1])


def get_chars_length(file_path: str) -> None:
    with open(file_path, 'r') as file:
        print(reduce(lambda x, y: x + len(y), file.read().splitlines(), 0))


def print_shortest(file_path: str) -> None:
    with open(file_path, 'r') as file:
        content = file.read().splitlines()
        min_length = len(min(content, key=len))
        print("\n".join(filter(lambda x: len(x) == min_length, content)))


def write_lengths(src_file_path: str, dst_file_path: str) -> None:
    with open(dst_file_path, 'w') as dst_file:
        with open(src_file_path, 'r') as src_file:
            dst_file.write(("\n".join([str(len(x)) for x in src_file.read().splitlines()])))


def print_elements_by_length(file_path: str) -> None:
    word_length = int(input("Enter name length: "))
    with open(file_path, 'r') as file:
        print("\n".join([x for x in file.read().splitlines() if len(x) == word_length]))


def main():
    get_longest_name("names.txt")
    get_chars_length("names.txt")
    print_shortest("names.txt")
    write_lengths("names.txt", "name_length.txt")
    print_elements_by_length("names.txt")


if __name__ == "__main__":
    main()
