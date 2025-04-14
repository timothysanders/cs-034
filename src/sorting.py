"""
Sorting algorithm implementations

Implementations of the following algorithms
- selection sort
- insertion sort
"""

def selection_sort(numbers: list[int]) -> None:
    """
    Implementation of the selection sort algorithm.

    Note: The sorting of the list is done in place, modifying the original list.

    Parameters
    ----------
    numbers : list[int]
        The list of numbers to be sorted

    Returns
    -------
    None
    """
    for i in range(len(numbers) - 1):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        if i != index_smallest:
            numbers[i], numbers[index_smallest] = numbers[index_smallest], numbers[i]


def insertion_sort(numbers: list[int | float]) -> None:
    """
    Sort an array of integers or floating point numbers in-place in ascending order.

    Parameters
    ----------
    numbers : list[int|float]

    Returns
    -------
    None
    """
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
