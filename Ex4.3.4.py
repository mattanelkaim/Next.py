from typing import Generator


def get_fibo() -> Generator[int, int, None]:
    """
    A generator function that yields the next num in
    the Fibonacci sequence on each call.
    :return: A generator with the Fibonacci elements
    :rtype: Generator[int, int, None]
    """
    a, b = 0, 1  # Init first values of series
    while True:
        yield a
        a, b = b, a + b


def main():
    fibo_gen = get_fibo()
    for _ in range(1_000):
        print(next(fibo_gen))


if __name__ == '__main__':
    main()
