def translate(sentence: str) -> str:
    """
    Translates the original sentence from Spanish to English
    :param sentence: The Spanish sentence to translate
    :type sentence: str
    :return: The translated sentence to English
    :rtype: str
    """
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    new_sentence = " ".join((words.get(word) for word in sentence.split()))
    return new_sentence


def main():
    print(translate("el gato esta en la casa"))


if __name__ == '__main__':
    main()
