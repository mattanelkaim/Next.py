NOTES_FREQUENCIES = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
NUM_OF_OCTAVES = 5
NOTES_PER_OCTAVE = len(NOTES_FREQUENCIES)
TOTAL_NOTES = NOTES_PER_OCTAVE * NUM_OF_OCTAVES


class MusicNotes:
    """
    An iterator that represents music notes.
    :ivar _index: The index of the current note in the iterator
    """
    def __init__(self):
        # Could have used a list, but it's much more efficient to calc values and return directly
        # self._notes_list = [x * (2 ** y) for y in range(NUM_OF_OCTAVES) for x in NOTES_FREQUENCIES]
        self._index = -1

    def __iter__(self) -> "MusicNotes":
        return self

    def __next__(self) -> float:
        """
        Calculates the next note in the iterator.
        :return: The next note in the iterator
        :rtype: float
        :raises StopIteration: If there are no more elements in the iterator
        """
        self._index += 1
        if self._index >= TOTAL_NOTES:
            raise StopIteration

        current_note = self._index % NOTES_PER_OCTAVE
        current_octave = self._index // NOTES_PER_OCTAVE
        return NOTES_FREQUENCIES[current_note] * (2 ** current_octave)


def main():
    my_notes = MusicNotes()

    for freq in my_notes:
        print(freq)


if __name__ == '__main__':
    main()
