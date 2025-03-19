# Chapter 5: Sorting Algorithms

### 5.1: Sorting: Introduction
- **Sorting** is the process of converting a list of elements into ascending or descending order. The challenge with sorting is that a program cannot just see all elements of the list at the same time, so we have to perform a series of simpler operations, such as observing or swapping two elements at a time
### 5.2: Selection Sort
#### Selection sort
- **Selection sort** is a sorting algorithm that treats the input as two parts, a sorted part and an unsorted part, and repeatedly selects the proper next value to move from the unsorted part to the sorted part.
```python
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        if i != index_smallest:
            temp = numbers[i]
            numbers[i] = numbers[index_smallest]
            numbers[index_smallest] = temp
        print(f"Current status of the list: {numbers}")
    return numbers

numbers = [7,9,3,18,8]
assert selection_sort(numbers) == [3, 7, 8, 9, 18]
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
assert selection_sort(numbers) == [2, 4, 7, 10, 11, 32, 45, 78]
```
- In this sorting algorithm, elements to the left of `i` are sorted, and elements including and to the right of `i` are unsorted. All elements of the unsorted part are searched to find the index of the element with the smallest value, which is then swapped with the element at location `i`
#### Selection sort runtime
- Selection sort is easy to code, with one loop nested in another loop, but it can require a large number of comparisons. The runtime of selection sort is $O(N^2)$, if a list has N elements, the outer loop executes N - 1 times and the inner loop executes an average of $\frac{N}{2}$ times
  - This means that an array of $2N$ runs four times as long as $N$ and $10N$ runs 100 times as long as $N$
#### Challenge Activity
- When using selection sort to sort an array with 6 elements, what is the minimum number of assignments to indexSmallest once the outer loop starts?
  - Answer: 5
- When using selection sort, how many times longer will sorting an array of 12 elements take compared to sorting an array of 6 elements?
  - Answer: 4 (as input size increases by x times, the runtime increases $x^2$ times)
- Given array: [ 8, 9, 1, 6, 7 ] when using selection sort, what is the array after the first loop iteration
  - Answer: [ 1, 9, 8, 6, 7]
- Given array: 
Given array: [ 3, 5, 8, 2, 1 ] when using selection sort, what is the array after the second outer loop iteration
  - Answer: First loop [1, 5, 8, 2, 3] Second loop [1, 2, 8, 5, 3]

### 5.3: Python - Selection sort
#### Selection sort
- The `selection_sort()` function takes a list as a parameter and sorts the list in place
- The outer loop uses `i` to hold the index position of the item that will be sorted next and the inner loop uses j to examine all indices from i+1 to the end of the list. After the inner loop finishes, the variable `index_smallest` will store the index position of the smallest item in the list from `i` onward. Then, we swap values at `i` and `index_smallest` and repeat as needed
```python
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        if i != index_smallest:
            temp = numbers[i]
            numbers[i] = numbers[index_smallest]
            numbers[index_smallest] = temp
    return numbers
```
### 5.4: Insertion sort
#### Insertion sort algorithm
- **Insertion sort** is a sorting algorithm that treats the input as two parts, a sorted part and an unsorted part, and repeatedly inserts the next value from the unsorted part into the correct location in the sorted part
```python
def insertion_sort(numbers: list[int|float]) -> list[int|float]:
    """
    Sort an array of integers or floating point numbers in-place in ascending order.
    
    Parameters
    ----------
    numbers : list[int|float]
    
    Returns
    -------
    list[int|float]
    """
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            print(f"Current status of the list: {numbers}")
            j -= 1
    return numbers

numbers = [32, 6, 15, 3, 20]
assert insertion_sort(numbers) == [3, 6, 15, 20, 32]
```
- The index variable i denotes the starting point of the current element in the unsorted part. The first element (index 0) is assumed to be sorted, so the outer for loop initializes `i` to 1. The inner while loop inserts the current element into the sorted part by repeatedly swapping the current element with the elements in the sorted part that are larger. Once a smaller or equal element is found in the sorted part, the current element has been inserted in the correct location and the while loop terminates
#### Insertion sort runtime
- Insertion sort's typical runtime is $O(N^2)$, if a list has N elements, the outer loop executes N-1 times. Then for each inner loop, it may need to examine all elements of the sorted part, executing on average $\frac{N}{2}$ times
#### Nearly sorted lists
- For sorted and nearly sorted lists, insertion sort's runtime is $O(N)$. A **nearly sorted** list only contains a few elements that are not in sorted order
#### Insertion sort runtime for nearly sorted input
- For each outer loop execution, if the element is already in sorted position, only a single comparison is made. Each element not in sorted position requires at most N comparison. If there are a constant number, C, of unsorted elements, sorting the N - C sorted elements requires one comparison each, and sorting the C unsorted elements requires at most N comparisons each. This gives us a runtime of $O(N)$
#### Challenge Activity
- Given array [ 24, 30, 43, 45, 51, 25, 37, 40 ], when using insertion sort, what is the value of i when the first swap executes?
  - Answer: 5
