def read_file(file_name: str) -> str:
    """
    Returns the content of a file if it exists,
    else handles the error and specifies error in return
    :param file_name: The path to the file
    :type file_name: str
    :return: File content / error if file not found
    :rtype: str
    """
    # Intentionally unoptimized: must use try, except, else and finally
    final_string = ["__CONTENT_START__\n"]
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        final_string.append("__NO_SUCH_FILE__")
    else:
        final_string.append(content)
    finally:
        final_string.append("\n__CONTENT_END__")
        return ''.join(final_string)  # "Cast" to string


def main():
    print(read_file("Ex3.2.5.py"))


if __name__ == '__main__':
    main()
