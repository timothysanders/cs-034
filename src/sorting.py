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


def insertion_sort_interleaved(numbers: list[int], start_index: int, gap: int) -> None:
    """

    Parameters
    ----------
    numbers
    start_index
    gap

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If an empty list, a negative start index, a gap value less than one,
        or a start index greater or equal to the length of the list.
    """
    if not numbers or start_index < 0 or gap < 1 or start_index >= len(numbers):
        raise ValueError("Invalid parameters")

    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            numbers[j], numbers[j - gap] = numbers[j - gap], numbers[j]
            j = j - gap


def shell_sort(numbers: list[int], gap_values: list[int]) -> None:
    """
    Sort a list of integers in-place using the Shell sort algorithm.

    The algorithm uses a sequence of gap values, which should typically be provided
    in descending order, with the final gap being 1 to ensure the list is fully sorted.

    Parameters
    ----------
    numbers : list[int]
        A list of integers to be sorted
    gap_values : list[int]
        A list of positive integers representing the gap sequence. This must contain at
        least one gap, and the final gap value should be 1.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If an empty list is provided for the gap values, or if gap values
        are provided in non-descending order, or do not end with one.
    """
    if not numbers:
        return None
    if not gap_values:
        raise ValueError("You must provide gap values")
    if gap_values != sorted(gap_values, reverse=True) or gap_values[-1] != 1:
        raise ValueError("Gap values must be in descending order and end with 1")

    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)