- Which array leads to the best-case performance of insertion sort?
  - Answer: [15, 52, 68, 75, 94, 99]
- Which array leads to the worst-case performance of insertion sort?
  - Answer: [99, 84, 66, 47, 28, 15]
- Given array [ 20, 31, 42, 44, 57, 32, 41, 23, 53, 55 ], when `i` is 5, how many swaps will be performed in the inner loop of insertion sort?
  - Answer: 3
- Given array [ 18, 57, 39, 27, 56, 87, 65, 32 ], when using insertion sort, what is the array after three iterations of the outer loop?
  - Answer: [18, 27, 39, 57, 56, 87, 65, 32]
- Given array [ 69, 10, 43, 74, 19, 98, 75 ], how many swaps are needed to sort the array with insertion sort?
  - Answer: 6
    1. [10, 69, 43, 74, 19, 98, 75]
    2. [10, 43, 69, 74, 19, 98, 75]
    3. [10, 43, 69, 19, 74, 98, 75]
    4. [10, 43, 19, 69, 74, 98, 75]
    5. [10, 19, 43, 69, 74, 98, 75]
    6. [10, 19, 43, 69, 74, 75, 98]
### 5.5: Python - Insertion Sort
#### Insertion sort algorithm
- The `insertion_sort()` function has one parameter, `numbers`, which is an unsorted list of elements. Because the list is a mutable object, changes to the list in the function will affect any variable that references that list.
- The index variable `i` denotes the starting position of the current element in the unsorted part of the list, we assume the first element is sorted, so we start with `i == 1`. The inner while loop inserts the current element into the sorted part by repeatedly swapping the current element with the elements of the sorted part that are larger. Once a smaller or equal element is found in the sorted part, the current element has been inserted at the correct location and the while loop terminates.

### 5.6: Shell Sort
#### Shell sort's interleaved lists
- **Shell sort** is a sorting algorithm that treats the input as a collection of interleaved lists, sorting each list individual with a variation of insertion sort. Shell sort uses **gap values** to determine the number of interleaved lists. These gap values are positive integers representing the distance between elements in an interleaved list. For each interleaved list, if an element is at index `i`, the next element is at index `i` + gap value.
- Shell sort starts by choosing a gap value of `K` and sorting `K` interleaved lists. Shell sort finishes by performing a standard insertion sort on the entire array, which is quick because the interleaved portions have already been sorted.
#### Insertion sort for interleaved lists
- If a gap value of `K` is chosen, creating `K` entirely new lists is computationally expensive, so instead, the shell sort algorithm sorts the interleaved lists in-place with a variation of insertion sort. This variation of insertion sort redefines "next" and "previous" items, so for an index at `X`, the next item is `X + K` (instead of `X + 1`) and the previous item is `X - K` (instead of `X - 1`)
#### Shell sort algorithm
- Shell sort begins by picking an arbitrary collection of gap values, for each gap value of `K`, `K` calls are made to the insertion sort variant function to sort `K` interleaved lists. Shell sort ends with a final gap value of 1, finishing with a regular insertion sort
- Shell sort performs well when choosing gap values in descending order, such as choosing the powers of 2 minus 1. For example, an array of size 100, would have gap values of 63, 31, 15, 7, 3, 1
#### Challenge Activity
- The following array is given: [ 45, 80, 44, 27, 31 ] A gap value of 2 is used, so the array is treated as 2 interleaved arrays.
  - What is the first interleaved array?
    - Answer: [45, 44, 31]
  - What is the second interleaved array?
    - Answer: [80, 27]
