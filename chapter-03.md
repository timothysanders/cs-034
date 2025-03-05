# Chapter 3: Introduction to Data Structures and Algorithms

### 3.1: Data Structures
#### Data structures
- **Data structures** are ways of organizing, storing, and performing operations on data, such as accessing/updating stored data, searching for specific data, inserting new data, removing data

| Data structure | Description                                                                                                                                                                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Record         | A **record** is the data structure that stores subitems, often called fields, with a name associated with each subitem.                                                                                                                                                  |
| Array          | An **array** is a data structure that stores an ordered list of items, where each item is directly accessible by a positional index.                                                                                                                                     |
| Linked list    | A **linked list** is a data structure that stores an ordered list of items in nodes, where each node stores data and has a pointer to the next node.                                                                                                                     |
| Binary tree    | A **binary tree** is a data structure in which each node stores data and has up to two children, known as a left child and a right child.                                                                                                                                |
| Hash table     | A **hash table** is a data structure that stores unordered items by mapping (or hashing) each item to a location in an array.                                                                                                                                            |
| Heap           | A **max-heap** is a tree that maintains the simple property that a node's key is greater than or equal to the node's childrens' keys. A **min-heap** is a tree that maintains the simple property that a node's key is less than or equal to the node's childrens' keys. |
| Graph          | A **graph** is a data structure for representing connections among items, and consists of vertices connected by edges. A **vertex** represents an item in a graph. An **edge** represents a connection between two vertices in a graph.                                  |

#### Choosing data structures
- The selection of a data structure depends on the type of data and the operations needed to be performed, often requiring a balance of expected use cases

### 3.2: Introduction to algorithms
#### Algorithms
- **algorithm** describes a sequence of steps to solve a computational problem or perform a calculation. It can be described in English, pseudocode, programming language, etc.
- **computational problem** specifies an input, a question about the input that can be answered using a computer, and the desired output
#### Practical applications of algorithms
- Computational problems can be solved in many different ways, but finding the "best" algorithm can be challenging. However, many computational problems have common subproblems, where efficient algorithms have been developed

| Application domain | Computational problem                                                                                                    | Common algorithm                                                                                                                                                                                                                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNA analysis       | Given two DNA sequences from different individuals, what is the longest shared sequence of nucleotides?                  | *Longest common substring problem*: A longest common substring algorithm determines the longest common substring that exists in two input strings.<br>DNA sequences can be represented using strings consisting of the letters A, C, G, and T to represent the four different nucleotides.                                                                |
| Search engines     | Given a product ID and a sorted array of all in-stock products, is the product in stock and what is the product's price? | *Binary search*: The binary search algorithm is an efficient algorithm for searching a list. The list's elements must be sorted and directly accessible (such as an array).                                                                                                                                                                               |
| Navigation         | Given a user's current location and desired location, what is the fastest route to walk to the destination?              | *Dijkstra's shortest path*: Dijkstra's shortest path algorithm determines the shortest path from a start vertex to each vertex in a graph.<br>The possible routes between two locations can be represented using a graph, where vertices represent specific locations and connecting edges specify the time required to walk between those two locations. |

#### Efficient algorithms and hard problems
- Algorithm efficiency is most commonly measured in algorithm runtime, and an efficient algorithm is one whose runtime increases no more than polynomially with respect to the input size
- **NP-complete** problems are sets of problems for which no known efficient algorithm exists, they must have the following characteristics
  - No efficient algorithm has been found to solve an NP-complete problem
  - No one has proven that an efficient algorithm to solve an NP-complete problem is impossible
  - If an efficient algorithm exists for one NP-complete problem, then all NP-complete problems can be solved efficiently
- If a problem is NP-complete, then the programmer can focus on finding an algorithm that implements a good, but non-optimal, solution

### 3.3: Relation between data structures and algorithms
#### Algorithms for data structures
- Data structures not only define how data is organized and stored, but also the operations performed on the data structure. Common operations include inserting/removing/searching for data, algorithms to implement these operations are typically specific to each data structure
#### Algorithms using data structures
- Some algorithms use data structures to store/organize data during algorithm execution. 

### 3.4 Abstract data types
#### Abstract data types (ADTs)
- **abstract data type** is a data type described by predefined user operations, such as "insert data at rear", without indicating how each operation is implemented. An ADT can be implemented using different underlying data structures, but you do not need to have knowledge of the underlying implementation to use an ADT

