# Chapter 4: Searching and Algorithm Analysis

### 4.1: Searching and Algorithms
#### Algorithms
- **Algorithm** is a series of steps for solving a task, an example of an algorithm being a **linear search** algorithm. A linear search starts from the beginning of a list and checks every item in the list until the search key is found or the end of the list is reached.
```python
def linear_search(numbers, numbers_size, key):
    i = 0
    while i < numbers_size:
        if numbers[i] == key:
            return i
        i += 1
    return -1

numbers = [54, 79, 26, 91, 29, 33]
linear_search(numbers, len(numbers), 54)
linear_search(numbers, len(numbers), 82)
```
#### Algorithm runtime
- The runtime of an algorithm is the amount of time it takes to execute. If each comparison takes 1 microsecond, then a linear search algorithm for a list with 200 million items could take more than 3 minutes.
- Algorithms typically use a number of steps proportional to the size of the input. For the linear search algorithm, if there are 32 items in the list, the algorithm will require at most 32 comparisons, or for a list with `N` elements, linear search requires at most `N` comparisons. The algorithm is said to require "on the order" of `N` comparisons

### 4.2: Binary Search
#### Linear search vs. binary search
- Because linear search could require searching every element in a list, it can take a long time to run. If the list is sorted, however, a faster search, called **binary search** can be conducted. This algorithm checks the middle value first, if the desired value is lower, then the binary search searches the first half, otherwise the last half, with each step reducing the values that need to be searched by half
#### Binary search algorithm
- **Binary search** is a faster algorithm for searching a list, if the elements are sorted and are directly accessible (such as an array). This algorithm checks the middle element of the list, if the search key is found, the algorithm returns the matching location. If the search key is not found, the algorithm repeats the search on the left or right sublist (depending on if the search key was greater or less than the previously checked value).
```python
def binary_search(numbers, numbers_size, key):
    mid = 0
    low = 0
    high = numbers_size - 1
    while high >= low:
        mid = int((high + low) / 2)
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

numbers = [2, 4, 7, 10, 11, 32, 45, 87]
binary_search(numbers, len(numbers), 0)
binary_search(numbers, len(numbers), 10)
```
#### Binary search efficiency
- Binary search is very efficient for finding elements in sorted arrays, as it reduces the search space by about half in each step. For an `N` element array, the maximum number of steps required to reduce the search space to an empty subarray is $log_2N + 1$
- If each comparison takes 1 microsecond, then the binary search algorithm's runtime is at most 20 microseconds for a list with 1,000,000 elements, 21 microseconds for 2,000,000 element, 22 microseconds for 4,000,000 elements, etc. Using the example from before with 200,000,000 items, binary search requires less than 28 microseconds, which is up to 7,000,000 times faster than linear search

### 4.3: Python: Linear and binary search
#### Linear search
- Search algorithms are used to find the location of a particular key element from a list, or indicate that the key is not in the list. Linear search starts from the beginning of the list and checks every element, one at a time, until either the search key is found or the end of the list is reached. An example implementation is shown below
```python
def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1

linear_search([2, 4, 7, 10, 11, 32, 45, 87], 45)
linear_search([4, 7, 9, 11, 15, 18, 20, 22, 54], 55)
```
#### Binary search
- The binary search algorithm finds a location of a key value in a list, but is much faster than linear search, due to the operations it performs on a sorted list. Binary search compares the middle element of the list to the key, if the key matches, the number is returned and the algorithm is done. If the key is smaller, the loop proceeds to search the first half of the list, if the key is larger, the loop proceeds to search the last half of the list. The search field is always cut in half, which results in many fewer comparisons.
- To get the index of the middle of the low and high indices, the sum of the high and low indices is divided by two, if this result is not an integer, the result is rounded down to the nearest whole number using floor division, the operation can be written as `mid = (high + low) // 2`
```python
def binary_search(numbers, key):
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] < key:
            high = mid - 1
        else:
            return mid
    return -1


binary_search([2, 4, 7, 10, 11, 32, 45, 87], 10)
binary_search([2, 4, 7, 10, 11, 32, 45, 87], 45)
```
### 4.4: Constant time operations
#### Constant time operations
- Designing efficient algorithms aims to lower the amount of time needed for the algorithm to run. However, faster processors run algorithms more quickly, so we describe algorithm runtime in terms of constant time operations, not units of time. A **constant time operation** is an operation that always operates in the same amount of time, regardless of the input values. 
  - Examples of constant time operations are assignment statements and multiplication, while operations like loops and string concatenations are examples of operations that are not constant time.
  - Keep in mind that multiple constant time operations taken together may be considered a constant time operation (a constant times a constant is still a constant)
  - Another thing to keep in mind is that certain hardware may execute division more slowly than multiplication
#### Identifying constant time operations
- The programming language, along with the hardware, can affect what is and is not a constant time operation. For example, most processors perform arithmetic operations as constant time operations, unaffected by operand values.

| Operation                                                                                           | Example                                                                                           |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Addition, subtraction, multiplication, and division of fixed size integer or floating point values. | <pre><code class="language-python">w = 10.4<br>x = 3.4<br>y = 2.0<br>z = (w - x) / y</code></pre> |
| Assignment of a reference, pointer, or other fixed size data value.                                 | <pre><code>x = 1000<br>y = x<br>a = True<br>b = a</code></pre>                                    |
| Comparison of two fixed size data values.                                                           | <pre><code>a = 100<br>b = 200<br>if (b > a):<br>    ...</code></pre>                              |
| Read or write an array element at a particular index.                                               | <pre><code>x = arr[index]<br>arr[index + 1] = x + 1</code></pre>                                  |

### 4.5: Growth of functions and complexity
#### Upper and lower bounds