- Given an array [ 24, 51, 33, 15, 53, 17, 83, 52, 73, 87 ] and a gap value of 5: What is the array after shell sort with a gap value of 5?
  - Answer: [17, 51, 33, 15, 53, 24, 83, 52, 73, 87]
- Given an array [ 86, 91, 44, 47, 52, 67 ] and a gap array of [ 4, 2, 1 ]:
  - What is the array after shell sort with a gap value of 4?
    - Answer: [52, 67, 44, 47, 86, 91]
  - What is the resulting array after shell sort with a gap value of 2?
    - Answer: [44, 47, 52, 67, 86, 91] 
  - What is the resulting array after shell sort with a gap value of 1?
    - Answer: [44, 47, 52, 67, 86, 91]
### 5.7: Python - Shell Sort
#### Sorting interleaved lists for shell sort
- Shell sort uses a variation of the insertion sort algorithm to sort subsets of an input list. Instead of sorting items immediately adjacent to each other, it compares elements that are a fixed distance apart, known as a gap space (our gap value from before). Shell sort repeats this process using different gap sizes and starting points within the input list.
```python
def insertion_sort_interleaved(numbers: list[int], start_index: int, gap: int) -> None:
    if not numbers or start_index < 0 or gap < 1 or start_index >= len(numbers):
        raise ValueError("Invalid parameters")
    
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            numbers[j], numbers[j - gap] = numbers[j - gap], numbers[j]
            j = j - gap

def shell_sort(numbers: list[int], gap_values):
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)

```
#### Shell sort algorithm
- `shell_sort()` calls the `insertion_sort_interleaved()` function repeatedly using gap sizes and start indices. For example, if a gap value is 3, then `shell_sort()` executes the following
  - `insertion_sort_interleaved(numbers, 0, 3)`
  - `insertion_sort_interleaved(numbers, 1, 3)`
  - `insertion_sort_interleaved(numbers, 2, 3)`
- All values from 0 to gap size - 1 are used as the start_index and this process repeats for all gap values
- Choosing good gap values will minimize the total number of swap operations, but the only requirement is that one of the gap values (typically the last one) is 1. These gap values are often specified in decreasing order and a gap value of 1 is equivalent to the regular insertion sort algorithm. If you specify larger gap values first, the final insertion sort will have to do less work.
  - A common strategy is to use the powers of two (minus one), so 31, 15, 7, 3, 1, etc.

