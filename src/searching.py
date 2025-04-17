
def linear_search(numbers: list[int|float], key: int|float) -> int:
    """
    Perform a linear search of an array of numbers for a key, return the index of the key, if found.

    Parameters
    ----------
    numbers : list[int|float]
        The list of numbers to search
    key : int|float
        The key value to search for within `numbers`

    Returns
    -------
    int
        The index of the found item, -1 if not found.
    """
    for i, num in enumerate(numbers):
        if num == key:
            return i
    return -1

def binary_search(numbers: list[int|float], key: int|float) -> int:
    """
    Perform a binary search on the given list of numbers for the provided key.

    Note that the input list of numbers must be sorted in ascending order.

    Parameters
    ----------
    numbers : list[int|float]
        List of numbers to be searched. Must be sorted in ascending order.
    key : int|float
        Key value to search within the provided list.

    Returns
    -------
    int
        The index of the found key, -1 if not found.
    """
    low = 0
    high = len(numbers) - 1
    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1
