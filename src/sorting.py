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
    Sort the given subarray of numbers in place, using insertion sort.

    This sorts the given array starting from the element at `start_index` and
    every additional element at multiples of `gap`

    Parameters
    ----------
    numbers : list[int]
        The list of integers to be partially sorted
    start_index
        The index at which to begin sorting
    gap
        The step interval between elements in the interleaved subarray

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


def partition(numbers: list[int | float], low_index: int, high_index: int) -> int:
    """
    Partition the array segment and return the partition index.

    Parameters
    ----------
    numbers : list
        The list to be partitioned
    low_index : int
        The lower bound of the segment to be partitioned
    high_index : int
        The upper bound of the segment to be partitioned

    Returns
    -------
    int
        The index where the partition ends
    """
    # Identify the midpoint/pivot value using floor division
    midpoint = low_index + (high_index - low_index) // 2
    pivot = numbers[midpoint]
    done = False
    while not done:
        while numbers[low_index] < pivot:
            low_index += 1
        while pivot < numbers[high_index]:
            high_index -= 1
        if low_index >= high_index:
            done = True
        else:
            numbers[low_index], numbers[high_index] = numbers[high_index], numbers[low_index]
            low_index += 1
            high_index -= 1
    return high_index


def quicksort(numbers: list[int | float], low_index: int, high_index: int) -> None:
    """
    Sort a list in-place using quicksort algorithm.

    This implementation relies on the Hoare partition schema and
    will select the pivot as the middle index of the given list.

    Parameters
    ----------
    numbers : list
        The list to be sorted (modified in-place)
    low_index : int
        The lower bound of the segment to be sorted
    high_index : int
        The upper bound of the segment to be sorted
    """
    # Our base case for recursion is where the partition size is 1 or zero elements
    if low_index >= high_index:
        return

    partition_index = partition(numbers, low_index, high_index)
    quicksort(numbers, low_index, partition_index)
    quicksort(numbers, partition_index + 1, high_index)