### 5.8: Quicksort
#### Quicksort
- **Quicksort** is a sorting algorithm that repeatedly partitions the input into low and high parts (each part unsorted), then recursively sorts each of those parts. To partition the input, quicksort chooses a pivot to divide the data into low and high parts. The **pivot** is any value in the array being sorted, usually the value of the middle array element. For example, in `[4, 34, 10, 25, 1]` the pivot could be 10
- After choosing the pivot, the quicksort algorithm divides the array into two parts, the low partition and the high partition. All values in the low partition are less than or equal to the pivot value and all values in the high partition are greater than or equal to the pivot value (remember, these partitions are not sorted). Using our previous example of `[4, 34, 10, 25, 1]`, we end up with a low partition of `[4, 1, 10]` and a high partition of `[25, 34]`. Values equal to the pivot value may appear in either or both of the partitions.
#### Partitioning algorithm
- The partitioning algorithm uses two index variables, low_index and high_index, initialized to the left and right sides of the current elements being sorted. While the value of index low_index is less than the pivot value, the algorithm increments low_index, because that value should remain in the low partition. Similarly, while the value at high_index is greater than the pivot value, the algorithm decrements high_index, because that value should remain in the high partition. Then if low_index >= high_index, all elements have been partitioned and the partitioning algorithm returns the value of high_index, which is the last element in the low partition. Otherwise, the elements at indices low_index and high_index are swapped to move them to the correct partition. The algorithm then increments low_index, decrements high_index, and repeats.
```python
def partition(numbers: list[int|float], low_index: int, high_index: int) -> int:
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

def quicksort(numbers: list[int|float], low_index: int, high_index: int) -> None:
    """
    Sort a segment of the list using quicksort algorithm.
    
    Parameters
    ----------
    numbers : list
        The list to be sorted (modified in-place)
    low_index : int
        The lower bound of the segment to be sorted
    high_index : int
        The upper bound of the segment to be sorted
    """
    # Our base case is where the partition size is 1 or zero elements
    if low_index >= high_index:
        return
    
    partition_index = partition(numbers, low_index, high_index)
    
    quicksort(numbers, low_index, partition_index)
    quicksort(numbers, partition_index + 1, high_index)

numbers = [10, 2, 78, 4, 45, 32, 7, 11]
```
#### Recursively sorting partitions
- After each partition has been created, each partition needs to be sorted. Quicksort is typically implemented recursively, using quicksort to sort the low and high partitions. This recursive sorting process continues until a partition has one or zero elements, which will already be sorted.
#### Quicksort runtime
- The quicksort algorithm runtime is usually `O(N log N)`. Because the quicksort has several partitioning levels, the first level divides the input into two parts, the second into four parts, the third into eight parts, etc. At each level, the algorithm does at most `N` comparisons moving the low_index and high_index indices. If the pivot gives you two equal sized parts, there will be log N levels, requiring the `N * log N` comparisons
#### Worst case runtime
- For unsorted data, equal partitioning typically occurs, but partitioning may give you unequally sized parts in some cases. If the pivot you select for partitioning is the largest or smallest value, you will have one partition of one element and the other partition will have all other elements. If this were to happen at every level, you would have `N - 1` levels, giving you a runtime of $O(N^2)$, which fortunately, rarely occurs.
#### Challenge Activity
- Given numbers = [76, 28, 42], lowIndex = 0, highIndex = 2
  - When quicksort is used, what is the midpoint?
    - Answer: 1
  - When quicksort is used, what is the pivot?
    - Answer: 28
- Given numbers = [20, 52, 51, 89, 72, 75, 29, 67, 36, 38], lowIndex = 0, highIndex = 9
  - When quicksort is used, what is the midpoint?
    - Answer: 4
  - When quicksort is used, what is the pivot?
    - Answer: 72
- Given numbers = [93, 87, 59, 20, 82], lowIndex = 1, highIndex = 4
  - What is the midpoint?
    - Answer: 2
  - What is the pivot?
    - Answer: 59
- Given numbers = [32, 33, 69, 37, 48, 43, 53], pivot = 37
  - What are the elements in the low partition after partitioning?
    - Answer: [32, 33, 37]
  - What are the elements in the high partition after partitioning?
    - Answer: [69, 48, 43, 53]
- numbers = [13, 29, 21, 43, 36, 38, 46, 33, 64, 58] Partition(numbers, 3, 9) is called. So, only elements in indices 3 to 9 are partitioned. Elements in indices 0 to 2 are not affected. Assume quicksort always chooses the element at the midpoint as the pivot.
  - What is the pivot?
    - Answer: 46
  - What is the low partition?
    - Answer: [43, 36, 38, 33]
  - What is the high partition?
    - Answer: [46, 64, 58]
  - What is numbers after partition(numbers, 3, 9) completes?
    - Answer: [13, 29, 21, 43, 36, 38, 33, 46, 64, 58]
- How many partitioning levels are required for a list of 16 elements if quicksort:
  - always chooses a pivot that divides the elements into two equal parts?
    - Answer: 4
  - always chooses the largest element as the pivot?
    - Answer 15