| Abstract data type | Description                                                                                                                                                         | Common underlying data structures |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| List               | A **list** is an ADT for holding ordered data.                                                                                                                      | Array, linked list                |
| Dynamic array      | A **dynamic array** is an ADT for holding ordered data and allowing indexed access.                                                                                 | Array                             |
| Stack              | A **stack** is an ADT in which items are only inserted on or removed from the top of a stack.                                                                       | Linked list                       |
| Queue              | A **queue** is an ADT in which items are inserted at the end of the queue and removed from the front of the queue.                                                  | Linked list                       |
| Deque              | A **deque** (pronounced "deck" and short for double-ended queue) is an ADT in which items can be inserted and removed at both the front and back.                   | Linked list                       |
| Bag                | A **bag** is an ADT for storing items in which the order does not matter and duplicate items are allowed.                                                           | Array, linked list                |
| Set                | A **set** is an ADT for a collection of distinct items.                                                                                                             | Binary search tree, hash table    |
| Priority queue     | A **priority queue** is a queue where each item has a priority, and items with higher priority are closer to the front of the queue than items with lower priority. | Heap                              |
| Dictionary (Map)   | A **dictionary** is an ADT that associates (or maps) keys with values.                                                                                              | Hash table, binary search tree    |

### 3.5: Application of ADTs
#### Abstraction and optimization
- Abstraction means having the user interact with an item at a high level, with lower-level internal details hidden from the user. ADTs support abstraction, because the user does not need to know the underlying implementation details, but has a well-defined set of operations for using the ADT
- Abstract data types enable programmers to focus on higher-level operations and algorithms, which can improve efficiency. However, knowing the underlying implementation is needed to analyze or improve the runtime efficiency
#### ADTs in standard libraries
- Most programming languages provide standard libraries that implement common abstract data types, with some allowing the programmer to choose the underlying data structure used for the ADTs, some may have specific data structures for each ADT, or may automatically choose the underlying data structure

| Programming language | Library                          | Common supported ADTs                       |
|----------------------|----------------------------------|---------------------------------------------|
| Python               | Python standard library          | list, set, dict, deque                      |
| C++                  | Standard template library (STL)  | vector, list, deque, queue, stack, set, map |
| Java                 | Java collections framework (JCF) | Collection, Set, List, Map, Queue, Deque    |

### 3.6: Algorithm efficiency
#### Algorithm efficiency
- **Algorithm efficiency** is typically measured by the algorithms computational complexity
- **Computational complexity** is the amount of resources used by the algorithm, with the most commonly considered being runtime and memory usage
#### Runtime complexity, best case, and worst case
- **Runtime complexity** is a function, `T(N)` that represents the number of constant time operations performed by an algorithm on an input of size `N`
- Because algorithm runtime can vary significantly based on the input data, a common approach is to identify best/worst case scenarios
  - **Best case** is the scenario where the algorithm does the minimum possible number of operations
  - **Worst case** is the scenario where the algorithm does the maximum possible number of operations
  - Note that these only describe contents of the algorithms input data, and the input data size must remain a variable, otherwise most algorithms would have a best case where `N=0` and no input would be processed
- An example for linear search best/worse case scenarios is below. The best case scenario is where key == 54, because only one comparison is made. The worst case is where key == 82, because every element is searched and no match is found
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
- Another example with a function to return the first value in a list that is less than the specified value. The best case is where the first item in the list is less than the value. The worst case is where no items in the list are less than the value
```python
def find_first_less_than(list, list_size, value):
    i = 0
    while i < list_size:
        if list[i] < value:
            return list[i]
        i += 1
    return value
```
#### Space complexity
- **Space complexity** of an algorithm is a function, `S(N)` that represents the number of fixed-size memory units used by the algorithm for an input of size `N`. An example of the space complexity for an algorithm that duplicates a list of numbers is `S(N) = 2N + k` where `k` is a constant representing memory used for things like a loop counter and list pointers
- Space complexity includes the input data and additional memory allocated by the algorithm. **Auxiliary space complexity** is the space complexity not including the input data. An example is an algorithm to find the maximum number in a list which will have a space complexity of `S(N) = N + k`, but an auxiliary space complexity of `S(N) = k` (k is constant)
- In the example below, the `find_max()` function has two variables in the function body, `maximum` and `i`. The list size is a variable, `N`, and three integers are used, `list_size`, `maximum`, and `i`, which makes the space complexity `S(N) = N + 3`. The auxiliary space complexity includes only non-input data and is `S(N) = 2`
```python
def find_max(list, list_size):
    if list_size >= 1:
        maximum = list[0]
        i = 1
        while i < list_size:
            if list[i] > maximum:
                maximum = list[i]
            i += 1
        return maximum
```
