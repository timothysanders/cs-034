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
            j -= 1
        print(f"Current status of the list: {numbers}")
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