### 5.9: Python - Quicksort
#### The `partition()` function
- The quicksort algorithm partitions a section of the unsorted list into a low portion and a high portion, based on the pivot element within the list. `partition()` has three parameters, the unsorted list, the start index, and the end index. When the function completes, the elements between the start and end indices are reorganized so that items in the lower part are less than or equal to the pivot and items in the higher part are greater than or equal to the pivot. These parts may be different sizes, and the function returns the index of the last item in the lower part. These parts themselves are not sorted.
#### The `quicksort()` algorithm
- Quicksort uses recursion to sort the two parts of the list, eventually sorting the full list. The function has three parameters: the unsorted list, the start index, and the end index. `quicksort()` calls `partition()` to create low and high parts, `quicksort()` then calls itself, using recursion to sort the two list parts. You can use `quicksort()` with a start_index of 0, end_index of the last item in the list to sort the list.

### 5.10: Merge sort
#### Merge sort overview
- **Merge sort** is a sorting algorithm that divides a list into two halves, recursively sorts each half, then merges the sorted halves to produce a sorted list. The recursive sorting continues until a list of 1 element is reached, as this is already sorted.
#### Merge sort partitioning
- Merge sort uses three index variables to keep track of elements to sort in each recursive function call. Variable `i` is the index of the first element in the list, `k` is the index of the last element, `j` is used to divide the list into two halves. Elements from `i` to `j` are in the left half, elements from `j + 1` to `k` are in the right half
#### Merge sort algorithm
- Merge sort merges the two partitions into a single list by repeatedly selecting the smallest element from either the left or right partition and adding that element to the temporary merged list. Once fully merged, this temporary merged list is copied back to the original list
```python
def merge(numbers: list[int|float], i: int, j: int, k: int) -> None:
    """
    Merge two sorted subarrays into a single sorted subarray.
    
    Parameters
    ----------
    numbers : list[int|float]
        The list containing the subarrays to merge
    i : int
        Start index of the first subarray
    j : int
        End index of the first subarray
    k : int
        End index of the second subarray (second subarray starts at j+1)
    """
    merged_size = k - i + 1
    merged_numbers = [0] * merged_size
    merge_position = 0
    left_position = i
    right_position = j + 1
    # Add the smallest element from left or right partition to merged numbers
    while left_position <= j and right_position <= k:
        if numbers[left_position] <= numbers[right_position]:
            merged_numbers[merge_position] = numbers[left_position]
            left_position += 1
        else:
            merged_numbers[merge_position] = numbers[right_position]
            right_position += 1
        merge_position += 1
    # If left partition is not empty, add remaining elements to merged numbers
    while left_position <= j:
        merged_numbers[merge_position] = numbers[left_position]
        left_position += 1
        merge_position += 1
    # If right partition is not empty, add remaining elements to merged numbers
    while right_position <= k:
        merged_numbers[merge_position] = numbers[right_position]
        right_position += 1
        merge_position += 1
    # Copy merge back to original list
    for mp in range(merged_size):
        numbers[i + mp] = merged_numbers[mp]

def merge_sort(numbers: list[int|float], i: int, k: int) -> None:
    """
    Sort a subarray using the merge sort algorithm.
    
    Parameters
    ----------
    numbers : list[int|float]
        The list to be sorted (sorted in-place)
    i : int
        Start index of the subarray to be sorted
    k : int
        End index of the subarray to be sorted
    """
    if i < k:
        j = (i + k) // 2
        # recursively sort left and right partitions
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        # merge left and right partition in sorted order
        merge(numbers, i, j, k)
```
#### Merge sort runtime
- The merge sort algorithm's runtime is $O(N \log{N})$. Merge sort divides the input in half until a list of 1 element is reached, which requires log N partitioning levels. At each level, the algorithm does ~N comparisons to select and copy elements from left and right partitions, giving N * log N comparisons
- Merge sort requires O(N) additional memory elements for the temporary array of merged elements, which has the same number of elements as the input. To allocate this temporary array, the `merge()` function creates its own array
#### Challenge Activity
- numbers: [46, 14, 37, 24, 61, 38]
  - What arguments should be provided to MergeSort() to sort the numbers array?
    - Answer: merge_sort(numbers, 0, 5)
