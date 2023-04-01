import winsound

FREQUENCIES = {"la": 220,
               "si": 247,
               "do": 261,
               "re": 293,
               "mi": 329,
               "fa": 349,
               "sol": 392,
               }
NOTES = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

sounds = ((FREQUENCIES[a], int(b)) for note in NOTES.split("-") for a, b in [note.split(",")])

# Create a for loop using while
while True:
    try:
        frequency, duration = next(sounds)
    except StopIteration:
        break

    print(frequency, duration)
    winsound.Beep(frequency, duration)
