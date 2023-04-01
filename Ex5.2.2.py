numbers = iter(range(1, 101))

# Print every 3rd number in iterable without using "if"
while True:
    try:
        next(numbers)
        next(numbers)
    except StopIteration:  # Consumed all
        break
    print(next(numbers))