- numbers1: [35, 36, 65, 68, 74, 80] numbers2: [13, 19, 20, 46, 60, 78]
  - What are the first two elements compared when merging numbers1 and numbers2 with merge sort?
    - Answer: 35, 13
  - What are the next two elements compared when merging numbers1 and numbers2 with merge sort?
    - Answer, 35, 19
- numbers: [28, 13, 67, 62, 89, 19, 74, 15]
  - merge_sort(numbers, 0, 7) is called. The next two calls to merge_sort() are:
    - Answer: merge_sort(numbers, 0, 3)
    - Answer: merge_sort(numbers, 0, 1)
- numbers: [36, 67, 74, 23, 31, 55]
- numbers: [21, 51, 66, 60, 85]
  - merge_sort(numbers, 0, 4) is called. merge() is called to merge the following partitions:
### 5.11: Python - Merge sort
#### Merge sort algorithm
- Merge sort divides a list into two halves, recursively sorting each half, then merging the sorted halves to give a sorted list, and makes use of two functions, `merge()` and `merge_sort()`.
- `merge()` merges two sequential, sorted partitions within a list and requires 4 parameters
  - The list of numbers containing the two sorted partitions to merge
  - The start index of the first sorted partition
  - The end index of the first sorted partition
  - The end index of the second sorted partition
- `merge_sort()` sorts a partition in a list and has three parameters
  - The list containing the partition to sort
  - The start index of the partition to sort
  - The end index of the partition to sort
- If a partition size is greater than one, `merge_sort()` recursively sorts the left and right halves of the partition, then merges those sorted halves together. If the start index is 0 and the end index is the list length - 1, `merge_sort()` sorts the entire list

### 5.12: Radix sort
#### Buckets
- Radix sort is an algorithm designed specifically for integers and makes use of a concept called buckets and is a type of bucket sort. Arrays of integers can be subdivided into buckets by using the digits of integer values and a **bucket** is a collection of values that share a particular digit value. For example, 57, 97, 77, and 17 all have 7 in the 1's digit
#### Radix sort algorithm
- **Radix sort** is a sorting algorithm for arrays of *integers*. The algorithm processes one digit at a time, starting with the least significant digit and ending with the most significant. There are two steps for each digit, first, all array elements are placed into buckets based on the current digit's value, then the array is rebuilt by removing all elements from buckets, from the lowest bucket to highest bucket. This algorithm can also be applied to non-base 10 integers
#### Sorting signed integers
- To handle signed integers, we need two buckets, one for negative integers and one for non-negative integers, with integers from the array placed into the appropriate bucket. Then the algorithm reverses the order of the negative bucket and concatenates the buckets to give a sorted array
#### Challenge Activity
- Given array: (3, 45, 37, 5, 87, 731, 142) what is the array after sorting based on the 1's digit?
  - Answer: 731, 142, 3, 45, 5, 37, 87
- Given array: (57, 951, 4, 15, 9, 74) After putting into buckets based on the 1's digit, the array is: (951, 4, 74, 15, 57, 9) What is the array after sorting based on the 10's digit?
  - Answer: 4, 9, 15, 951, 57, 74
- Given array: (-482, 4, -30, -905, -53, 43)
  - After initial sorting, but before the negative and non-negative buckets are built, what is the array?
    - Answer: 4, -30, 43, -53, -482, -905
  - After reversal, what integers are in the negative bucket?
    - Answer: -905, -482, -53, -30

