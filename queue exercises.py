from queue import Queue
from typing import Union


# Ex 1
def print_queue(q: Queue) -> None:
    """
    Prints queue elements as a list
    :param q: The queue to print
    :type q: Queue
    :return: None
    """
    print(list(q.queue))


# Ex 2
def max_in_queue(q: Queue[Union[int, float]]) -> int:
    """
    Finds max value in an ints queue
    :param q: The queue to search
    :type q: Queue[Union[int, float]]
    :return: The max value in the queue
    :rtype: int
    """
    return max(q.queue)


# Ex 3
def average_of_queue(q: Queue[Union[int, float]]) -> float:
    """
    Calculates the average of the queue elements
    :param q: The queue to find its average
    :type q: Queue[Union[int, float]]
    :return: The average of all the elements
    :rtype: float
    """
    length = len(q.queue)  # More efficient than q.qsize()
    if length == 0:
        return 0
    return float(sum(q.queue) / length)


# Ex 4
def print_elements(q: Queue, x: int) -> None:
    """
    Prints each element in queue x times in different lines
    :param q: Its elements need to be printed
    :type q: Queue
    :param x: The times to print each element
    :type x: int
    :return: None
    """
    for element in q.queue:
        for _ in range(x):
            print(element)


# Ex 7
def is_in_queue(q: Queue, x: int) -> bool:
    """
    Checks if x in the queue q
    :param q: The queue to search
    :type q: Queue
    :param x: The value to find in queue
    :type x: Any
    :return: Whether x is in queue or not
    :rtype: bool
    """
    return x in q.queue


# Ex 8
def only_positives(q: Queue[Union[int, float]]) -> Queue[Union[int, float]]:
    """
    Creates a new queue containing only positive elements from the original queue.
    :param q: The original queue
    :type q: Queue[Union[int, float]]
    :return: A queue containing only positive ints
    :rtype: Queue[Union[int, float]]
    """
    new_queue = Queue()

    for i in q.queue:
        if i > 0:
            new_queue.put(i)
    return new_queue


# Ex 10
def build_double_queue(n: int, m: int) -> Queue[int]:
    """
    Creates a queue containing even ints between n and m (excluded)
    :param n: Min value
    :type n: int
    :param m: Max value
    :type m: int
    :return: A queue with even ints
    :rtype: Queue[int]
    """
    queue_result = Queue()

    if n % 2 != 0:
        n += 1  # Make it even

    for i in range(n, m, 2):
        queue_result.put(i)
    return queue_result


my_queue = Queue()
for num in range(10, 80, 10):
    my_queue.put(num)

print_queue(my_queue)