### 5.13: Python - Radix sort
#### Radix sort algorithm
- The **radix sort** algorithm sorts a list of integers by grouping elements based on the element's digits, starting with the least significant digit and ending with the most significant
- First, all list elements are placed into buckets based on the current digit's value. Then, the list is rebuilt by removing all elements from buckets, in order from lowest bucket to highest.
- The `radix()` function takes one parameter, numbers, which is the unsorted list of integers. A list of 10 lists is used for the buckets
```python
def radix_get_max_length(numbers: list[int]) -> int:
    """
    Return the maximum length of a number in numbers.
    
    Parameters
    ----------
    numbers : list[int]
    
    Returns
    -------
    int
    """
    max_digits = 0
    for num in numbers:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits

def radix_get_length(value: int) -> int:
    """
    Return the length of a given value, in number of digits.
    
    Parameters
    ----------
    value : int
    
    Returns
    -------
    int
    """
    if value == 0:
        return 1
    digits = 0
    while value != 0:
        digits += 1
        value = int(value / 10)
    return digits

def radix_sort(numbers: list[int]) -> None:
    """
    Sort the array numbers using the radix sort algorithm.
    
    Parameters
    ----------
    numbers : list[int]
    
    Returns
    -------
    None
    """
    buckets = []
    for i in range(10):
        buckets.append([])
    # find the max length of any number in the provided numbers
    max_digits = radix_get_max_length(numbers)
    pow_10 = 1
    for digit_index in range(max_digits):
        for num in numbers:
            bucket_index = (abs(num) // pow_10) % 10
            buckets[bucket_index].append(num)
        numbers.clear()
        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()
        pow_10 *= 10

    negatives = []
    non_negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    numbers.clear()
    numbers.extend(negatives + non_negatives)
```

### 5.14: Overview of fast sorting algorithms
#### Fast sorting algorithm
- A **fast sorting algorithm** is one that has an average runtime complexity of $O(N \log{N})$ or better.

| Sorting algorithm | Average case runtime complexity | Fast? | Comparison |
|-------------------|---------------------------------|-------|------------|
| Selection sort    | O($N^2$)                        | No    | Yes        |
| Insertion sort    | O($N^2$)                        | No    | Yes        |
| Shell sort        | O($N^{1.5}$)                    | No    | Yes        |
| Quicksort         | O($N\log N$)                    | Yes   | Yes        |
| Merge sort        | O($N\log N$)                    | Yes   | Yes        |
| Heap sort         | O($N\log N$)                    | Yes   | Yes        |
| Radix sort        | O($N$)                          | Yes   | No         |
#### Comparison sorting
- An **element comparison sorting algorithm** is one that operates on an array of elements that can be compared to each other, such as an array of strings.
- Selection sort, insertion sort, shell sort, quicksort, merge sort, and heap sort are all comparison sorting algorithms, which radix sort is not.
#### Best and worst case runtime complexity
- A fast sorting algorithm's best/worst case runtime complexity may differ from its average runtime complexity

| Sorting algorithm | Best case runtime complexity | Average case runtime complexity | Worst case runtime complexity |
|-------------------|------------------------------|---------------------------------|-------------------------------|
| Quicksort         | O($N\log N$)                 | O($N\log N$)                    | O($N^2$)                      |
| Merge sort        | O($N\log N$)                 | O($N\log N$)                    | O($N\log N$)                  |
| Heap sort         | O($N$)                       | O($N\log N$)                    | O($N\log N$)                  |
| Radix sort        | O($N$)                       | O($N$)                          | O($N$)                        |

### 5.15: Python - Sorting with different operators
#### Sorting with Python built-ins
- Many Python objects have natural ordering, which means that when two objects of the type are compared, one comes before the other in some way (or the objects are equal). Natural ordering is used by the comparison operators `<, <=, >, >=, ==, !=`
- Python has a built-in `sorted()` function that takes a list argument, sorts the items in ascending order, then returns a new sorted list
- Python lists also have a `sort()` method that does in place sorting in ascending order
##### Sorting in descending order with `sorted()` and `sort()`
- These two built-ins can take an optional `reverse` keyword argument that, when True, sorts the list in descending order
#### Using a key function
- These two built-ins also can take an optional key argument, which is a function that determines how to sort the list, such as sorting words in a case-insensitive way. Note that the key parameter is the function itself, not calling the function
##### Custom key function
- A common use for the key parameter is to sort a list by one of an element's values if the items in the list are a tuple.
- Custom key functions must be defined to only have one parameter, a single list element
##### The `itemgetter()` function
- A special function, `itemgetter()`, is defined in Python's operator module to get a key from an element using an index instead of a custom key function. For example, instead of creating a custom key function `key_is_name()`, you can use `operator.itemgetter(0)`. The `itemgetter()` function returns a function